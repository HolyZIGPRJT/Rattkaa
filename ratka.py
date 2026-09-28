import time
import os
import sys

A = int(input("скока ты хочешь голдi:"))
B = int(input("айди твой да:"))
print("голда будет через")

otchet_ara = 5
fps_ara = 1
while otchet_ara >= 0:
    print(f"{otchet_ara} сек")
    otchet_ara -= fps_ara
    time.sleep(fps_ara)
print("Пизда тобi, ты попался на рат")
For i in range(1,100):
	time.sleep(0.04)
	print("Файл спизжен")
