import os
import shutil
import pyautogui
import time
def moveTo():
	pyautogui.click(x=1013,y=67)
	move = pyautogui.locateOnScreen('Table1.png')
	buttonx, buttony = pyautogui.center(move)
	pyautogui.moveTo(buttonx, buttony)
	pyautogui.dragTo(x=1327, y=39,duration=0.3)
def wait():
	pyautogui.click(x=1112,y=50)
	move = pyautogui.locateOnScreen('Table1.png')
	buttonx, buttony = pyautogui.center(move)
	pyautogui.moveTo(buttonx, buttony)
	pyautogui.dragTo(x=1327, y=39,duration=0.3)
wait()
