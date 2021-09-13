# Covert Exfil CTF Challenge

*SPOILERS*

## Challenge Overview

The python script *exfil.py* takes the secret flag data, splits it into 20 bit 
chunks and embeds it in IPv6 flow labels of some crafted packets. the packets 
are ICMP6 echo requests, with random payload data, which is effectivly just a 
red herring (Sorry!).

## Flag

The flag can be tailored per-event, just change *flag.txt*.

## Resouces & Hosting

The only challenge file required is *covert_exfil.pcap*, which can be supplied
along with a challenge description of your choosing. That's it. An example 
challenge description is in *challenge.md*.

It is possible to re-generate the pcap (on Linux) as follows:
```bash
~$ ./capture.tcpdump.sh &
~$ ./exfil.py
~$ fg
~$ ^C
```

## Difficulty

I'm afraid this challenge just depends on checking the various fields in the 
packets and not getting hung up on trying to do anything with the echo data.
Once you have the flow label idea, the challenge is easy/medium to solve, but 
the potential for frustration probably puts it around medium IMO. 

## Solution

A solution is included in *solution.py*.

# In this repo

-- covert_exfil/
 |-- capture.tcpdump.sh             - shell script to re-capture packets
 |-- challenge.md                   - example challenge wording
 |-- covert_exfil.pcap              - challenge file to be supplied to players
 |-- exfil.py                       - script to generate packets for capture
 |-- flag.txt                       - flag file
 |-- README.md                      - this file 
 |-- solution.py                    - solution script
 |-- writeup/                       - writeup resources
 |  |-- extract_flow_labels.py      - example script for flow label extraction
 |  |-- extract_icmp.py             - example script for ICMP payload extraction
 |  |-- \*.png                      - writeup images
 |-- writeup.md                     - writeup file
