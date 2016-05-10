#!/usr/bin
# -*- coding: utf-8 -*-
import os
import shutil
import pyautogui
import time
def moveHandHistory():
	directory=[x[:-1] for x in os.popen('ls ~/.wine/drive_c/Program\ Files\ \(x86\)/Full\ Tilt\ Poker/HandHistory/7_ee_Zy').readlines()]
	[shutil.move('/home/tak/.wine/drive_c/Program Files (x86)/Full Tilt Poker/HandHistory/7_ee_Zy/'+x,'/home/tak/.wine/drive_c/Program Files (x86)/Full Tilt Poker/HandHistory/reserv') for x in directory]
def registration():
	pyautogui.click(x=860,y=580)
	reg = pyautogui.locateOnScreen('regLobbyBlack.png')
	if reg:regx, regy = pyautogui.center(reg)
	else:
		reg = pyautogui.locateOnScreen('regLobbyWhite.png')
		regx, regy = pyautogui.center(reg)
	pyautogui.moveTo(regx, regy)
	pyautogui.doubleClick()
	time.sleep(1)
	registerNow = pyautogui.locateOnScreen('registerNow.png')
	while not registerNow:
		closeRegion = pyautogui.locateOnScreen('closeFullTilt.png')
		pyautogui.click(x=closeRegion[0]+5,y=closeRegion[1]+10)
		registerNow = pyautogui.locateOnScreen('registerNow.png')
	registerNowx, registerNowy = pyautogui.center(registerNow)
	pyautogui.moveTo(registerNowx, registerNowy)
	pyautogui.click()
	time.sleep(1)
	byin = pyautogui.locateOnScreen('300chips.png')
	byinx, byiny = pyautogui.center(byin)
	pyautogui.moveTo(byinx, byiny-37)
	pyautogui.click()
	time.sleep(3)
def wait():
	waitt = 0
	while not waitt:
		waitt=pyautogui.locateOnScreen('closeWindowAct.png')
		time.sleep(3)
def moveTo():
	move = pyautogui.locateOnScreen('options.png')
	buttonx= move[0]+move[2]-5
	buttony = move[1]-10
	pyautogui.moveTo(buttonx, buttony)
	pyautogui.dragTo(x=1351, y=53,duration=2)
def waitWhenReg():
	waitWhenReg = 0
	while waitWhenReg:
		waitWhenReg = pyautogui.locateOnScreen('tournWillStart.png')
		time.sleep(5)

def closeWindow():	
	time.sleep(2)
	closeRegion = pyautogui.locateOnScreen('rematch.png')
	if closeRegion:pyautogui.doubleClick(x=closeRegion[0]+10,y=closeRegion[1]+10)
	else:
		closeRegion = pyautogui.locateOnScreen('yesNo.png')
		if closeRegion:pyautogui.click(x=closeRegion[0]+100,y=closeRegion[1]+10)
closeWindow()

# 	else:
# 		closeRegion = pyautogui.locateOnScreen('closeWindow.png')
# 		pyautogui.click(x=closeRegion[0]+5,y=closeRegion[1]+10)
	
# 	time.sleep(1)
# 	closeRegion = pyautogui.locateOnScreen('closeFullTilt.png')
# 	pyautogui.click(x=closeRegion[0]+5,y=closeRegion[1]+10)




	









