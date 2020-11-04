import wmi

w = wmi.WMI()
print(w.Win32_TemperatureProbe())

# Low Power: powercfg /S 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635d
# High Power: powercfg /S 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
