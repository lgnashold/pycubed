import board
import busio
import time
import digitalio
import json

uart = busio.UART(board.PB16, board.PB17, baudrate=9600)

testdata = {"hello":"Moritz","How":"AreYouDoing"}

def sendMessage(raw):
    payload = json.dumps(raw) + "\n"
    b= bytearray()
    b.extend(payload)
    numBytes = uart.write(b)
    #print("Wrote message to Pi (" + str(numBytes) + "): " + payload)

def handleMessage(msg):
    print(msg.decode('utf-8'))

count = 0

while True:
    # checks if bytes in UART buffer
    if uart.in_waiting:
        # Reads line of data as bytes
        data = uart.readline()
        if data is not None:
            handleMessage(data)

    count += 1
    if count % 10 == 0:
        sendMessage(testdata)

    time.sleep(0.1)