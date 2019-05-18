class testIp:
    def __init__(self, ip, wildcard = None):
        self.ip = ip
        self.bin_ip = {}
        self.wildcard = wildcard
        self.splitted_ip = str(self.ip).split(".", 3)

    def get_splet_ip(self):
        return str(self.splitted_ip[0] + "." + \
               self.splitted_ip[1] + "." +\
               self.splitted_ip[2] + "." + \
               self.splitted_ip[3])

    def set_mask(self, mask):
        self.mask = int(mask)

    def get_ip(self):
        return self.ip

    def get_bin_ip(self):
        return str(self.bin_ip[0] + "." +
                     self.bin_ip[1] +
                     "." + self.bin_ip[2] + "." +
                     self.bin_ip[3]).replace(" ", "")

    def get_mask(self):
        return self.mask



    def ip_to_bin(self):
        i = 0
        for x in self.splitted_ip:
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

    def bin_mask(self):
        bin_mask = "{binary_mask:{fill}<32}".format(binary_mask="1"*self.mask, fill="0")
        return str(bin_mask[0:8] + "." + bin_mask[8:16] + "." + bin_mask[16:24] + "." + bin_mask[24:])

    def bin_wildcard(self):
        self.wildcard = "{binary_wildcard:{fill}<32}"\
            .format(binary_wildcard="0"*int(self.mask), fill=1)
        return str(self.wildcard[0:8] + "."\
               + self.wildcard[8:16] + "."\
               + self.wildcard[16:24] + "." +\
               self.wildcard[24:])

    def decimal_wildcard(self):

        return

    def network(self):
        pass

    def broadcast(self):
        pass

    def host(self):
        pass
  #  def __str__(self):
  #         result = str(self.bin_ip[0] + "." +
  #                      self.bin_ip[1] +
  #                      "." + self.bin_ip[2] + "." +
  #                      self.bin_ip[3]).replace(" ", "")
  #         return result


#ip = testIp("132.15.11.0")
#ip.ip_to_bin(ip.split_ip())
#print(ip.class_of_ip("20"))
#print(ip.bin_mask())
#print(ip.bin_wildcard())
#print("wildcard     " + ip.get_wildcard())
#print(ip.get_mask())