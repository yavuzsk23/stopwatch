import wmi

# Düzgün namespace kullanımı (kaçış hatasını önlemek için r"" kullandık)

w = wmi.WMI(namespace=r"root\OpenHardwareMonitor")

for sensor in w.Sensor():
    print(sensor.Name, sensor.SensorType, sensor.Value)
