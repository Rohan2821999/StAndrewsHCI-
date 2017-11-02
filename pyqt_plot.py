from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
import serial

app = QtGui.QApplication([])

p = pg.plot()
p.setWindowTitle('Accelerometer and Gyro Plot')
curve = p.plot()

data = []
defserial=serial.Serial('COM3', 115200)


def update():
    global curve, data
    line = defserial.readline()
    gyro_x, gyro_y, gyro_z = line.split()
    data.append(gyro_x)
    xdata = np.array(data, dtype='float64')
    curve.setData(xdata)
    app.processEvents()
    if len(data) > 200:
        del data[:100]   


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
