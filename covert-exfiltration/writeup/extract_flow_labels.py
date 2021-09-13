#!/usr/bin/env python3

from scapy.all import *

packets = sniff(offline='covert_exfil.pcap')    

flow_label = ""
for p in packets:
    # Extract flow label and pad out to 20 bits in case of leading zeros
    flow_label += bin(p['IPv6'].fl)[2:].zfill(20) 

print(f"Got raw flow label bits : {flow_label}")
