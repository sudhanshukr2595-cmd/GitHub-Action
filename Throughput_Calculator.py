import math
#import math to import math function

input1 = input("Enter the NR channel Bandwidth(MHz):")
input2 = input("Enter the SCS(KHz):")
MIMOLayers = input("Enter the number of MIMO layers(1 to 4):")
#MCSIndex = input("Enter the MCS Index (0-27):")
Choice = input("choose input 0 for CQI and 1 for MCS:")
Index = input("Enter the corresponding CQI(0-15) or MCS index(0-27)")
BLERTarget = input("Enter the BLER(%)")

x=int(input1)*1000/int(input2)/12
NumPRB = x-4
NumPRB = math.floor(NumPRB)
DL_Slots =1600 
print("Avaiable number of PRB is : " +str(NumPRB))

spectralefficiencyMCS = [0.2344, 0.3066, 0.3770, 0.4902, 0.6016, 0.7402, 0.8770, 1.0273, 1.1758, 1.3262, 1.3281, 1.4766, 1.6953, 1.9141, 2.1602, 2.4063, 2.5703, 2.5664, 2.7305, 3.0293, 3.3223, 3.6094, 3.9023, 4.2129, 4.5234, 4.8164, 5.1152, 5.3320, 5.5547]
spectralefficiencyCQI = [0, -6.7, -4.7, -2.3, 0.2, 2.4, 4.3, 5.9, 8.1, 10.3, 11.7, 14.1, 16.3, 18.7, 21.0, 22.7]
if int(Choice) == 0:
    
    y = spectralefficiencyCQI[int(Index)]
elif int(Choice) ==1:
    
    y = spectralefficiencyMCS[int(Index)]

#y = spectralefficiencyMCS[int(MCSIndex)]
print("The MCS Spectral Efficiency is " + str(y))
TBSize = 132 * y
TBSize = math.floor(TBSize)
Throughput = int(TBSize) * int(NumPRB) * int(DL_Slots) * int(MIMOLayers) * ((100-int(BLERTarget))/100)/1000/1000
print("Maximum Throughput for this configuration is :"+str(Throughput) +" Mbps")

##We will use mcs /scs/mimo/bandwidth/to calculate throughput.
##we will incooprate MCS table using list

##later we have in cooperated CQI to check the better/efficient throughput
