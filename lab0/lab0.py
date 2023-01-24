import pyb

print ("Hello, Milky Way")                  # A comment
print ("The answer is {:d}".format (42))
for count in range (12):
    print (count)          # Must get indentation right


pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)
pinC0.high()
pinC0.low()
