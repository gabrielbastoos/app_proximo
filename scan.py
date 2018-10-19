# Python 2.x    program to Scan and Read a QR code 
from qrtools.qrtools import QR

my_QR = QR(filename = "./qr.png") 
  
# decodes the QR code and returns True if successful 
my_QR.decode() 
  
# prints the data 
print (my_QR.data) 
