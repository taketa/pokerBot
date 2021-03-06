#!/usr/bin
# -*- coding: utf-8 -*-
import pyperclip
import pyautogui
import time
import os
import io

text=pyperclip.paste()
text=text.split('\n')
def rounddd():			
	doska=bord()
	doska=doska.bord()
	if len(doska)==0:return 0
	if len(doska)==3:return 1
	if len(doska)==4:return 2
	if len(doska)==5:return 3 
def lastHand(x=text):
	lastHand=[]
	for line in text:
		if '#' in line:
			lastHand.append(text.index(line))
	if len(lastHand)>=1:
		lastHand=text[max(lastHand):]			#определение последней руки
		[lastHand.remove(ss) for ss in lastHand if 'left to act' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'System' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'Tournament Director' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'has timed out' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'has reconnected' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'has been disconnected' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'has returned' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'requested TIME' in ss]
		[lastHand.remove(ss) for ss in lastHand if 'is feeling' in ss]


	# if not lastHand[-1]:lastHand.pop()
	return lastHand

class myCards:					#преобразование в числа
	def myCards(self):
		if len(lastHand())>3:
			for line in lastHand():
				if 'You have been dealt' in line:
					myCardsText=line.split(' ')
			myCardsText=myCardsText[-2:]
			myCard1=myCardsText[0].replace('[','')
			myCard2=myCardsText[1].replace(']','')
			myCards=[myCard1,myCard2]
			return myCards
	def myCardsDig(self):	
		if len(lastHand())>3:
			myCardsDig=myCards()
			myCardsDig=myCardsDig.myCards()
			myCardsDig=[z.replace('c','') for z in myCardsDig]
			myCardsDig=[z.replace('d','') for z in myCardsDig]
			myCardsDig=[z.replace('s','') for z in myCardsDig]
			myCardsDig=[z.replace('h','') for z in myCardsDig]
			myCardsDig=[z.replace('A','14') for z in myCardsDig]
			myCardsDig=[z.replace('K','13') for z in myCardsDig]
			myCardsDig=[z.replace('Q','12') for z in myCardsDig]
			myCardsDig=[z.replace('J','11') for z in myCardsDig]
			myCardsDig=[z.replace('T','10') for z in myCardsDig]
			myCardsDig=[int(x) for x in myCardsDig]
			return sorted(myCardsDig,reverse=True)
	def myCardsMast(self): #мои масти
		if len(lastHand())>3:
			myCardsMast=myCards()
			myCardsMast=myCardsMast.myCards()
			myCardsMast=[list(x) for x in myCardsMast]
			myCardsMast=[y for x,y in myCardsMast]
			return myCardsMast					#определение моих карманных карт
myCardss=myCards()
myCardss=myCardss.myCards()



####################################################################

def hisCardsDig(cardsFromDiapazon):	
	cardsFromDiapazon=[cardsFromDiapazon[:2],cardsFromDiapazon[2:]]
	cardsFromDiapazon=[z.replace('c','') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('d','') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('s','') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('h','') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('A','14') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('K','13') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('Q','12') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('J','11') for z in cardsFromDiapazon]
	cardsFromDiapazon=[z.replace('T','10') for z in cardsFromDiapazon]
	cardsFromDiapazon=[int(x) for x in cardsFromDiapazon]
	return sorted(cardsFromDiapazon,reverse=True)
def hisCardsMast(cardsFromDiapazon): #мои масти
	cardsFromDiapazon=[cardsFromDiapazon[:2],cardsFromDiapazon[2:]]
	cardsFromDiapazon=[list(x) for x in cardsFromDiapazon]
	cardsFromDiapazon=[y for x,y in cardsFromDiapazon]
	return cardsFromDiapazon

preflopCards=myCards()
preflopCards=preflopCards.myCardsDig()
class bord:
	def bord(self):
		def flopCards():
			for line in lastHand():
				if 'The flop is' in line: #определение карт Флопа
					flopCardsText=line.split(' ')
					flopCardsText=flopCardsText[-3:]
					flopCard1=flopCardsText[0].replace('[','')
					flopCard2=flopCardsText[1]
					flopCard3=flopCardsText[2].replace(']','')
					flopCards=[flopCard1,flopCard2,flopCard3]
					return flopCards
			else:return []
		def turnCard():
			for line in lastHand():
				if 'The turn is' in line: #определение карты Терна
					turnCardsText=line.split(' ')
					turnCardsText=turnCardsText[-1:]
					turnCard=[turnCardsText[0].replace('[','')]
					turnCard=[turnCard[0].replace(']','')]
					return turnCard
			else:return []
		def riverCard():
			for line in lastHand():
				if 'The river is' in line: #определение карты Ривера
					riverCardsText=line.split(' ')
					riverCardsText=riverCardsText[-1:]
					riverCard=[riverCardsText[0].replace('[','')]
					riverCard=[riverCard[0].replace(']','')]
					return riverCard
			else:return []
		return flopCards()+turnCard()+riverCard()
	def bordDig(self):		#преобразование карт борда в цифры
		bordDig=bord()
		bordDig=bordDig.bord()
		bordDig=[z.replace('c','') for z in bordDig]
		bordDig=[z.replace('d','') for z in bordDig]
		bordDig=[z.replace('s','') for z in bordDig]
		bordDig=[z.replace('h','') for z in bordDig]
		bordDig=[z.replace('A','14') for z in bordDig]
		bordDig=[z.replace('K','13') for z in bordDig]
		bordDig=[z.replace('Q','12') for z in bordDig]
		bordDig=[z.replace('J','11') for z in bordDig]
		bordDig=[z.replace('T','10') for z in bordDig]
		bordDig=[int(x) for x in bordDig]
		return sorted(bordDig,reverse=True)
bordx=bord()
bordx=bordx.bord()
# def Mast():
# 	Mastt=bordx
# 	myMastt=myCards()
# 	myMastt=myMastt.myCardsMast()
# 	Mastt=[list(x) for x in Mastt]
# 	Mastt=[y for x,y in Mastt]
	
# 	if Mastt:Mastt=Mastt+myMastt
# 	else:Mastt=myMastt
# 	MastH=[1 for x in Mastt if x=='h']
# 	MastH=len(MastH)
# 	MastS=[1 for x in Mastt if x=='s']
# 	MastS=len(MastS)
# 	MastD=[1 for x in Mastt if x=='d']
# 	MastD=len(MastD)
# 	MastC=[1 for x in Mastt if x=='c']
# 	MastC=len(MastC)
# 	Mast=[MastH,MastS,MastD,MastC]
# 	return 	Mast
def hisMast(his):
	Mastt=bordx
	myMastt=hisCardsMast(his)
	Mastt=[list(x) for x in Mastt]
	Mastt=[y for x,y in Mastt]
	
	if Mastt:Mastt=Mastt+myMastt
	else:Mastt=myMastt
	MastH=[1 for x in Mastt if x=='h']
	MastH=len(MastH)
	MastS=[1 for x in Mastt if x=='s']
	MastS=len(MastS)
	MastD=[1 for x in Mastt if x=='d']
	MastD=len(MastD)
	MastC=[1 for x in Mastt if x=='c']
	MastC=len(MastC)
	Mast=[MastH,MastS,MastD,MastC]
	return 	Mast
def allkardss(his):
		hiss=hisCardsDig(his)
		myMastk=hisMast(his)
		bordK=bord()
		bordK=bordK.bordDig()
		allkards=sorted(hiss+bordK,reverse=True)
		for x in myMastk:
			if x>=5: allkards.append(True)
		return allkards	#виды комбинаций





class allkards:					#комбинации
	def allkards(his):
		his=hisCardsDig(his)
		myMastk=Mast()
		myMastk=myMastk.Mast()
		bordK=bord()
		bordK=bordK.bordDig()
		allkards=sorted(his+bordK,reverse=True)
		for x in myMastk:
			if x>=5: allkards.append(True)
		return allkards	#виды комбинаций	
class highCard(allkards): 			
	def highCard(self):			#старшая карта
		highCard=allkards()
		highCard=highCard.allkards()
		return ['highCard',sorted(highCard,reverse=True)[:2]]			

def pare(his):
	pare=allkardss(his)
	pare14=[1 for x in pare if x==14]
	if sum(pare14)==2:return his
	pare13=[1 for x in pare if x==13]
	if sum(pare13)==2:return his
	pare12=[1 for x in pare if x==12]
	if sum(pare12)==2:return his
	pare11=[1 for x in pare if x==11]
	if sum(pare11)==2:return his
	pare10=[1 for x in pare if x==10]
	if sum(pare10)==2:return his
	pare9=[1 for x in pare if x==9]
	if sum(pare9)==2:return his
	pare8=[1 for x in pare if x==8]
	if sum(pare8)==2:return his
	pare7=[1 for x in pare if x==7]
	if sum(pare7)==2:return his
	pare6=[1 for x in pare if x==6]
	if sum(pare6)==2:return his
	pare5=[1 for x in pare if x==5]
	if sum(pare5)==2:return his
	pare4=[1 for x in pare if x==4]
	if sum(pare4)==2:return his
	pare3=[1 for x in pare if x==3]
	if sum(pare3)==2:return his
	pare2=[1 for x in pare if x==2]
	if sum(pare2)==2:return his
		


def twopare(his):
	twopare=allkardss(his)
	twopareFin=[]
	twopare14=[1 for x in twopare if x==14]
	if sum(twopare14)==2:
		twopareFin.append(14)
	twopare13=[1 for x in twopare if x==13]
	if sum(twopare13)==2:
		twopareFin.append(13)
	twopare12=[1 for x in twopare if x==12]
	if sum(twopare12)==2:
		twopareFin.append(12)
	twopare11=[1 for x in twopare if x==11]
	if sum(twopare11)==2:
		twopareFin.append(11)
	twopare10=[1 for x in twopare if x==10]
	if sum(twopare10)==2:
		twopareFin.append(10)
	twopare9=[1 for x in twopare if x==9]
	if sum(twopare9)==2:
		twopareFin.append(9)
	twopare8=[1 for x in twopare if x==8]
	if sum(twopare8)==2:
		twopareFin.append(8)
	twopare7=[1 for x in twopare if x==7]
	if sum(twopare7)==2:
		twopareFin.append(7)
	twopare6=[1 for x in twopare if x==6]
	if sum(twopare6)==2:
		twopareFin.append(6)
	twopare5=[1 for x in twopare if x==5]
	if sum(twopare5)==2:
		twopareFin.append(5)
	twopare4=[1 for x in twopare if x==4]
	if sum(twopare4)==2:
		twopareFin.append(4)
	twopare3=[1 for x in twopare if x==3]
	if sum(twopare3)==2:
		twopareFin.append(3)
	twopare2=[1 for x in twopare if x==2]
	if sum(twopare2)==2:
		twopareFin.append(2)
	if len(twopareFin)>=2: return his
					
			

def trips(his):
	trips=allkardss(his)
	trips14=[1 for x in trips if x==14]
	if sum(trips14)==3:return his
	trips13=[1 for x in trips if x==13]
	if sum(trips13)==3:return his
	trips12=[1 for x in trips if x==12]
	if sum(trips12)==3:return his
	trips11=[1 for x in trips if x==11]
	if sum(trips11)==3:return his
	trips10=[1 for x in trips if x==10]
	if sum(trips10)==3:return his
	trips9=[1 for x in trips if x==9]
	if sum(trips9)==3:return his
	trips8=[1 for x in trips if x==8]
	if sum(trips8)==3:return his
	trips7=[1 for x in trips if x==7]
	if sum(trips7)==3:return his
	trips6=[1 for x in trips if x==6]
	if sum(trips6)==3:return his
	trips5=[1 for x in trips if x==5]
	if sum(trips5)==3:return his
	trips4=[1 for x in trips if x==4]
	if sum(trips4)==3:return his
	trips3=[1 for x in trips if x==3]
	if sum(trips3)==3:return his
	trips2=[1 for x in trips if x==2]
	if sum(trips2)==3:return his					#трипс

def kare(his):
	kare=allkardss(his)

	kare14=[1 for x in kare if x==14]
	if sum(kare14)==4:return his
	kare13=[1 for x in kare if x==13]
	if sum(kare13)==4:return his
	kare12=[1 for x in kare if x==12]
	if sum(kare12)==4:return his
	kare11=[1 for x in kare if x==11]
	if sum(kare11)==4:return his
	kare10=[1 for x in kare if x==10]
	if sum(kare10)==4:return his
	kare9=[1 for x in kare if x==9]
	if sum(kare9)==4:return his
	kare8=[1 for x in kare if x==8]
	if sum(kare8)==4:return his
	kare7=[1 for x in kare if x==7]
	if sum(kare7)==4:return his
	kare6=[1 for x in kare if x==6]
	if sum(kare6)==4:return his
	kare5=[1 for x in kare if x==5]
	if sum(kare5)==4:return his
	kare4=[1 for x in kare if x==4]
	if sum(kare4)==4:return his
	kare3=[1 for x in kare if x==3]
	if sum(kare3)==4:return his
	kare2=[1 for x in kare if x==2]
	if sum(kare2)==4:return his	

def street(his):
	street=allkardss(his)
	street=set(street)
	street=list(street)	
	street=sorted(street,reverse=True)


	if len(street)==5:
		if street[0]-street[1]==1 and street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1:return his
		if street[-1]==2 and street[-2]==3 and street[-3]==4 and street[-4]==5 and street[0]==14:return his
	if len(street)==6:
		if street[0]-street[1]==1 and street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1:return his
		if street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1 and street[4]-street[5]==1:return his
		if street[-1]==2 and street[-2]==3 and street[-3]==4 and street[-4]==5 and street[0]==14:return his
	if len(street)==7:
		if street[0]-street[1]==1 and street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1:return his
		if street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1 and street[4]-street[5]==1:return his
		if street[2]-street[3]==1 and street[3]-street[4]==1 and street[4]-street[5]==1 and street[5]-street[6]==1:return his
		if street[-1]==2 and street[-2]==3 and street[-3]==4 and street[-4]==5 and street[0]==14:return his
						
def flash(his):			#флэш
	flash=allkardss(his)
	if flash[-1]==True: return his			#флэш
class whatKomb:	
	def whatKomb(self):			#определение комбинации
		highCardx=highCard()
		highCardx=highCardx.highCard()
		parex=pare()
		parex=parex.pare()
		twoparex=twopare()
		twoparex=twoparex.twopare()
		tripsx=trips()
		tripsx=tripsx.trips()
		karex=kare()
		karex=karex.kare()
		streetx=street()
		streetx=streetx.street()
		flashx=flash()
		flashx=flashx.flash()
		if karex:return karex
		if flashx:return flashx
		if streetx:return streetx
		if tripsx:return tripsx
		if twoparex:return twoparex
		if parex:return parex
		if highCardx:return highCardx#определение комбинации			



def diapazon():
	xx=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
	yy=['h','d','s','c']
	koloda=[t+m for t in xx for m in yy]


	if myCardss[0] in koloda:koloda.remove(myCardss[0])
	if myCardss[1] in koloda:koloda.remove(myCardss[1])
	for x in bordx:
		if x in koloda:koloda.remove(x)
	diapazon=[x+koloda[i] for x in koloda for i in range(koloda.index(x)+1,len(koloda))]
	diapazonPare=[x for x in diapazon if x[0]==x[2]]
	diapazonNonPare=[x for x in diapazon if x[0]!=x[2]]
	diapazon=diapazonPare+diapazonNonPare
	return diapazon
def diapazonPokerStove(diapazon):
	diapazonPokerStove=[]
	[diapazonPokerStove.append(x[0]+x[2]) for x in diapazon if x[0]==x[2]]
	[diapazonPokerStove.append(x[0]+x[2]+'o') for x in diapazon if x[1]!=x[3] and x[0]!=x[2]]
	[diapazonPokerStove.append(x[0]+x[2]+'s') for x in diapazon if x[1]==x[3] and x[0]!=x[2]]
	
	diapazonPokerStove=set(diapazonPokerStove)
	diapazonPokerStove=list(diapazonPokerStove)
	diapazonPokerStove=str(','.join(diapazonPokerStove))
	# diapazonPokerStove=sorted(diapazonPokerStove,reverse=True)
	return diapazonPokerStove
	# while diapazon:
	# 	length=diapazon[:140]
	# 	diapazonPokerStovex=str(','.join(length))
	# 	mycardss=str(''.join(myCardss))
	# 	bord=str(''.join(bordx))
	# 	pokerStoveAct(diapazonPokerStovex,mycardss,bord)
	# 	del(diapazon[:140])

	# diapazonPokerStove=','.join(diapazon)
	
	# return diapazonPokerStove
def pokerStoveAct(diapazon,mycards,bord):
	pyperclip.copy(diapazon)
	time.sleep(1)
	pyautogui.doubleClick(x=148,y=149)
	time.sleep(0.5)
	pyautogui.hotkey('ctrl', 'v')
	my=''.join(mycards)
	time.sleep(1)
	pyperclip.copy(my)
	time.sleep(1)
	pyautogui.moveTo(x=150, y=177)
	pyautogui.doubleClick(x=150,y=177)
	
	time.sleep(0.5)
	pyautogui.hotkey('ctrl', 'v')	
	time.sleep(1)
	pyperclip.copy(''.join(bord))
	time.sleep(1)
	pyautogui.moveTo(x=447,y=152)
	pyautogui.rightClick(x=447,y=152)
	time.sleep(1)
	pyautogui.click(x=450, y=270)
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'v')	
	time.sleep(1)
	pyautogui.click(x=486,y=298)
	time.sleep(1)
	pyautogui.click(x=486,y=298)
	time.sleep(1)
	pyautogui.doubleClick(x=335,y=177)
	pyautogui.hotkey('ctrl', 'c')
	equity=pyperclip.paste()
	equity=equity.split('.')
	equity=int(equity[0])
	return equity
def diapazonPostFlop(diapazon):
	diapazonPostFlop=[]
	diapazonDel=[]
	diapazonKare=[kare(x) for x in diapazon]
	diapazonKare=[x for x in diapazonKare if x]
	diapazonDel=[diapazon.remove(x) for x in diapazonKare if x in diapazon]
	diapazonFlash=[flash(x) for x in diapazon]
	diapazonFlash=[x for x in diapazonFlash if x]
	diapazonDel=[diapazon.remove(x) for x in diapazonFlash if x in diapazon]
	diapazonStreet=[street(x) for x in diapazon]
	diapazonStreet=[x for x in diapazonStreet if x]
	diapazonDel=[diapazon.remove(x) for x in diapazonStreet if x in diapazon]
	diapazonTrips=[trips(x) for x in diapazon]
	diapazonTrips=[x for x in diapazonTrips if x]
	diapazonDel=[diapazon.remove(x) for x in diapazonTrips if x in diapazon]
	diapazonTwoPare=[twopare(x) for x in diapazon]
	diapazonTwoPare=[x for x in diapazonTwoPare if x]
	diapazonDel=[diapazon.remove(x) for x in diapazonTwoPare if x in diapazon]
	diapazonPare=[pare(x) for x in diapazon]
	diapazonPare=[x for x in diapazonPare if x]
	diapazonDel=[diapazon.remove(x) for x in diapazonPare if x in diapazon]
	diapazonPostFlop=diapazonKare+diapazonFlash+diapazonStreet+diapazonTrips+diapazonTwoPare+diapazonPare
	return diapazonPostFlop
def testAct(mycards,bord):
	mycards=str(''.join(mycards))
	bord=str(''.join(bord))
	bordx=pyperclip.copy(bord)
	print(pyperclip.paste())
	mycardsx=pyperclip.copy(mycards)
	pyautogui.click(x=195, y=209)
	pyautogui.hotkey('ctrl', 'v')
	
print(pokerStoveAct(diapazonPokerStove(diapazon()),myCardss,bordx))





