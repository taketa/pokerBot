#!/usr/bin
# -*- coding: utf-8 -*-
import time
from imp import reload

import pyperclip
def action():
	import forMainAllDef
	reload(forMainAllDef)
	diapazonx=[]
	indicator=forMainAllDef.lastHand()[0].split(' ')
	indicator=indicator[-1]
	
	diapazonx=forMainAllDef.diapazonPreFlop()
	diapazon1=diapazon2=diapazon3=diapazonx
	while 'finishes in' not in forMainAllDef.lastHand()[-1] and 'stands up' not in forMainAllDef.lastHand()[-1]:
		while forMainAllDef.rounddd()==0 and forMainAllDef.lastHand()[0].split(' ')[-1]==indicator:


			
			reload(forMainAllDef)
			
			if forMainAllDef.didI():
				diapazonx=forMainAllDef.diapazonPreFlop()
				if forMainAllDef.position()=='oop':
					if forMainAllDef.lineIP:
						try:
							eval(forMainAllDef.lineIP)
						except NameError:
							if forMainAllDef.lineIP and forMainAllDef.lineIP[-1]=='c':
								if forMainAllDef.evaluatePreFlop(diapazonx)>=0.5:forMainAllDef.bettx()
								else:forMainAllDef.checkkx()
							elif forMainAllDef.lineIP and forMainAllDef.lineIP[-1]=='r':

								if forMainAllDef.evaluatePreFlop(diapazonx)>=0.75:

									if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
									else:forMainAllDef.bettx()

								elif forMainAllDef.evaluatePreFlop(diapazonx)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
								else:forMainAllDef.foldsx()
						else:
							diapazonx=forMainAllDef.diapazonPercent(diapazonx,eval(forMainAllDef.lineIP))
							if forMainAllDef.lineIP and forMainAllDef.lineIP[-1]=='c':
								if forMainAllDef.evaluatePreFlop(diapazonx)>=0.5:forMainAllDef.bettx()
								else:forMainAllDef.checkkx()
							elif forMainAllDef.lineIP and forMainAllDef.lineIP[-1]=='r':
								if forMainAllDef.evaluatePreFlop(diapazonx)>=0.75:
									if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
									else:forMainAllDef.bettx()
								elif forMainAllDef.evaluatePreFlop(diapazonx)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
								else:forMainAllDef.foldsx()

				
				if forMainAllDef.position()=='ip':
					if not forMainAllDef.lineIP:
						if forMainAllDef.evaluatePreFlop(diapazonx)>=0.5:forMainAllDef.bettx()
						else:forMainAllDef.calllx()
					else:
						try:eval(forMainAllDef.lineIP)
						except NameError:
							if forMainAllDef.lineIP and forMainAllDef.lineIP[-1]=='r':
								if forMainAllDef.evaluatePreFlop(diapazonx)>=0.75:
									if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
									else:forMainAllDef.pushhx()
								elif forMainAllDef.evaluatePreFlop(diapazonx)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
								else:forMainAllDef.foldsx()
						else:
							diapazonx=forMainAllDef.diapazonPercent(diapazonx,eval(forMainAllDef.lineIP))
							if forMainAllDef.lineIP and forMainAllDef.lineIP[-1]=='r':
								if forMainAllDef.evaluatePreFlop(forMainAllDef.diapazonPercent(diapazonx,eval(forMainAllDef.lineIP)))>=0.75:
									if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
									else:forMainAllDef.pushhx()
								elif forMainAllDef.evaluatePreFlop(forMainAllDef.diapazonPercent(diapazonx,eval(forMainAllDef.lineIP)))>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
								else:forMainAllDef.foldsx()
			reload(forMainAllDef)
		while forMainAllDef.rounddd()==1 and forMainAllDef.lastHand()[0].split(' ')[-1]==indicator:
			
			reload(forMainAllDef)
			
			if forMainAllDef.didI():

				diapazon1=forMainAllDef.diapazonMinus(diapazonx)

				if forMainAllDef.lineIP:
					try:eval(forMainAllDef.lineIP)
					except NameError:
						if forMainAllDef.lineIP[-1]!='r' and forMainAllDef.lineIP[-1]!='b':
							if forMainAllDef.evaluatePostFlop(diapazon1)>=0.5:forMainAllDef.bettx()
							else:forMainAllDef.checkkx()
						
						else:
							if forMainAllDef.evaluatePostFlop(diapazon1)>=0.75:
								if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
								else:forMainAllDef.pushhx()
								

							elif forMainAllDef.evaluatePostFlop(diapazon1)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
							else:forMainAllDef.foldsx()
					else:
						diapazon1=forMainAllDef.diapazonPercent(diapazon1,eval(forMainAllDef.lineIP))
						if forMainAllDef.lineIP[-1]!='r' and forMainAllDef.lineIP[-1]!='b':
							if forMainAllDef.evaluatePostFlop(diapazon1)>=0.5:forMainAllDef.bettx()
							else:forMainAllDef.checkkx()
						
						else:
							if forMainAllDef.evaluatePostFlop(diapazon1)>=0.75:
								if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
								else:forMainAllDef.pushhx()
							elif forMainAllDef.evaluatePostFlop(diapazon1)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
							else:forMainAllDef.foldsx()
			reload(forMainAllDef)
		while forMainAllDef.rounddd()==2 and forMainAllDef.lastHand()[0].split(' ')[-1]==indicator:
			
			reload(forMainAllDef)
			
			if forMainAllDef.didI():
				diapazon2=forMainAllDef.diapazonMinus(diapazon1)
				if forMainAllDef.lineIP:
					try:eval(forMainAllDef.lineIP)
					except NameError:
						if forMainAllDef.lineIP[-1]!='r' and forMainAllDef.lineIP[-1]!='b':
							if forMainAllDef.evaluatePostFlop(diapazon2)>=0.5:forMainAllDef.bettx()
							else:forMainAllDef.checkkx()
						
						else:
							if forMainAllDef.evaluatePostFlop(diapazon2)>=0.75:
								if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
								else:forMainAllDef.pushhx()
							elif forMainAllDef.evaluatePostFlop(diapazon2)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
							else:forMainAllDef.foldsx()
					else:
						diapazon2=forMainAllDef.diapazonPercent(diapazon2,eval(forMainAllDef.lineIP))
						if forMainAllDef.lineIP[-1]!='r' and forMainAllDef.lineIP[-1]!='b':
							if forMainAllDef.evaluatePostFlop(diapazon2)>=0.5:forMainAllDef.bettx()
							else:forMainAllDef.checkkx()
						
						else:
							if forMainAllDef.evaluatePostFlop(diapazon2)>=0.75:
								if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
								else:forMainAllDef.pushhx()
							elif forMainAllDef.evaluatePostFlop(diapazon2)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
							else:forMainAllDef.foldsx()
			reload(forMainAllDef)
		while forMainAllDef.rounddd()==3 and forMainAllDef.lastHand()[0].split(' ')[-1]==indicator and 'finishes in' not in forMainAllDef.lastHand()[-1] and 'stands up' not in forMainAllDef.lastHand()[-1]:
			reload(forMainAllDef)
			
			if forMainAllDef.didI():
				diapazon3=forMainAllDef.diapazonMinus(diapazon2)
				if forMainAllDef.lineIP:
					try:eval(forMainAllDef.lineIP)
					except NameError:

						if forMainAllDef.lineIP[-1]!='r' and forMainAllDef.lineIP[-1]!='b':
							if forMainAllDef.evaluatePostFlop(diapazon3)>=0.5:forMainAllDef.bettx()
							else:forMainAllDef.checkkx()
						
						else:
							if forMainAllDef.evaluatePostFlop(diapazon3)>=0.75:
								if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
								else:forMainAllDef.pushhx()
							elif forMainAllDef.evaluatePostFlop(diapazon3)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
							else:forMainAllDef.foldsx()
					else:
						diapazon3=forMainAllDef.diapazonPercent(diapazon3,eval(forMainAllDef.lineIP))
						if forMainAllDef.lineIP[-1]!='r' and forMainAllDef.lineIP[-1]!='b':
							if forMainAllDef.evaluatePostFlop(diapazon3)>=0.5:forMainAllDef.bettx()
							else:forMainAllDef.checkkx()
						
						else:
							if forMainAllDef.evaluatePostFlop(diapazon3)>=0.75:
								if forMainAllDef.stack<=float(forMainAllDef.toCallx):forMainAllDef.calllx()
								forMainAllDef.pushhx()
							elif forMainAllDef.evaluatePostFlop(diapazon3)>=float(forMainAllDef.toCallx)/(forMainAllDef.potx+float(forMainAllDef.toCallx)):forMainAllDef.calllx()
							else:forMainAllDef.foldsx()
			reload(forMainAllDef)
		
while True:
	from newTourney import moveHandHistory,registration,wait,waitWhenReg,moveTo,closeWindow
	moveHandHistory()
	registration()
	wait()
	moveTo()
	waitWhenReg()

	while True:
		action()
		closeWindow()
		time.sleep(1)
		pyautogui.click(x=479, y=34)
		time.sleep(1)

		break


# while True:
# 	action()
	