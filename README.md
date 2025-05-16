# Blink on FOMU using YoWASP vscode plugin

0. Install the YoWASP Toolchain vscode plugin.
1. Insert FOMU into USB port.
2. In vscode, run command `YoWASP Toolchain: Build...` (`cmd`+`shift`+`p`)
3. ...
4. FOMU's LED should cycle between different colors.
5. Try modifying the logic for the counter in `blink.py` to see the LED change at different rates.
  (If you make any changes, unplug the FOMU and plug it back in before running `YoWASP Toolchain: Build` again.)

# Blink on FOMU using CLI

0. Install [uv](https://docs.astral.sh/uv/).
1. If on Linux, add [udev rules](https://docs.astral.sh/uv/) for Fomu.
2. Insert FOMU into USB port.
3. Run `./build.sh`.
  (It may take a while the first time, but it should be fast and network-free on subsequent runs.)
4. FOMU's LED should cycle between different colors.
5. Try modifying the logic for the counter in `blink.py` to see the LED change at different rates.
  (If you make any changes, unplug the FOMU and plug it back in before running `./build.sh` again.)