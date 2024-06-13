#!/bin/sh

python3.11 counter.py | tee blink.v
cat fomu.v >> blink.v