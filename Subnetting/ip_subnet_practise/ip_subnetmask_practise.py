'''
    Ip Subnet Calculation Practise, randomized (B & C)
    
    #! FOR VISUAL STUDIO CODE EDITOR

    Author: WattoX00
    Date:   07/11/2023
'''

'''
Ip format:
x.y.z.w/mask
e.g. 192.168.100.1/24
'''

import random

def practise():
    try:
        rand_ = random.randint(16,30)
        full_ip = str()
        for i in range(4):
            if i <= 2:
                full_ip+=str(random.randint(0,255))
                full_ip=str(full_ip)+"."
            else:
                full_ip+=str(random.randint(0,255))
        full_ip=full_ip+"/"+str(rand_)
        print(full_ip)
        mask = full_ip.split("/")
        ip = mask[0].split(".")
        mask=int(mask[1])
        octet_decimal=0
        bit = [128,64,32,16,8,4,2,1]
        network = int()
        broadcast = int()
        first_ip = int()
        last_ip = int()
        if mask > 0 and mask < 31:
            if mask >= 24:
                bit_needed = mask-24
                for i in range(bit_needed):
                    octet_decimal+=bit[i]
                steps = 256-octet_decimal
                octet = int(ip[-1])
                x = int()
                start_ip = str()
                for e in range(len(ip)-1):
                    start_ip += ip[e]+"."
                while True:
                    if octet >= steps*x and octet <= (steps*(x+1))-1:
                        network = steps*x
                        broadcast = (steps*(x+1))-1
                        first_ip = network+1
                        last_ip = broadcast-1
                        network = str(start_ip)+str(network)
                        broadcast = str(start_ip)+str(broadcast)
                        first_ip = str(start_ip)+str(first_ip)
                        last_ip = str(start_ip)+str(last_ip)
                        break
                    else:
                        x+=1
            elif mask >= 16:
                bit_needed = mask-16
                for i in range(bit_needed):
                    octet_decimal+=bit[i]
                steps = 256-octet_decimal
                octet = int(ip[-2])
                start_ip = str()
                x = int()
                for e in range(len(ip)-2):
                    start_ip += ip[e]+"."
                while True:
                    if octet >= steps*x and octet <= (steps*(x+1))-1:
                        network = steps*x
                        broadcast = (steps*(x+1))-1
                        first_ip = network
                        last_ip = broadcast

                        network = str(start_ip)+str(network)+".0"
                        broadcast = str(start_ip)+str(broadcast)+".255"
                        first_ip = str(start_ip)+str(first_ip)+".1"
                        last_ip = str(start_ip)+str(last_ip)+".254"
                        break
                    else:
                        x+=1
        else:
            print("Wrong")
        print_able = str()
        network_q = str(input("Network: "))
        broadcast_q = str(input("Broadcast: "))
        first_ip_q = str(input("First Ip: "))
        last_ip_q = str(input("Last Ip: ")) 
        if network_q == network:
            print_able+= network+"\n"
        else:
            print_able+= network+"\n"
        
        if broadcast_q == broadcast:
            print_able+= broadcast+"\n"
        else:
            print_able+= broadcast+"\n"
        
        if first_ip_q == first_ip:
            print_able+= first_ip+"\n"
        else:
            print_able+= first_ip+"\n"
        
        if last_ip_q == last_ip:
            print_able+= last_ip+"\n"
        else:
            print_able+= last_ip+"\n"
        print(print_able)
    except (KeyboardInterrupt,ValueError):
        print("\nExiting the program.")
        quit()
        
while True:
    practise()