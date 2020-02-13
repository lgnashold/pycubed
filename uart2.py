import board
import busio
import time
import digitalio
import json
#TX, RX
uart = busio.UART(board.PB16, board.PB17, baudrate=9600)
#uart = busio.UART(board.TX, board.RX, baudrate=9600)

start = "["
end = "]"
print("Output:")

def handleMessage(msg):
    print(msg)

while True:
    data = 1#'a'uart.read(1)  # read a byte

    if data is not None:  # Data was received

        output = b'hello\r\n'
        print("In waiting: " + str(uart.in_waiting))
        print("Just written: " + str(uart.write(output)))         # Print to serial
        time.sleep(1.0)


    #raw = {"hello":"Moritz","How":"AreYouDoing"}
    #payload = json.dumps(raw) + "\n"
    #print(payload)
    #b = bytearray()
    #b.extend(payload)
    ##print(b)
    #print(uart.write(b))
    #
    #print(uart.in_waiting)

    #if uart.in_waiting: # check if there's anything in uart buffer
    #    data = uart.read(32) # read at most 32 bytes
        # data is a bytearray, we'll want to convert it to a string
    #    data_string = ''.join([chr(b) for b in data])
   #     print(data_string)
        #handleMessage(data_string)
        #raw = {"hello":"Moritz","How":"AreYouDoing"}
        #payload = json.dumps(raw)
        #b = bytearray()
        #b.extend(payload)ello
        #uart.write(b)
        #while (not uart.in_waiting):
        #    pass

    time.sleep(0.1)

