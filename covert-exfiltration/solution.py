#!/usr/bin/env python3

from scapy.all import *
from sys import exit

def bits_to_string(message):
    """8 bit ASCII assumed for flag - watch out if not"""
    s = ""
    for i in range(0, len(message), 8):
        bits = message[i:i+8]       # 8 bits for our character
        s += chr(int(bits, 2))   # Convert from bits to ascii
    return s

packets = sniff(offline='covert_exfil.pcap')    

flag = ""
for p in packets:
    flag += bin(p['IPv6'].fl)[2:].zfill(20) # Extract flow label and pad out to 20 bits

print(f"Got raw flag : {flag}")
print(f"Flag is : {bits_to_string(flag)}")
