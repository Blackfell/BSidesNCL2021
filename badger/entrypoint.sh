#!/bin/bash
socat tcp-listen:1337,fork,reuseaddr exec:'/badger/badger'
