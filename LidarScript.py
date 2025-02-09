import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 115200)

def GetData():
	while True:
		time.sleep(0.01)
		count = ser.in_waiting
		if count > 8:
			recv = ser.read(9)
			ser.reset_input_buffer()
			if recv[0] == 0x59 and recv[1] == 0x59:
				distance = recv[2] + recv[3] * 256
				strength = recv[4] + recv[5] * 256
				print('(distance = ', distance, ' cm, strength = ', strength, ')')
				ser.reset_input_buffer()
if __name__ == '__main__':
	try:
		if ser.is_open == False:
			ser.open()
		GetData()
	except KeyboardInterrupt:
		if ser != None:
			ser.close()
