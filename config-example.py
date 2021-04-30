# Path to CSV file for logging
pingLogCsv = "ping_log.csv"

# Do we write results in influxdb
writeInfluxDb = False

# InfluxDB password
inflpass = "influxdb_password"

# Max size of log file in bytes
maxFileSize = 100000

# List of known public URLs that can be pinged
public_urls = [
    "google-public-dns-a.google.com",
    "google-public-dns-b.google.com",
    "ns1.telstra.net"
]

# List of known public IPV4 addresses that can be pinged
public_ipv4_addresses = [
    "8.8.8.8",    # google-public-dns-a.google.com
    "8.8.4.4",    # google-public-dns-b.google.com
    "1.1.1.1",    # cloudflare_resolver_1
    "1.0.0.1",    # cloudflare_resolver_2
    "139.130.4.5" # ns1.telstra.net
]

## WAN gateway address provided by ISP
isp_gateway_ipv4_addresses = [
    "your-wan-gateway-ip4"
]

## DNS servers IPV4 addresses
dns_ipv4_addresses = [
    "your-dns-ip4"
]

## LAN gateway IPV4 address
local_ipv4_gateway = [
    "your-local-gateway-ip4"
]

## Router WAN IP address (as assigned by ISP, hopefully static) 
router_wan_ipv4_addresses = [
    "router_wan_ipv4"
]

## List of LAN IP addresses that can be pinged
local_ipv4_addresses = [
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4"
]

## Local NIC (loopback address)
local_ipv4_loopback = [
    "127.0.0.1"
]

# Status codes saved in the log file
status_codes = {
    0: "Public URLs accessible",
    1: "DNS accessible",
    2: "Public IPs accessible",
    3: "ISP GW accessible",
    4: "Router public IP accessible",
    5: "Router local IP accessible",
    6: "Local IPs accessible",
    7: "NIC accessible",
    8: "Nothing accessible",
}