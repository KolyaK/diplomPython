class testIp:
    def __init__(self, ip, mask = None):
        self.ip = ip
        self.bin_ip = {}
        self.mask = mask

    def get_ip(self):
        return self.ip

    def get_bin_ip(self):
        return str(str(self.bin_ip[0] + "." +
                     self.bin_ip[1] +
                     "." + self.bin_ip[2] + "." +
                     self.bin_ip[3]).replace(" ", ""))

    def get_mask(self):
        return self.mask

    def split_ip(self):

        splited_ip = str(self.ip).split(".", 3)
        return splited_ip

    def ip_to_bin(self, splitted_ip):

        i = 0
        for x in splitted_ip:
            self.bin_ip[i] = "{message:{fill}>{width}}".format(message=bin(int(x))[2:], fill="0", width=8)
            i += 1
        return self.bin_ip

    def class_of_ip(self, mask):
        self.mask = int(mask)
        if (self.mask >0 and self.mask <= 8):
            return "Class A"
        elif (self.mask >8 and self.mask <= 16):
            return "Class B"
        elif (self.mask >16 and self.mask <= 24):
            return "Class C"

    def __str__(self):
           result = str(self.bin_ip[0] + "." +
                        self.bin_ip[1] +
                        "." + self.bin_ip[2] + "." +
                        self.bin_ip[3]).replace(" ", "")
           return result

    def wildcard(self):
        pass

    def network(self):
        pass

    def broadcast(self):
        pass

    def host(self):
        pass

#ip = testIp("132.15.11.0")
#ip.ip_to_bin(ip.split_ip())
#print(ip.class_of_ip("20"))
