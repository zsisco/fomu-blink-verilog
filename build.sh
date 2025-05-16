#!/bin/bash
set -e
uv run blink.py
uv run yowasp-yosys -DPVT blink.v -p synth_ice40 -o blink.json
uv run yowasp-nextpnr-ice40 --up5k --package uwg30 --pcf fomu-pvt.pcf --json blink.json --asc blink.asc
uv run yowasp-icepack blink.asc blink.bit
openFPGALoader --Version || \
  (printf '\nerror: openFPGALoader not found, please install it\n\n' && exit 1)
openFPGALoader -b fomu blink.bit --verify || \
  (printf '\nerror: failed to upload, replug the USB, wait for it to register, and try again\nif on linux: https://workshop.fomu.im/en/latest/requirements/drivers.html\n\n' && exit 1)