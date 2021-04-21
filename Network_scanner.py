# Project : NetWork_Scanner.py
# Language in Used : Python
# Author : Rajdip
  
import scapy.all as scapy

def Scan_Network(IP):
    arp_request = scapy.ARP(pdst=IP)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answerd = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []

    for element in answerd:
        client_dict = {"IP" : element[1].psrc, "MAC" : element[1].hwsrc }
        client_list.append(client_dict)
    return client_list

def print_result(resullt_list):
    print("IP\t\t\tMAC ADDRESS\n-------------------------------")
    for client in resullt_list:
        print(client["IP"] + client["MAC"])


result = Scan_Network("192.1688.1.1/24")
print_result(result)
