import serial.tools.list_ports
import socket,os


#   Open the file to log the operands and the operation 



# Create a blank instance of serial port
#this will list all ports in use rn 

ports = serial.tools.list_ports.comports()

# Create a blank instance of serial object 

serialInst = serial.Serial()
portList = []







for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))


# To choose a port 3shan nsam3 

val  = input("select Port: COM")




#   Looping through ports

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
#   printed the chosen port 
        print(portList[x])



#Bn-set rl baud rate 3ala 7asb el arduino
#   At what rate we sample data 

serialInst.baudrate = 9600

#   Adjusting the port 

serialInst.port = portVar

# to open that port and listen for any incoming data 

serialInst.open()

 
while True:

    #   Lw fee data fel buffer hn-read-ha
    if serialInst.in_waiting:
        file = open('Screen.txt','w')

        #read incoming bytes from serial device
        packet = serialInst.readline()
        print(packet.decode('utf'))
        file.write(packet.decode('utf'))
        print("Teslm eidak ya jumboo\n teslm eidaaaak")
        
        file.close()
        

file.close





        
