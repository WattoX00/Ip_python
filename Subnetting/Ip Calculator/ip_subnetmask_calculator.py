'''
    Ip Subnet Calculator (A,B,C)

    Author: WattoX00
    Date:   07/11/2023
'''

'''
Ip format:
x.y.z.w/mask
e.g. 192.168.100.1/24
'''
try:
    def c_ip():
        subnet_multiplier: int = int()
        octet_decimal: int = int()
        bit_needed = mask-24
        for i in range(bit_needed):
            octet_decimal+=bit[i]
        steps = 256-octet_decimal
        octet = int(ip[-1])
        start_ip = str()
        for e in range(len(ip)-1):
            start_ip += ip[e]+"."
        while True:
            if octet >= steps*subnet_multiplier and octet <= (steps*(subnet_multiplier+1))-1:
                network = steps*subnet_multiplier
                network_bin = bin(network).replace('0b','')
                broadcast = (steps*(subnet_multiplier+1))-1
                broadcast_bin = bin(broadcast).replace('0b','')
                first_ip = network+1
                first_bin = bin(first_ip).replace('0b','')
                last_ip = broadcast-1
                last_bin = bin(last_ip).replace('0b','')
                network = str(start_ip)+str(network).ljust(ljust_width)+"\t"
                broadcast = str(start_ip)+str(broadcast).ljust(ljust_width)+"\t"
                first_ip = str(start_ip)+str(first_ip).ljust(ljust_width)+"\t"
                last_ip = str(start_ip)+str(last_ip).ljust(ljust_width)+"\t"
                print("Network: "+network,network_bin+"\n"
                    "Broadcast: "+broadcast,broadcast_bin+"\n"
                    "First Ip: "+first_ip,first_bin+"\n"
                    "Last Ip: "+last_ip,last_bin)
                break
            else:
                subnet_multiplier+=1
    def b_ip():
        subnet_multiplier: int = int()
        octet_decimal: int = int()
        bit_needed = mask-16
        for i in range(bit_needed):
            octet_decimal+=bit[i]
        steps = 256-octet_decimal
        octet = int(ip[-2])
        start_ip = str()
        for e in range(len(ip)-2):
            start_ip += ip[e]+"."
        while True:
            if octet >= steps*subnet_multiplier and octet <= (steps*(subnet_multiplier+1))-1:
                network = steps*subnet_multiplier
                broadcast = (steps*(subnet_multiplier+1))-1
                first_ip = network
                last_ip = broadcast
                print("Network: "+str(start_ip)+str(network)+".0".ljust(ljust_width)+"\t","00000000"+"\n"
                    "Broadcast: "+str(start_ip)+str(broadcast)+".255".ljust(ljust_width)+"\t","11111111"+"\n"
                    "First Ip: "+str(start_ip)+str(first_ip)+".1".ljust(ljust_width)+"\t","00000001"+"\n"
                    "Last Ip: "+str(start_ip)+str(last_ip)+".254".ljust(ljust_width)+"\t","11111110")
                break
            else:
                subnet_multiplier+=1
    def a_ip():
        subnet_multiplier: int = int()
        octet_decimal: int = int()
        bit_needed = mask-8
        for i in range(bit_needed):
            octet_decimal+=bit[i]
        steps = 256-octet_decimal
        octet = int(ip[-3])
        start_ip = str()
        for e in range(len(ip)-3):
            start_ip += ip[e]+"."
        while True:
            if octet >= steps*subnet_multiplier and octet <= (steps*(subnet_multiplier+1))-1:
                network = steps*subnet_multiplier
                broadcast = (steps*(subnet_multiplier+1))-1
                first_ip = network
                last_ip = broadcast
                print("Network: "+str(start_ip)+str(network)+".0.0".ljust(ljust_width)+"\t","00000000"+"\n"
                    "Broadcast: "+str(start_ip)+str(broadcast)+".255.255".ljust(ljust_width),"11111111"+"\n"
                    "First Ip: "+str(start_ip)+str(first_ip)+".0.1".ljust(ljust_width)+"\t","00000001"+"\n"
                    "Last Ip: "+str(start_ip)+str(last_ip)+".255.254".ljust(ljust_width)+"\t","11111110")
                break

            else:
                subnet_multiplier+=1
    def under_ip():
        subnet_multiplier: int = int()
        octet_decimal: int = int()
        bit_needed = mask
        for i in range(bit_needed):
            octet_decimal+=bit[i]
        steps = 256-octet_decimal
        octet = int(ip[-4])
        start_ip = str()
        for e in range(len(ip)-4):
            start_ip += ip[e]+"."
        while True:
            if octet >= steps*subnet_multiplier and octet <= (steps*(subnet_multiplier+1))-1:
                network = steps*subnet_multiplier
                broadcast = (steps*(subnet_multiplier+1))-1
                first_ip = network
                last_ip = broadcast
                print("Network: "+str(start_ip)+str(network)+".0.0.0".ljust(ljust_width)+"\t","00000000"+"\n"
                    "Broadcast: "+str(start_ip)+str(broadcast)+".255.255.255".ljust(ljust_width)+"\t","11111111"+"\n"
                    "First Ip: "+str(start_ip)+str(first_ip)+".0.0.1".ljust(ljust_width)+"\t","00000001"+"\n"
                    "Last Ip: "+str(start_ip)+str(last_ip)+".255.255.254".ljust(ljust_width)+"\t","11111110")
                break
            else:
                subnet_multiplier+=1

    while True:
        print()
        raw_ip: str = str(input("ip+mask: "))
        print()
        mask: list = raw_ip.split("/")
        if len(mask) != 2:
                raise ValueError("Invalid input format. Please use IP+Mask format.")
        ip: list = mask[0].split(".")
        mask = int(mask[1])
        ljust_width: int = 15
        network: int = int()
        broadcast: int = int()
        first_ip: int = int()
        last_ip: int = int()
        bit: list = [128,64,32,16,8,4,2,1]

        if mask >= 24 and mask < 31:      
            c_ip()
        elif mask >= 16 and mask < 24:
            b_ip()
        elif mask >= 8 and mask < 16:
            a_ip()
        elif mask >= 0:
            under_ip()
        else:
            pass
except (KeyboardInterrupt,ValueError,IndexError):
    print("\nExiting the program.")
    quit()