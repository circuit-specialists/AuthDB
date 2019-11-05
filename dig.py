from requests import get
import socket

class DIG:
    def __init__(self):
        hostname = self.getHOSTNAME()
        lan = self.getLAN_IP()
        wan = self.getWAN_IP()

    def getHOSTNAME(self):
        hostname = socket.gethostname()
        return ("My Hostname is: " + hostname)

    def getLAN_IP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return ('My local IP address is: %s' % IP)

    def getWAN_IP(self):
        ip = get('https://api.ipify.org').text
        return ('My public IP address is: %s' % ip)