#!/usr/bin/env bash
sudo tcpdump -i lo -s0 -l -X "ip6" -w covert_exfil.pcap
