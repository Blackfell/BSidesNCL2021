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
change *flag.txt*, it's got two example values in already, top one is used. 

## Resouces & Hosting

The challenge is intended to be hosted via Docker; the included script 
*run_challenge.sh* is intended to allow a single line running of the challenge 
container, but tweaking ports exposed etc. should cause zero problems.

The generate_files.sh script creates the required challenge files for this
task, but players can just be supplied with the included copy of *badger*
and the *flag.txt.example* file (if you want to supply that as an aid too). 
The hard variant is stripped with no example flag, I intended for the 
challenge to be run using the *badger.zip* archive, which just includes an 
un-stripped copy and an example flag file (I omitted source, because reversing
is part of this challenge really). If you're short of toughies, switch to the 
stripped version if you like :)

## Difficulty

This challenge is easy, it's just a case of reversing the program, spotting the 
issue, understanding that the stack frame is still there and working out where 
to point to get the flag printed.

See the above section for options to increase difficulty. 

## Solution

A solution is included in *solution.py*. See *writeup.md* for more info.

