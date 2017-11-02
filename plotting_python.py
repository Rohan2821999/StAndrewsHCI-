import random
import matplotlib.pyplot as plt
import serial
arr, arr_y, arr_z, arr_gyro_x, arr_gyro_y, arr_gyro_z = [], [], [], [], [], []
t = []
i = 0
plt.ion()
#plt.ylim(0,5)

defserial = serial.Serial('com3',115200)
#f, axarr = plt.subplots(2,sharex = True)

while True:
    #plt.ylim(-1000,1000)
    val = defserial.readline()
    accel_x, accel_y, accel_z = val.split()
    
    arr.append(accel_x)
    arr_y.append(accel_y)
    arr_z.append(accel_z)

    #arr_gyro_x.append(gyro_x)
    #arr_gyro_y.append(gyro_y)
    #arr_gyro_z.append(gyro_z)

    
    i = i+1
    t.append(i)
    if len(arr) > 10:
        #print i
        plt.plot(t,arr,t,arr_y,t,arr_z)
        #axarr[1].plot(t,arr_gyro_x,t,arr_gyro_y,t,arr_gyro_z)
        if i%55 == 0:
            plt.cla()
            arr, arr_y, arr_z, t = [], [], [], []
        plt.pause(0.05)


