import fcntl
import termios
import struct
   
th, tw, hp, wp = struct.unpack('HHHH',
fcntl.ioctl(0, termios.TIOCGWINSZ,
struct.pack('HHHH', 0, 0, 0, 0)))
tw, th

print(f'Number of columns and Rows: {tw, th}')