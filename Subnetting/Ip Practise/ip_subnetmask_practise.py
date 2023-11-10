'''
    Ip Subnet Calculation Practise, randomized (B & C)

    Author: WattoX00
    Date:   07/11/2023
'''

'''
Ip format:
x.y.z.w/mask
e.g. 192.168.100.1/24
'''
import random
try:
    def c_ip():
        print_able: str = str()
        subnet_multiplier: int = int()
        octet_decimal: int = int()
        bit_needed = mask-24
        for i in range(bit_needed):
            octet_decimal+=bit[i]
        steps = 256-octet_decimal
        octet = int(ip[-1])
        subnet_multiplier = int()
        start_ip = str()
        for e in range(len(ip)-1):
            start_ip += ip[e]+"."
        while True:
            if octet >= steps*subnet_multiplier and octet <= (steps*(subnet_multiplier+1))-1:
                network = steps*subnet_multiplier
                broadcast = (steps*(subnet_multiplier+1))-1
                first_ip = network+1
                last_ip = broadcast-1
                network = str(start_ip)+str(network)
                broadcast = str(start_ip)+str(broadcast)
                first_ip = str(start_ip)+str(first_ip)
                last_ip = str(start_ip)+str(last_ip)
                break
            else:
                subnet_multiplier+=1
        print()
        counter: int = int()
        network_q = str(input("Network: "))
        broadcast_q = str(input("Broadcast: "))
        first_ip_q = str(input("First Ip: "))
        last_ip_q = str(input("Last Ip: ")) 
        if network_q == network:
            print_able+= str(network)+"\n"
            counter+=1
        else:
            print_able+= str(network)+"\n"
        
        if broadcast_q == broadcast:
            print_able+= str(broadcast)+"\n"
            counter+=1
        else:
            print_able+= str(broadcast)+"\n"
        
        if first_ip_q == first_ip:
            print_able+= str(first_ip)+"\n"
            counter+=1
        else:
            print_able+= str(first_ip)+"\n"
        
        if last_ip_q == last_ip:
            print_able+= str(last_ip)+"\n"
            counter+=1
        else:
            print_able+= str(last_ip)+"\n"
        print()
        print(print_able)
        print(str(counter)+"/4")

    def b_ip():
        print_able: str = str()
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

                network = str(start_ip)+str(network)+".0"
                broadcast = str(start_ip)+str(broadcast)+".255"
                first_ip = str(start_ip)+str(first_ip)+".1"
                last_ip = str(start_ip)+str(last_ip)+".254"
                break
            else:
                subnet_multiplier+=1
        print()
        counter: int = int()
        network_q = str(input("Network: "))
        broadcast_q = str(input("Broadcast: "))
        first_ip_q = str(input("First Ip: "))
        last_ip_q = str(input("Last Ip: ")) 
        if network_q == network:
            print_able+= str(network)+"\n"
            counter+=1
        else:
            print_able+= str(network)+"\n"
        
        if broadcast_q == broadcast:
            print_able+= str(broadcast)+"\n"
            counter+=1
        else:
            print_able+= str(broadcast)+"\n"
        
        if first_ip_q == first_ip:
            print_able+= str(first_ip)+"\n"
            counter+=1
        else:
            print_able+= str(first_ip)+"\n"
        
        if last_ip_q == last_ip:
            print_able+= str(last_ip)+"\n"
            counter+=1
        else:
            print_able+= str(last_ip)+"\n"
        print()
        print(print_able)
        print(str(counter)+"/4")

    while True:
        full_ip = str()
        for i in range(4):
            if i <= 2:
                full_ip+=str(random.randint(0,255))
                full_ip=str(full_ip)+"."
            else:
                full_ip+=str(random.randint(0,255))
        full_ip=full_ip+"/"+str(random.randint(16,30))
        print()
        print(full_ip)
        mask = full_ip.split("/")
        ip = mask[0].split(".")
        mask=int(mask[1])
        bit = [128,64,32,16,8,4,2,1]
        if mask >= 24 and mask < 31:
            c_ip()
        elif mask >= 16 and mask < 24:
            b_ip()
except KeyboardInterrupt:
    print("\n\nExiting the program!")
    quit()