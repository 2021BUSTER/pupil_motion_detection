import serial 
import numpy as np 

import matplotlib.pyplot as plt
import seaborn as sns

PORT_H = '/dev/ttyUSB1' 
PORT_B = '/dev/ttyUSB0' 

BaudRate = 9600 

ARD_H = serial.Serial(PORT_H,BaudRate) 
ARD_B = serial.Serial(PORT_B,BaudRate) 

cnt = 0

data_9 = list(range(0,16))
splitData = list(range(0,16))

#Arduino for heap
def Ardread_H(cnt): # return list [Ard1,Ard2] 
    global splitData
    if ARD_H.readable(): 
        LINE = ARD_H.readline()
        data = LINE.decode('utf-8')
        data = data.strip('\n')
        data = data.strip('\r')
        splitData = data.split(',')

        for i in range(0,16) :
            splitData[i] = int(splitData[i])

        splitData = np.reshape(splitData,(4,4))
        splitData = np.flip(splitData)
    else :
        print("읽기 실패 from _Ardread_") 
        
#Arduino for back
def Ardread_B(cnt): # return list [Ard1,Ard2] 
    global data_9
    if ARD_B.readable(): 
        LINE = ARD_B.readline()
        data = LINE.decode('utf-8')
        data = data.strip('\n')
        data = data.strip('\r')
        Data9 = data.split(',')
        for i in range(0,9) :
            Data9[i] = int(Data9[i])

        j = 0
        for i in range(0,16) :
            if i % 4 == 3 or i > 11:
                data_9[i] = 0
            else :
                data_9[i] = Data9[j]
                j = j+1

        data_9 = np.reshape(data_9,(4,4))

    else : 
        print("읽기 실패 from _Ardread_")


        

def merger_heatmap() :
    global splitData
    global data_9
    
    heatmapArr = np.concatenate((data_9, splitData), axis=0)
    print(heatmapArr)

    ax = sns.heatmap(heatmapArr, cmap='Greys', cbar=False , vmin = 0, vmax = 1024)
    ax.tick_params(left=False, bottom=False)
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
     
    fname = 'correct' + str(cnt) +'.png'
    plt.savefig("/home/pi/shareSamba/correctPosition/"+fname, dpi=200)
        
    data_9 = np.reshape(data_9,(16,1))
    splitData = np.reshape(splitData,(16,1))
    
while (True): 
    Ardread_H(cnt)
    Ardread_B(cnt)
    merger_heatmap()
    cnt += 1

