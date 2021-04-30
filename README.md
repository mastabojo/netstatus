# netstatus

Scripts for checking net status

Main goal is to automatically monitor internet access from LAN and records details about connection dropouts when they occur. 

There might be many reasons for connection dropouts, namely:

* Error beyond ISP
* Error at the ISP
* ISP/internal DNS failure
* WAN modem failure
* LAN router/switch failure (wired/wireless)
* Internal DNS failure
* Local NIC failure

All above points shall be checked using best methods as outlined below.

## Using ping

* Check internet connectivity pinging outside URL (i.e. google.com)
* If pinging URL does not work check DNS servers (internal, ISP)
* If pinging URL does not work and DNS works check connectivity pinging outside public IP address
* If pinging outside IP does not work ping your ISP gateway IP address 
* If pinging ISP gateway IP address does not work ping routers WAN IP address (if known i.e. static)
* If pinging routers WAN IP address does not work ping routers LAN IP address
* If pinging routers LAN IP address does not work ping local NIC

## Using speedtest CLI

* Check internet connectivity and speed using speedtest CLI (https://www.speedtest.net/apps/cli)

TBD

Local IP addresses, URIs and other stuff are set up in the config file.

# Public IP addresses

These public addresses can be used to test connection:

| URL | IP |
|-----|----|
| google-public-dns-a.google.com | 8.8.8.8 |
| google-public-dns-b.google.com | 8.8.4.4 |
| cloudflare DNS resolver | 1.1.1.1, 1.0.0.1 |
| ns1.telstra.net | 139.130.4.5 |
