import board
import busio
import time
import digitalio
#TX, RX
uart = busio.UART(board.SCK, board.MOSI, baudrate=9600)

while True:
		if uart.in_waiting: # check if there's anything in uart buffer
			data = uart.read(32) # read at most 32 bytes

			# data is a bytearray, we'll want to convert it to a string
			data_string = ''.join([chr(b) for b in data])
			print(data_string)
		time.sleep(0.1)
