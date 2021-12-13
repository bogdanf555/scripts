#!/usr/bin/python3
from gpiozero import CPUTemperature

if __name__ == '__main__':
    cpu = CPUTemperature()
    print("{0:.2f}°C".format(cpu.temperature))
