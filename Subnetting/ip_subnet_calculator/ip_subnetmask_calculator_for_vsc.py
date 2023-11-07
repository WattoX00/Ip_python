'''
    Ip Subnet Calculator (A,B,C)
    
    #! FOR VISUAL STUDIO CODE EDITOR

    Author: WattoX00
    Date:   30/10/2023
'''

'''
Ip format:
x.y.z.w/mask
e.g. 192.168.100.1/24
'''
print("Format: e.g., 192.168.100.1/24")
def calculator():
    try:
        raw_ip = str(input("ip+mask: "))
        octet_decimal = int()
        mask = raw_ip.split("/")
        if len(mask) != 2:
                raise ValueError("Invalid input format. Please use IP+Mask format.")
        ip = mask[0].split(".")
        mask=int(mask[1])
        x_width = 15
        x = int()
        network = int()
        broadcast = int()
        first_ip = int()
        last_ip = int()
        bit = [128,64,32,16,8,4,2,1]
        if mask > 0 and mask < 31:
            if mask >= 24:
                bit_needed = mask-24
                for i in range(bit_needed):
                    octet_decimal+=bit[i]
                steps = 256-octet_decimal
                octet = int(ip[-1])
                start_ip = str()
                for e in range(len(ip)-1):
                    start_ip += ip[e]+"."
                while True:
                    if octet >= steps*x and octet <= (steps*(x+1))-1:
                        network = steps*x
                        network_bin = bin(network)
                        broadcast = (steps*(x+1))-1
                        broadcast_bin = bin(broadcast)
                        first_ip = network+1
                        first_bin = bin(first_ip)
                        last_ip = broadcast-1
                        last_bin = bin(last_ip)
                        network = str(start_ip)+str(network).ljust(x_width)+"\t"
                        broadcast = str(start_ip)+str(broadcast).ljust(x_width)+"\t"
                        first_ip = str(start_ip)+str(first_ip).ljust(x_width)+"\t"
                        last_ip = str(start_ip)+str(last_ip).ljust(x_width)+"\t"
                        print("Network: \033[34m"+network,network_bin+"\n"
                            "\033[0mBroadcast: \033[34m"+broadcast,broadcast_bin+"\n"
                            "\033[0mFirst Ip: \033[34m"+first_ip,first_bin+"\n"
                            "\033[0mLast Ip: \033[34m"+last_ip,last_bin+"\033[0m")
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
                for e in range(len(ip)-2):
                    start_ip += ip[e]+"."
                while True:
                    if octet >= steps*x and octet <= (steps*(x+1))-1:
                        network = steps*x
                        broadcast = (steps*(x+1))-1
                        first_ip = network
                        last_ip = broadcast
                        print("Network: \033[34m"+str(start_ip)+str(network)+".0".ljust(x_width)+"\t","00000000"+"\n"
                            "\033[0mBroadcast: \033[34m"+str(start_ip)+str(broadcast)+".255".ljust(x_width)+"\t","11111111"+"\n"
                            "\033[0mFirst Ip: \033[34m"+str(start_ip)+str(first_ip)+".1".ljust(x_width)+"\t","00000001"+"\n"
                            "\033[0mLast Ip: \033[34m"+str(start_ip)+str(last_ip)+".254".ljust(x_width)+"\t","11111110"+"\033[0m")
                        break
                    else:
                        x+=1
            elif mask >= 8:
                bit_needed = mask-8
                for i in range(bit_needed):
                    octet_decimal+=bit[i]
                steps = 256-octet_decimal
                octet = int(ip[-3])
                start_ip = str()
                for e in range(len(ip)-3):
                    start_ip += ip[e]+"."
                while True:
                    if octet >= steps*x and octet <= (steps*(x+1))-1:
                        network = steps*x
                        broadcast = (steps*(x+1))-1
                        first_ip = network
                        last_ip = broadcast
                        print("Network: \033[34m"+str(start_ip)+str(network)+".0.0".ljust(x_width)+"\t","00000000"+"\n"
                            "\033[0mBroadcast: \033[34m"+str(start_ip)+str(broadcast)+".255.255".ljust(x_width),"11111111"+"\n"
                            "\033[0mFirst Ip: \033[34m"+str(start_ip)+str(first_ip)+".0.1".ljust(x_width)+"\t","00000001"+"\n"
                            "\033[0mLast Ip: \033[34m"+str(start_ip)+str(last_ip)+".255.254".ljust(x_width)+"\t","11111110"+"\033[0m")
                        break

                    else:
                        x+=1
            elif mask >= 0:
                bit_needed = mask
                for i in range(bit_needed):
                    octet_decimal+=bit[i]
                steps = 256-octet_decimal
                octet = int(ip[-4])
                start_ip = str()
                for e in range(len(ip)-4):
                    start_ip += ip[e]+"."
                while True:
                    if octet >= steps*x and octet <= (steps*(x+1))-1:
                        network = steps*x
                        broadcast = (steps*(x+1))-1
                        first_ip = network
                        last_ip = broadcast
                        print("Network: \033[34m"+str(start_ip)+str(network)+".0.0.0".ljust(x_width)+"\t","00000000"+"\n"
                            "\033[0mBroadcast: \033[34m"+str(start_ip)+str(broadcast)+".255.255.255".ljust(x_width)+"\t","11111111"+"\n"
                            "\033[0mFirst Ip: \033[34m"+str(start_ip)+str(first_ip)+".0.0.1".ljust(x_width)+"\t","00000001"+"\n"
                            "\033[0mLast Ip: \033[34m"+str(start_ip)+str(last_ip)+".255.255.254".ljust(x_width)+"\t","11111110"+"\033[0m")
                        break
                    else:
                        x+=1
        else:
            print("Wrong mask!")
    except (KeyboardInterrupt,ValueError):
        print("\nExiting the program.")
        quit()
while True:
    calculator()