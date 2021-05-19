import serial 
import numpy as np 

import matplotlib.pyplot as plt
import seaborn as sns

PORT = 'COM4' 
BaudRate = 9600 

ARD = serial.Serial(PORT,BaudRate) 

array=[]
buf=[]

cnt = 0

def Ardread(cnt): # return list [Ard1,Ard2] 

    if ARD.readable(): 
        LINE = ARD.readline()
        data = LINE.decode('utf-8')
        data = data.strip('\n')
        data = data.strip('\r')
        splitData = data.split(',')

        for i in range(0,16) :
            splitData[i] = int(splitData[i])

        splitData = np.reshape(splitData,(4,4))

        ax = sns.heatmap(splitData, cmap='Blues', cbar=False , vmin = 0, vmax = 1000)
        ax.tick_params(left=False, bottom=False)
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
     
        fname = 'savefig16_200dpi' + str(cnt) +'.png'
        plt.savefig(fname, dpi=200)
        
    else : 
        print("읽기 실패 from _Ardread_") 
        
while (True): 
    Ardread(cnt)
    cnt += 1