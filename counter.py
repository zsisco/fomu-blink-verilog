import pyrtl

# Use counter logic to divide system clock.
# The clock is 48 MHz, so we divide it down by 2^28.

counter_o = pyrtl.Output(bitwidth=58, name='counter_o')
counter = pyrtl.Register(bitwidth=58, name='counter')

counter.next <<= counter + 1
counter_o <<= counter


##=========================================================================##
import sys
pyrtl.importexport.output_to_verilog(dest_file=sys.stdout, add_reset=False)