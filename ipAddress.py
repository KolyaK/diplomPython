class test_ip:
    def __init__(self, ip):
        self.ip = ip
        self.bin_ip = {}

    def split_ip(self):

        splited_ip = str(self.ip).split(".", 3)
        return splited_ip

    def ip_to_bin(self, splitted_ip):

        i = 0
        for x in splitted_ip:
            self.bin_ip[i] = "{message:{fill}>{width}}".format(message=bin(int(x))[2:], fill="0", width=8)
            i += 1
        return self.bin_ip

    def __str__(self):
        result = str(self.bin_ip[0] + "." + self.bin_ip[1] + "." + self.bin_ip[2] + "." + self.bin_ip[3]).replace(" ", "")
        return result


#ip = test_ip("132.15.11.0")
#ip.ip_to_bin(ip.split_ip())
#ip.__str__()