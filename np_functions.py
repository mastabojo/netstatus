import os
## https://github.com/alessandromaggio/pythonping
from pythonping import ping

# Checks if array of hosts (URLs, IP addresses) is reachable by ping
def isReachableByPing(targetList, pingCount = 4):
    for target in targetList:
        response_list = ping(target, size = 40, count = pingCount)
        response_iterator = iter(response_list)
        for r in range(pingCount):
            try:
                if(str(next(response_iterator))[:5] == "Reply"):
                    ## On first successful ping return True
                    return True
            except:
                pass
    # If no successful ping return False
    return False

def archiveFile(fileName):
    try:
        dateNow = time.strftime("%Y%m%d", time.localtime(time.time()))
        timeNow = time.strftime("%H%M%S", time.localtime(time.time()))
        archiveLogFile = logFile + "_" + dateNow + "_" + timeNow
        os.rename(fileName, archiveLogFile)
    except:
        pass
