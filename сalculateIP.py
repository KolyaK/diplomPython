class СalculateIp:
    def __init__(self, ip):
        self.ip = ip
        self.bin_ip = {}
        self.splitted_ip = str(self.ip).split(".", 3)

    def get_splet_ip(self):
        return self.splitted_ip

    def set_mask(self, mask):
        self.mask = int(mask)

    def get_ip(self):
        return self.ip

    def get_bin_ip(self):
        return "{first}.{second}.{third}.{fourth}".format(first=self.bin_ip[0:8],
                                                          second=self.bin_ip[8:16],
                                                          third=self.bin_ip[16:24],
                                                          fourth=self.bin_ip[24:32])

    def get_mask(self):
        return self.mask

    def ip_to_bin(self):
        i = 0
        bin_ip = {}
        for x in self.splitted_ip:
            bin_ip[i] = "{message:{fill}>{width}}".format(message=bin(int(x))[2:], fill="0", width=8)
            i += 1
        self.bin_ip = bin_ip[0] + bin_ip[1] + bin_ip[2] + bin_ip[3]
        return self.bin_ip

    def class_of_ip(self, mask):
        mask = int(mask)
        if (mask >0 and mask <= 8):
            return "Class A"
        elif (mask >8 and mask <= 16):
            return "Class B"
        elif (mask >16 and mask <= 24):
            return "Class C"

    def bin_mask(self):
        bin_mask = "{binary_mask:{fill}<32}".format(binary_mask="1"*self.mask, fill="0")
        return str(bin_mask[0:8] + "." + bin_mask[8:16] + "." + bin_mask[16:24] + "." + bin_mask[24:])

    def bin_wildcard(self):
        СalculateIp.wildcard = "{binary_wildcard:{fill}<32}"\
            .format(binary_wildcard="0"*int(self.mask), fill=1)
        return СalculateIp.wildcard

    def get_bin_wildcard(self):
        self.bin_wildcard()
        return str(СalculateIp.wildcard[0:8] + "." + СalculateIp.wildcard[8:16] + "." \
                   + СalculateIp.wildcard[16:24] + "." + \
                   СalculateIp.wildcard[24:])

    def get_dec_wildcard(self):
        self.bin_wildcard()
        return "{first}.{second}.{third}.{fourth}".format(first=int(СalculateIp.wildcard[0:8], 2),
                                                          second=int(СalculateIp.wildcard[8:16], 2),
                                                          third=int(СalculateIp.wildcard[16:24], 2),
                                                          fourth=int(СalculateIp.wildcard[24:32], 2))

    def bin_network(self):
        binary_ip = str(self.bin_ip[0:8] + self.bin_ip[8:16] + self.bin_ip[16:24] + self.bin_ip[24:32])
        return binary_ip[0:self.mask] + "0"*(32-self.mask)

    def get_network(self):
        network = self.bin_network()
        return "{first}.{second}.{third}.{fourth}".format(first=int(network[0:8], 2),
                                                          second=int(network[8:16], 2),
                                                          third=int(network[16:24], 2),
                                                          fourth=int(network[24:32], 2))

    def bin_broadcast(self):
        broadcast = self.bin_network()
        return broadcast[:self.mask] + "1" * (32-self.mask)

    def get_bin_broadcast(self):
        res = self.bin_broadcast()
        return "{first}.{second}.{third}.{fourth}".format(first=int(res[0:8]),
                                                          second=int(res[8:16]),
                                                          third=int(res[16:24]),
                                                          fourth=int(res[24:32]))

    def decimal_broadcast(self):
        dec_broadcast = self.bin_broadcast()
        return "{first}.{second}.{third}.{fourth}".format(first=int(dec_broadcast[0:8], 2),
                                                          second=int(dec_broadcast[8:16], 2),
                                                          third=int(dec_broadcast[16:24], 2),
                                                          fourth=int(dec_broadcast[24:32], 2))

    def host(self):
        hosts = str(pow(2, (32-self.mask))-2)
        return hosts
