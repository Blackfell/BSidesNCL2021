from scapy.all import *

packets = sniff(offline='covert_exfil.pcap')

for p in packets:
    print(p['ICMPv6EchoRequest'].data.decode(), end="") 
print('') 
