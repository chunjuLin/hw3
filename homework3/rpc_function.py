import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

# s.write(bytes("\r", 'UTF-8'))
# line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
# print(line)
# line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
# print(line)
# time.sleep(1)

# s.write(bytes("/Gesture_ui/run 0 \r", 'UTF-8'))
# line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
# print(line)
# line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
# print(line)
# time.sleep(1)
while True:
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    if line == "confirmed!":
        s.write(bytes("/Gesture_ui/run 0 \r", 'UTF-8'))


s.close()