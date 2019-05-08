class IpAddress():
    def __init__(self, ip=None):
        self.ip = ip

    def ip(self, ip):
        splitIp = str(ip).split(".", 3)
        return splitIp

    def ip_to_bin(self, splited_ip):
        i=0
        for x in splited_ip:
            print(bin(int(x)))
            self.bin_splited_ip[i] = x
            i += 1

        return self.bin_splited_ip


ipCalc = IpAddress()
ipCalc.ip("192.102.0.15")
ipCalc.ip_to_bin(ipCalc.ip("192.102.0.15"))

