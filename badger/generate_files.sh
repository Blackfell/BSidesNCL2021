#!/usr/bin/env bash

echo "WARNING - This script uses 7z, just deal with it."

make badger
mkdir ./badger_public ./badger_public_hard
cp ./badger ./badger_public
cp flag.txt.example ./badger_public/flag.txt
cp badger_stripped ./badger_public_hard/badger

7z a badger.zip ./badger_public/*
7z a badger_hard.zip ./badger_public_hard/*

rm -rf ./badger_public*

make clean

echo "Easy and Hard distributions created.")
