# Check Internet connection by sending ping starting from public targets down to local targets
# Sequence of pings:
# 1. Public URLs (google.com, ...)
# 2. DNS (local, ISP)
# 3. Public IPs (8.8.8.8., ...)
# 4. ISP GW
# 5. Public router IP
# 6. Local router IP
# 7. Local IPs (known machines IP addresses)
# 8. NIC (loopback)
#
# Write results in a CSV file or database
#
# Add line such as this to root crontab to run i.e. every 10 + 1 minutes
# 1,11,21,31,41,51 * * * * /usr/bin/python3 /path/to/netping.py

import os
import csv
import time
import config as cnf
import np_functions as np
if(cnf.writeInfluxDb):
    from influxdb import InfluxDBClient

connectionOk = True
errors = []
statusNo = 8
csvHeader = ["Date", "Time", "Status Number", "Status description", "Additional info"]

dateNow = time.strftime("%Y-%m-%d", time.localtime(time.time()))
timeNow = time.strftime("%H:%M:%S", time.localtime(time.time()))

## 1. Ping public URLs
if np.isReachableByPing(cnf.public_urls):
    connectionOk = True
    statusNo = 0
else:
    connectionOk = False
    errors.append("Public URLs")

## 2. Ping DNS servers
if not connectionOk:
    if np.isReachableByPing(cnf.dns_ipv4_addresses):
        connectionOk = True
        statusNo = 1
    else:
        connectionOk = False
        errors.append("DNS servers")
    
## 3. Ping public IPs
if not connectionOk:
    if np.isReachableByPing(cnf.public_ipv4_addresses):
        connectionOk = True
        statusNo = 2
    else:
        connectionOk = False
        errors.append("Public IPs")

## 4. Ping ISP GW
if not connectionOk:
    if np.isReachableByPing(cnf.isp_gateway_ipv4_addresses):
        connectionOk = True
        statusNo = 3
    else:
        connectionOk = False
        errors.append("ISP GW")

## 5. Ping router public IP
if not connectionOk:
    if np.isReachableByPing(cnf.router_wan_ipv4_addresses):
        connectionOk = True
        statusNo = 4
    else:
        connectionOk = False
        errors.append("ISP GW")

## 6. Ping LAN GW (router)
if not connectionOk:
    if np.isReachableByPing(cnf.local_ipv4_gateway):
        connectionOk = True
        statusNo = 5
    else:
        connectionOk = False
        errors.append("Local GW")

## 7. Ping local IPs
if not connectionOk:
    if np.isReachableByPing(cnf.local_ipv4_addresses):
        connectionOk = True
        statusNo = 6
    else:
        connectionOk = False
        errors.append("Local IPs")

## 8. Ping NIC
if not connectionOk:
    if np.isReachableByPing(cnf.local_ipv4_loopback):
        connectionOk = True
        statusNo = 7
    else:
        connectionOk = False
        errors.append("NIC (loopback)")

if len(errors) == 0:
    csvRow = [dateNow, timeNow, statusNo, cnf.status_codes[statusNo], "Connection OK"]
    print("Connection OK")
else:
    csvRow = [dateNow, timeNow, statusNo, cnf.status_codes[statusNo], ", ".join(errors)]
    print("NOT accessible: " + ", ".join(errors))

# If file does not exist write header row
if not os.path.isfile(cnf.pingLogCsv):
    with open(cnf.pingLogCsv, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter =';', quotechar ='"', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(csvHeader)

# Append to file
with open(cnf.pingLogCsv, 'a+', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter =';', quotechar ='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(csvRow)

# Check the size of the file
if(os.path.getsize(cnf.pingLogCsv) > cnf.maxFileSize):
    np.archiveFile(cnf.pingLogCsv)

# Write to InfluxDB
if(cnf.writeInfluxDb):
    if(statusNo == 0):
        msg = 'conn_ok'
    else:
        msg = cnf.status_codes[statusNo], ", ".join(errors)
    conn_data = [
        {
            "measurement": "pingtest",
            "tags": {
                "method": "ping",
                "message": msg
            },
            "fields": {
                "status": statusNo
            }
        }
    ]
    client = InfluxDBClient(host='localhost', port=8086, username='admin', password=cnf.inflpass)
    client.switch_database('connectivity')
    client.write_points(conn_data)
