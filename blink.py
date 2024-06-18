import pyrtl

# Use counter logic to divide system clock.
# The clock is 48 MHz, so we divide it down by 2^28.

bitwidth = 29  # Change this!
counter_o = pyrtl.Output(bitwidth=bitwidth, name='counter_o')
counter = pyrtl.Register(bitwidth=bitwidth, name='counter')

counter.next <<= counter + 1  # Change this!
counter_o <<= counter


##=========================================================================##
## Do not change the code below this header!
## Export this PyRTL code to Verilog, then combine it with the Verilog
## harness code in `fomu.v`, creating new file `blink.v`.
##=========================================================================##
with open('blink.v', 'w') as blink:
    with open("fomu.v", 'r') as harness:
        blink.write(harness.read())
    pyrtl.importexport.output_to_verilog(dest_file=blink, add_reset=False)
