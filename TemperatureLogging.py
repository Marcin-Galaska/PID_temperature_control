import numpy as np
import time
import json
import csv
import keyboard
import matplotlib.pyplot as plt
import serial.tools.list_ports


def dataPlot(temperature, time):
    temperature = np.array(temperature)
    time = np.array(time)
    error = np.subtract(25, temperature)

    plt.clf()
    plt.subplot(2, 1, 1)
    plt.title("Temperatura")
    plt.grid()
    plt.plot(time, temperature)
    plt.subplot(2, 1, 2)
    plt.title("Uchyb regulacji")
    plt.grid()
    plt.plot(time, error)
    plt.show()
    plt.pause(0.001)


#check which port is in use:
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

hSerial = serial.Serial('COM5', 115200, timeout=1, parity=serial.PARITY_NONE)
time.sleep(2)

time_str = time.strftime("%Y%m%d-%H%M%S")
hFile = open("PIDLogging%s.csv" % time_str, "a", newline='')

writer = csv.DictWriter(hFile, fieldnames=["temperature"])
writer.writeheader()

hSerial.reset_input_buffer()
hSerial.flush()
temperature_samples = []
t = []
t_value = 0

plt.ion()
plt.figure(figsize=(14, 8))
while True:
    text = hSerial.readline()
    temperature = 0

    try:
        sample = json.loads(text)
        temperature = sample["temperature"]
    except ValueError:
        print("Bad JSON")
        print("%s\r\n" % {text})
        hSerial.flush()
        hSerial.reset_input_buffer()

    hFile.write("%.2f," % temperature)
    temperature_samples.append(temperature)
    t.append(t_value)
    t_value += 1

    dataPlot(temperature_samples, t)
    if keyboard.is_pressed("q"):
        break

hSerial.close()
hFile.close()
