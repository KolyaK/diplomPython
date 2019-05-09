class test_ip:
    def __init__(self, ip):
        self.ip = ip

    def split_ip(self):
        splited_ip = str(self.ip).split(".", 3)
        return splited_ip

    def ip_to_bin(self, splitted_ip):
        bin_ip = ""
        i = 0
        for x in splitted_ip:
            print("{:+b}".format(x))
            i += 1
        return print(bin_ip)



ip = test_ip("132.15.11.0")
ip.ip_to_bin(ip.split_ip())

print('{:*^30}'.format('centered'))