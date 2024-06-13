# Blink on FOMU using YoWASP vscode plugin

0. Install the YoWASP Toolchain vscode plugin.
1. Insert FOMU into USB port.
2. Run `./load-pyrtl.sh` to output PyRTL to Verilog and combine it with `fomu.v`.
3. In vscode, run command `YoWASP Toolchain: Build...`
4. ...
5. FOMU's LED should cycle between different colors. Try modifying the logic for the counter in `counter.py` to see the LED change at different rates.