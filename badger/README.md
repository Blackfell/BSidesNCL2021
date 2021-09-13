# Badger CTF Challenge

*SPOILERS*

## Challenge Overview

This is an *easy* pwn/reversing challenge built around a 'badge printer' for 
a virtual BSides event. The program takes user input and creates a 'badge', but 
there is no bounds checking on an array index used to select a tagline for the 
badge. The flag is read into the stack inside a function, but the frame is torn 
down, the players must reference the old stack frame and use the flag pointer 
still present to print off the flag. 

## Flag

The flag can be tailored per-event, but must be less than `0x50` bytes. Just 
change *./private/flag.txt*, it's got two example values in already, top one is 
used. 

## Resouces & Hosting

The challenge is intended to be hosted via Docker, all files needed for challenge
hosting are in *./private/*. The *run_challenge.sh* script is intended to allow a 
single line to run the challenge container, but tweaking ports exposed etc. should 
cause zero problems.

## Solution

A solution is included in [*solution.py*](./solution.py). See 
[*writeup.md*](./writeup.md) for more info.

