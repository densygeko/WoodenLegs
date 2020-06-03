from scapy.all import *

class PCAPReader:
    
    def ReadFile(self, file): #Takes a pcap file and returns all ip addresses.
        pcap = rdpcap(file) #Read .pcap file
        ipAddresses = []
        ips = set([(p[IP].fields['src'], p[IP].fields['dst']) for p in pcap if p.haslayer(IP) ==1]) #Extract ip addresses as Source + Destination sets

        for ip in ips: #Add ips to list
            ipAddresses.append(ip[0])
            ipAddresses.append(ip[1])

        return ipAddresses


