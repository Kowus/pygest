import serial
import time
import pyautogui

ArduinoSerial = serial.Serial('/dev/cu.usbmodemFA131', 9600)
time.sleep(2)

while 1:
    incoming = str(ArduinoSerial.readline())
    print incoming

    if'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)
    if 'Rewind' in incoming:
        pyautogui.hotkey('option', 'command', 'left')
    if 'Forward' in incoming:
        pyautogui.hotkey('option', 'command', 'right')
    if'Vup' in incoming:
        pyautogui.hotkey('option', 'command', 'up')
    if'Vdown' in incoming:
        pyautogui.hotkey('option', 'command', 'down')
        incoming = ""
