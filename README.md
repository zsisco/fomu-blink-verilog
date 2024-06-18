# Blink on FOMU using YoWASP vscode plugin

0. Install the YoWASP Toolchain vscode plugin.
1. Insert FOMU into USB port.
2. In vscode, run command `YoWASP Toolchain: Build...` (`cmd`+`shift`+`p`)
3. ...
4. FOMU's LED should cycle between different colors.
5. Try modifying the logic for the counter in `blink.py` to see the LED change at different rates.
  (If you make any changes, unplug the FOMU and plug it back in before running `YoWASP Toolchain: Build` again.)