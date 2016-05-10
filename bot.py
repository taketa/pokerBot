#!/usr/bin
# -*- coding: utf-8 -*-
myChips=1500
myNick='7_ee_Zy'
import pyperclip
import pyautogui
import time
import os
import io
from poker import poker
from poker.utils import pretty_args

# hands=sum([1 for x in text if '#' in x])
####################################################
while True:

	from newTourney import moveHandHistory,registration,wait,waitWhenReg,moveTo,closeWindow
	moveHandHistory()
	registration()
	wait()
	moveTo()
	waitWhenReg()

	while True:
		pyperclip.copy('')
		def chattx():
		pyperclip.copy('')
			pyautogui.click(x=813, y=496)
			time.sleep(0.5)
			pyautogui.hotkey('ctrl', 'a')
			# time.sleep(0.2)
			pyautogui.hotkey('ctrl', 'c')
			# time.sleep(0.2)
			pyautogui.hotkey('ctrl', 'a')
			# time.sleep(0.2)
			pyautogui.hotkey('ctrl', 'c')
			# time.sleep(1)
		def bettx():
			pyautogui.click(x=1317, y=400)
			time.sleep(0.2)
			pyautogui.click(x=1320, y=490)
			time.sleep(3)
		def checkkx():
			pyautogui.click(x=1143, y=492)
			time.sleep(3)
		def calllx():
			pyautogui.click(x=1233, y=491)
			time.sleep(3)
		def pushhx():
			pyautogui.click(x=1342, y=400)
			time.sleep(0.5)
			pyautogui.click(x=1320, y=490)
			time.sleep(3)
		def foldsx():
			pyautogui.click(x=1143, y=492)
			time.sleep(3)

		chattx()


		while len(pyperclip.paste())<20:
			chattx()
		text=pyperclip.paste()
		text=text.split('\n')
		push=[[14,2],[14,3],[14,4],[14,5],[14,6],[14,7],[14,8],[14,9],[14,10],[14,11],[14,12],[14,13],[14,14],[13,8],[13,9],[13,10],[13,11],[13,12],[13,13],[12,9],[12,10],[12,11],[12,12],[11,10],[11,11],[10,10],[9,9],[8,8],[7,7],[6,6],[5,5],[4,4],[3,3],[2,2]]
		raiss=[[14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14],[13, 2], [13, 3], [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13],[12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12],[11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11],[10,10],[10,9],[9,8],[9,9],[8,8],[7,7],[6,6],[5,5],[4,4],[3,3],[2,2]]
		call=[[14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14],[13, 9], [13, 10], [13, 11], [13, 12], [13, 13],[12, 10], [12, 11], [12, 12],[11, 10], [11, 11],[10,9],[10,10],[9,8],[9,9],[8,8],[7,7],[6,6],[5,5],[4,4]]
		powerCall=[[14, 12], [14, 13], [14, 14],[13, 12], [13, 13],[12, 12],[11, 11],[10,10],[9,9],[8,8],[7,7]]
		OOP=[[14, 12], [14, 13], [14, 14],[13, 12], [13, 13],[12, 12],[11, 11],[10,10]]

		forRaise=[['two'],['trips'],['street'],['flash']]
		forCallF=[['pare',0],['pare',1],['pare',2],['pare',3]]
		forCallFpower=[['pare',0],['two'],['trips'],['street'],['flash']]
		allKom=[['pare',0],['pare',1],['pare',2],['pare',3],['two'],['trips'],['street'],['flash']]
		nice=[['pare',0],['two'],['trips'],['street'],['flash'],['kare']]
		veryNice=[['two'],['trips'],['flash'],['street'],['kare']]
		contBetRange=[['pare',0],['two'],['trips'],['street'],['flash'],['pare',1],['pare',2],['pare']]
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
		if len (lastHand())>3:
			for x in lastHand():
				if 'posts' in x:
					if '7_ee_Zy' not in x:
						nic=x[:x.index(' posts')]
						nic=nic[8:]			
						nic2=nic.replace(' ','') #определение ника противника
			if ' ' in nic:
				text=[x.replace(nic,nic2) for x in text]
		if len (lastHand())>3:
			niccx=[x for x in text if 'posts' in x]
			niccx=[x for x in niccx if '7_ee_Zy' not in x]
			niccx=niccx[0]
			niccx=niccx[:niccx.index(' posts')]
			niccx=niccx[8:]
			niccx2=niccx.replace(' ','')
			if ' ' in niccx:
				text=[x.replace(niccx,niccx2) for x in text]
		textForStat='\n'.join(text)
		textForStat=[textForStat.split('Dealer: Hand #')]
		textForStat=[x[y].split('\n') for x in textForStat for y in range(len(x))]
		
	######################################################################
		if len(lastHand())>3:
			if 'finishes in' not in lastHand()[-1] and 'stands up' not in lastHand()[-1]:
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
				class Mast: 					#количество карт одной масти на борде
					def Mast(self):
						Mast=bord()
						Mast=Mast.bord()
						myMast=myCards()
						myMast=myMast.myCardsMast()
						Mast=[list(x) for x in Mast]
						Mast=[y for x,y in Mast]
						if Mast:Mast=Mast+myMast
						else:Mast=myMast
						MastH=[1 for x in Mast if x=='h']
						MastH=len(MastH)
						MastS=[1 for x in Mast if x=='s']
						MastS=len(MastS)
						MastD=[1 for x in Mast if x=='d']
						MastD=len(MastD)
						MastC=[1 for x in Mast if x=='c']
						MastC=len(MastC)
						Mast=[MastH,MastS,MastD,MastC]
						return 	Mast
				class myStackMinus:				#минус от стэка
					def blind(self): #все проставленные блайнды
						blind=[line for line in lastHand() if '7_ee_Zy posts the' in line]
						blind=[x.split(' ') for x in blind]
						
						blind=[x[7] for x in blind]
						blind=[x.replace(',','') for x in blind]
						blind=[int(x) for x in blind]
						return(sum(blind))
					def call(self):	#все мои коллы
						call=[line for line in lastHand() if '7_ee_Zy calls' in line]
						call=[x.split(' ') for x in call]
						call=[x[3] for x in call]
						call=[x.replace(',','') for x in call]
						call=[int(x) for x in call]
						return(sum(call))
					def rais(self):	#все мои рейзы
						rais=[]
						for x in lastHand():
							if '7_ee_Zy raises to' in x:
								if '7_ee_Zy posts the' in lastHand()[lastHand().index(x)-3]:
									rai=x.split(' ')
									rai=rai[4]	
									rai=rai.replace(',','')
									rai=int(rai)
									bli=lastHand()[lastHand().index(x)-3].split(' ')
									bli=bli[-1]
									bli=bli.replace(',','')
									bli=int(bli)
									rai=rai-bli
									rais.append(rai)
								else:
									rai=x.split(' ')
									rai=rai[4]
									rai=rai.replace(',','')
									rai=int(rai)
									rais.append(rai)
						return sum(rais)
					def bet(self):	#все мои беты
						bet=[x for x in lastHand() if '7_ee_Zy bets' in x]
						bet=[x.split(' ') for x in bet]
						bet=[x[3] for x in bet]
						bet=[x.replace(',','') for x in bet]
						bet=[int(x) for x in bet]
						return(sum(bet))
					def myStackMinus(self): #все вклады в пот
						blind=myStackMinus()
						blind=blind.blind()
						call=myStackMinus()
						call=call.call()
						rais=myStackMinus()
						rais=rais.rais()
						bet=myStackMinus()
						bet=bet.bet()
						return blind+call+rais+bet 	

				# def myStackPlus(): 				#плюс к стэку
				# 	myStackPlus=
					# def wins(self): #выигрыш
					# 	wins=[line for line in text if '7_ee_Zy wins the pot' in line]
					# 	wins=[x.split(' ') for x in wins]
					# 	wins=[x[5] for x in wins]
					# 	wins=[x.replace(',','') for x in wins]
					# 	wins=[x.replace('(','') for x in wins]
					# 	wins=[x.replace(')','') for x in wins]
					# 	wins=[int(x) for x in wins]
					# 	return(sum(wins))
					# def returned(self): #возврат
					# 	returned=[line for line in text if 'returned to 7_ee_Zy' in line]
					# 	returned=[x.split(' ') for x in returned]
					# 	returned=[x[4] for x in returned]
					# 	returned=[x.replace(',','') for x in returned]
					# 	returned=[int(x) for x in returned]
					# 	return(sum(returned))
					# def myStackPlus(self): #Общий плюс
					# 	wins=myStackPlus()
					# 	wins=wins.wins()
					# 	returned=myStackPlus()
					# 	returned=returned.returned()
					# 	return wins+returned				
				class myStack:					#размер моего стэка
					def myStack(self,value=myChips):
						myStackPluss=myStackPlus()
						myStackPluss=myStackPluss.myStackPlus()
						myStackMinuss=myStackMinus()
						myStackMinuss=myStackMinuss.myStackMinus()
						myStack=value-myStackMinuss+myStackPluss
						return 	myStack	

						
					
					
				class allkards:					#комбинации
					def allkards(self):
						myCard=myCards()
						myCard=myCard.myCardsDig()
						myMastk=Mast()
						myMastk=myMastk.Mast()
						bordK=bord()
						bordK=bordK.bordDig()
						bordMast=Mast()
						bordMast=bordMast.Mast()
						allkards=sorted(myCard+bordK,reverse=True)
						for x in myMastk:
							if x>=5: allkards.append(True)
						return allkards	#виды комбинаций	
				class highCard(allkards): 			
					def highCard(self):			#старшая карта
						highCard=allkards()
						highCard=highCard.allkards()
						return ['highCard',sorted(highCard,reverse=True)[:2]]			
				class pare(allkards):			#пара
					def pare(self):
						xxx=bord()
						xxx=xxx.bordDig()
						if len(xxx)!=len(set(xxx)):
							bords=bord()
							bords=bords.bordDig()
							bords=set(bords)
							bords=list(bords)
							bords=sorted(bords,reverse=True)
							pare=myCards()
							pare=pare.myCardsDig()
							pare=pare+bords
							if preflopCards[0]!=preflopCards[1]:
								pare14=[1 for x in pare if x==14]
								if sum(pare14)==2:return ['pare',bords.index(14)]
								pare13=[1 for x in pare if x==13]
								if sum(pare13)==2:return ['pare',bords.index(13)]
								pare12=[1 for x in pare if x==12]
								if sum(pare12)==2:return ['pare',bords.index(12)]
								pare11=[1 for x in pare if x==11]
								if sum(pare11)==2:return ['pare',bords.index(11)]
								pare10=[1 for x in pare if x==10]
								if sum(pare10)==2:return ['pare',bords.index(10)]
								pare9=[1 for x in pare if x==9]
								if sum(pare9)==2:return ['pare',bords.index(9)]
								pare8=[1 for x in pare if x==8]
								if sum(pare8)==2:return ['pare',bords.index(8)]
								pare7=[1 for x in pare if x==7]
								if sum(pare7)==2:return ['pare',bords.index(7)]
								pare6=[1 for x in pare if x==6]
								if sum(pare6)==2:return ['pare',bords.index(6)]
								pare5=[1 for x in pare if x==5]
								if sum(pare5)==2:return ['pare',bords.index(5)]
								pare4=[1 for x in pare if x==4]
								if sum(pare4)==2:return ['pare',bords.index(4)]
								pare3=[1 for x in pare if x==3]
								if sum(pare3)==2:return ['pare',bords.index(3)]
								pare2=[1 for x in pare if x==2]
								if sum(pare2)==2:return ['pare',bords.index(2)]	
							else:return ['pare',pare.index(preflopCards[0])]
						else:
							pare=allkards()
							pare=pare.allkards()
							bords=bord()
							bords=bords.bordDig()
							if preflopCards[0]!=preflopCards[1]:
								pare14=[1 for x in pare if x==14]
								if sum(pare14)==2:return ['pare',bords.index(14)]
								pare13=[1 for x in pare if x==13]
								if sum(pare13)==2:return ['pare',bords.index(13)]
								pare12=[1 for x in pare if x==12]
								if sum(pare12)==2:return ['pare',bords.index(12)]
								pare11=[1 for x in pare if x==11]
								if sum(pare11)==2:return ['pare',bords.index(11)]
								pare10=[1 for x in pare if x==10]
								if sum(pare10)==2:return ['pare',bords.index(10)]
								pare9=[1 for x in pare if x==9]
								if sum(pare9)==2:return ['pare',bords.index(9)]
								pare8=[1 for x in pare if x==8]
								if sum(pare8)==2:return ['pare',bords.index(8)]
								pare7=[1 for x in pare if x==7]
								if sum(pare7)==2:return ['pare',bords.index(7)]
								pare6=[1 for x in pare if x==6]
								if sum(pare6)==2:return ['pare',bords.index(6)]
								pare5=[1 for x in pare if x==5]
								if sum(pare5)==2:return ['pare',bords.index(5)]
								pare4=[1 for x in pare if x==4]
								if sum(pare4)==2:return ['pare',bords.index(4)]
								pare3=[1 for x in pare if x==3]
								if sum(pare3)==2:return ['pare',bords.index(3)]
								pare2=[1 for x in pare if x==2]
								if sum(pare2)==2:return ['pare',bords.index(2)]	
							else:return ['pare',pare.index(preflopCards[0])]

							



				class twopare(allkards):		#две пары
					def twopare(self):
						bordd=bord()
						bordd=bordd.bordDig()
						twopare=allkards()
						twopare=twopare.allkards()	
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
						if len(twopareFin)>=2: 
							if twopareFin[0]==preflopCards[0] and twopareFin[1]==preflopCards[1]:return ['two']
						if preflopCards[0]==preflopCards[1]:return ['pare',twopare.index(preflopCards[0])]
						# if len(bordd)==3:
						# 	if preflopCards[0]==bordd[0] or preflopCards[0]==bordd[1] or preflopCards[0]==bordd[2] or preflopCards[1]==bordd[0] or preflopCards[1]==bordd[1] or preflopCards[1]==bordd[2]:return 'pare'
						# if len(bordd)==4:
						# 	if preflopCards[0]==bordd[0] or preflopCards[0]==bordd[1] or preflopCards[0]==bordd[2] or preflopCards[0]==bordd[3] or preflopCards[1]==bordd[0] or preflopCards[1]==bordd[1] or preflopCards[1]==bordd[2] or preflopCards[0]==bordd[3]:return 'pare'
						# if len(bordd)==5:
						# 	if preflopCards[0]==bordd[0] or preflopCards[0]==bordd[1] or preflopCards[0]==bordd[2] or preflopCards[0]==bordd[3] or preflopCards[0]==bordd[4] or preflopCards[1]==bordd[0] or preflopCards[1]==bordd[1] or preflopCards[1]==bordd[2] or preflopCards[0]==bordd[3] or preflopCards[0]==bordd[4]:return 'pare'


							
							
				class trips:					#трипс
					def trips(self):
						trips=allkards()
						trips=trips.allkards()
						trips14=[1 for x in trips if x==14]
						if sum(trips14)==3:return ['trips']
						trips13=[1 for x in trips if x==13]
						if sum(trips13)==3:return ['trips']
						trips12=[1 for x in trips if x==12]
						if sum(trips12)==3:return ['trips']
						trips11=[1 for x in trips if x==11]
						if sum(trips11)==3:return ['trips']
						trips10=[1 for x in trips if x==10]
						if sum(trips10)==3:return ['trips']
						trips9=[1 for x in trips if x==9]
						if sum(trips9)==3:return ['trips']
						trips8=[1 for x in trips if x==8]
						if sum(trips8)==3:return ['trips']
						trips7=[1 for x in trips if x==7]
						if sum(trips7)==3:return ['trips']
						trips6=[1 for x in trips if x==6]
						if sum(trips6)==3:return ['trips']
						trips5=[1 for x in trips if x==5]
						if sum(trips5)==3:return ['trips']
						trips4=[1 for x in trips if x==4]
						if sum(trips4)==3:return ['trips']
						trips3=[1 for x in trips if x==3]
						if sum(trips3)==3:return ['trips']
						trips2=[1 for x in trips if x==2]
						if sum(trips2)==3:return ['trips']					#трипс
				class kare:					#трипс
					def kare(self):
						kare=allkards()
						kare=kare.allkards()
						kare14=[1 for x in kare if x==14]
						if sum(kare14)==4:return ['kare']
						kare13=[1 for x in kare if x==13]
						if sum(kare13)==4:return ['kare']
						kare12=[1 for x in kare if x==12]
						if sum(kare12)==4:return ['kare']
						kare11=[1 for x in kare if x==11]
						if sum(kare11)==4:return ['kare']
						kare10=[1 for x in kare if x==10]
						if sum(kare10)==4:return ['kare']
						kare9=[1 for x in kare if x==9]
						if sum(kare9)==4:return ['kare']
						kare8=[1 for x in kare if x==8]
						if sum(kare8)==4:return ['kare']
						kare7=[1 for x in kare if x==7]
						if sum(kare7)==4:return ['kare']
						kare6=[1 for x in kare if x==6]
						if sum(kare6)==4:return ['kare']
						kare5=[1 for x in kare if x==5]
						if sum(kare5)==4:return ['kare']
						kare4=[1 for x in kare if x==4]
						if sum(kare4)==4:return ['kare']
						kare3=[1 for x in kare if x==3]
						if sum(kare3)==4:return ['kare']
						kare2=[1 for x in kare if x==2]
						if sum(kare2)==4:return ['kare']	
				class street:
					def street(self):
						street=allkards()
						street=street.allkards()
						street=set(street)
						street=list(street)	
						street=sorted(street,reverse=True)


						if len(street)==5:
							if street[0]-street[1]==1 and street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1:return ['street']
							if street[-1]==2 and street[-2]==3 and street[-3]==4 and street[-4]==5 and street[0]==14:return ['street']
						if len(street)==6:
							if street[0]-street[1]==1 and street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1:return ['street']
							if street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1 and street[4]-street[5]==1:return ['street']
							if street[-1]==2 and street[-2]==3 and street[-3]==4 and street[-4]==5 and street[0]==14:return ['street']
						if len(street)==7:
							if street[0]-street[1]==1 and street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1:return ['street']
							if street[1]-street[2]==1 and street[2]-street[3]==1 and street[3]-street[4]==1 and street[4]-street[5]==1:return ['street']
							if street[2]-street[3]==1 and street[3]-street[4]==1 and street[4]-street[5]==1 and street[5]-street[6]==1:return ['street']
							if street[-1]==2 and street[-2]==3 and street[-3]==4 and street[-4]==5 and street[0]==14:return ['street']
				class flash:						
					def flash(self):			#флэш
						flash=allkards()
						flash=flash.allkards()
						if flash[-1]==True: return ['flash']			#флэш
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




				def rounddd():			#определение текущего раунда
					doska=bord()
					doska=doska.bord()
					if len(doska)==0:return 0
					if len(doska)==3:return 1
					if len(doska)==4:return 2
					if len(doska)==5:return 3 
								#действие
				def position():
					last=lastHand()
					pos=[x for x in last if '7_ee_Zy posts' in x]
					if pos:
						pos=pos[0].split(' ')
						if pos[-4]=='small':return 'ip'
						else:return 'oop'










				# roundx=rounddd()
				# roundx=roundx.rounddd()
				# pos=action()
				# pos=pos.position()
				
				
				last=lastHand()
				
				cards=whatKomb()
				cards=cards.whatKomb()
				def mystack():
					whoesStack=0
					if os.popen('ls ~/.wine/drive_c/Program\ Files\ \(x86\)/Full\ Tilt\ Poker/HandHistory/7_ee_Zy/*em.txt').readlines():
						directory=[x[:-1] for x in os.popen('ls ~/.wine/drive_c/Program\ Files\ \(x86\)/Full\ Tilt\ Poker/HandHistory/7_ee_Zy/*em.txt').readlines()]
						lasthand=io.open(directory[-1],'r',encoding='utf16')
						lasthand=[x for x in lasthand]
						lasthand=''.join(lasthand)
						lasthand=lasthand.split('Full Tilt Poker Game #')
						lasthand=lasthand[-1]
						lasthand=lasthand.split('\n')
						mystack=[x for x in lasthand if 'Seat 2: 7_ee_Zy' in x or 'Seat 1: 7_ee_Zy' in x]
						mystack=mystack[0]
						mystack=mystack.split(' ')
						mystack=mystack[3]
						mystack=mystack.replace('(','')
						mystack=mystack.replace(')','')
						mystack=mystack.replace(',','')
						mystack=int(mystack)
						blind=[x for x in lasthand if '7_ee_Zy posts the' in x]
						blind=blind[-1]
						blind=blind.split(' ')
						blind=blind[6]
						blind=blind.replace(',','')
						blind=int(blind)
						collectedLost=0
						wonLost=0
						won=0
						collected=0
						for x in lasthand: 
							if 'collected' in x:
								if myNick in x:
									collected=x.split(' ')
									collectedx=collected.index('collected')
									collected=collected[collectedx+1]
									collected=collected.replace('(','')
									collected=collected.replace(')','')
									collected=collected.replace(',','')
									collected=int(collected)
								else:
									collectedLost=x.split(' ')
									collectedLostx=collectedLost.index('collected')
									collectedLost=collectedLost[collectedLostx+1]
									collectedLost=collectedLost.replace('(','')
									collectedLost=collectedLost.replace(')','')
									collectedLost=collectedLost.replace(',','')
									collectedLost=int(collectedLost)

						for x in lasthand: 
							if 'and won' in x:
								if myNick in x:
									won=x.split(' ')
									wonx=won.index('won')
									won=won[wonx+1]
									won=won.replace('(','')
									won=won.replace(')','')
									won=won.replace(',','')
									won=int(won)
								else:
									wonLost=x.split(' ')
									wonLostx=wonLost.index('won')
									wonLost=wonLost[wonLostx+1]
									wonLost=wonLost.replace('(','')
									wonLost=wonLost.replace(')','')
									wonLost=wonLost.replace(',','')
									wonLost=int(wonLost)

						mystack=mystack+0.5*won+0.5*collected-0.5*wonLost-0.5*collectedLost
						myStackNow=myStackMinus()
						myStackNow=myStackNow.myStackMinus()

						myStackNow=mystack-myStackNow
					else:myStackNow=myChips
					return myStackNow
				
				class pot: 						#размер пота
					def blind(self):
						last=lastHand()
						blind=[line for line in last if 'posts the' in line]
						blind=[x.split(' ') for x in blind]
						blind=[x[7] for x in blind]
						blind=[x.replace(',','') for x in blind]
						blind=[int(x) for x in blind]
						return(sum(blind))
					def rais(self):
						pot=[]
						last=lastHand()
						for x in last:
							if 'raises to' in x:
								if 'posts the small' in last[last.index(x)-3]:
									rai=x.split(' ')
									rai=rai[4]	#извл. блайнда
									rai=rai.replace(',','')
									rai=int(rai)
									if rai>mystack():rai=mystack()
									# if rai>effectiveStack():
									# 	rai=effectiveStack()
									bli=last[last.index(x)-3].split(' ')
									bli=bli[7]
									bli=bli.replace(',','')
									bli=int(bli)
									rai=rai-bli
									pot.append(rai)
								else:
									rai=x.split(' ')
									rai=rai[4]
									rai=rai.replace(',','')
									rai=int(rai)
									if rai>mystack():rai=mystack()
									pot.append(rai)
						return sum(pot)
					def call(self):
						last=lastHand()
						call=[]
						for x in last:
							if 'calls' in x:
								last=x.split(' ')
								call.append(last[3])
								call=[x.replace(',','') for x in call]
						call=[int(x) for x in call]
						return sum(call)
					def bet(self):
						last=lastHand()
						bet=[]
						for x in last:
							if 'bets' in x:
								last=x.split(' ')
								betx=last[3]
								betx=betx.replace(',','')
								betx=int(betx)
								if betx>mystack():betx=mystack()
								bet.append(betx)
						return sum(bet)

					def pot(self):
						blind=pot()
						blind=blind.blind()
						rais=pot()
						rais=rais.rais()
						call=pot()
						call=call.call()
						bet=pot()
						bet=bet.bet()
						return blind+rais+call+bet	
				xx=pot()
				xx=xx.bet()
				potx=pot()
				potx=potx.pot()
				def effectiveStack():
					effectiveStack=myChips*2-mystack()-potx
					if effectiveStack>mystack():effectiveStack=mystack()
					return effectiveStack
				stack=mystack()



				class callSize: 				#фишек для колла при бете
					def callSize(self):			
						last=lastHand()
						mySta=mystack()

						if 'bets' in last[-1]:
							callSize=last[-1].split(' ')
							callSize=callSize[3]
							callSize=callSize.replace(',','')
							callSize=int(callSize)
							if callSize>mySta:return mySta
							return callSize		
				class raiseSize: 				#сумма для колла при рейзе
					def raiseSize(self):
						last=lastHand() 
						mySta=mystack()

						if 'raises to' in last[-1] and 'been dealt' not in last[-2]:
							if '7_ee_Zy posts' not in last[-3]:
								my=last[-2].split(' ')
								my=my[-1]
								my=my.replace(',','')
								my=int(my)
								his=last[-1].split(' ')
								his=his[4]
								his=his.replace(',','')
								his=int(his)
								toCall=his-my
								if toCall>mySta:return mySta
							if toCall:return toCall
							return 0
						if 'raises to' in last[-1]:
							my=last[-3].split(' ')
							my=my[-1]
							my=my.replace(',','')
							my=int(my)
							his=last[-1].split(' ')
							his=his[4]
							his=his.replace(',','')
							his=int(his)
							toCall=his-my
							if toCall>mySta:return mySta
							if toCall:return toCall
							return 0	
						if 'bets' in last[-1]:
							callSize=last[-1].split(' ')
							callSize=callSize[3]
							callSize=callSize.replace(',','')
							callSize=int(callSize)
							if callSize>mySta:return mySta
							if callSize: return callSize
							return 0
				
				toCallx=raiseSize()
				toCallx=toCallx.raiseSize()
				def statsOvTest(text):
					statsOvTest=[]
					for x in text:
						if 'bets' in x:statsOvTest.append('b')
						if 'raises to' in x:statsOvTest.append('r')
						if 'checks' in x:statsOvTest.append('0') 
						if 'calls' in x:statsOvTest.append('c') 
						if 'folds' in x:statsOvTest.append('f') 
					return statsOvTest

				#СТатистика
				###########
				# r +
				# rf +
				# rc0b+
				# rc0bf +
				# rc0bc0b+
				# rc0bc0bf+
				# rrcbr+
				# rrcbrf+
				# rrc0b+
				# rrc0bf+
				# rrc0bc0b+
				# rrc0bc0bf+

				# rri+
				# rrfi+
				# rrcbi+
				# rrcbfi+
				# rcbi+
				# rcbfi+
				# rc0bri+
				# rc0brfi+
				# rc00bi+
				# rc00bfi+
				# rc00bcbi
				# rc00bcbfi






				










				statsOOP=[statsOvTest(x) for x in textForStat if len(x)>3 and niccx in x[1]]
				statsOOP=[''.join(x) for x in statsOOP]
				statsIP=[statsOvTest(x) for x in textForStat if len(x)>3 and niccx not in x[1]]
				statsIP=[''.join(x) for x in statsIP]
				



				


				
				c0_OOP=0.33
				c_OOPx=[x for x in statsOOP if 'c' in x[:1]]
				if len(c_OOPx)>=3:
					c_OOPx=c_OOPx[-3:]
					c0_OOP=sum([1 for x in c_OOPx if 'c0' in x[:2]])/3
				crcbcbf_OOP=0.33
				crcbcb_OOPx=[x for x in statsOOP if 'crcbcb' in x[:6]]
				if len(crcbcb_OOPx)>=3:
					crcbcb_OOPx=crcbcb_OOPx[-3:]
					crcbcbf_OOP=sum([1 for x in crcbcb_OOPx if 'crcbcbf' in x[:7]])/3
				crcbf_OOP=0.33
				rrcbc_OOP=0.33
				crcb_OOPx=[x for x in statsOOP if 'crcb' in x[:4]]
				if len(crcb_OOPx)>=3:
					crcb_OOPx=crcb_OOPx[-3:]
					crcbf_OOP=sum([1 for x in crcb_OOPx if 'crcbf' in x[:5]])/3
					rrcbc_OOP=sum([1 for x in crcb_OOPx if 'crcbc' in x[:5]])/3
				crf_OOP=0.33
				crr_OOP=0.33
				cr_OOPx=[x for x in statsOOP if 'cr' in x[:2]]
				if len(cr_OOPx)>=3:
					cr_OOPx=cr_OOPx[-3:]
					crf_OOP=sum([1 for x in cr_OOPx if 'crf' in x[:3]])/3
					crr_OOP=sum([1 for x in cr_OOPx if 'cr' in x[:3]])/3
				rrf_OOP=0.33
				rr_OOPx=[x for x in statsOOP if 'rr' in x[:2]]
				if len(rr_OOPx)>=3:
					rr_OOPx=rr_OOPx[-3:]
					rrf_OOP=sum([1 for x in rr_OOPx if 'rrf' in x[:3]])/3
				rrcbf_OOP=0.33
				rrcb_OOPx=[x for x in statsOOP if 'rrcb' in x[:4]]
				if len(rrcb_OOPx)>=3:
					rrcb_OOPx=rrcb_OOPx[-3:]
					rrcbf_OOP=sum([1 for x in rrcb_OOPx if 'rrcbf' in x[:5]])/3
				rcbf_OOP=0.33
				rcb_OOPx=[x for x in statsOOP if 'rcb' in x[:3]]
				if len(rcb_OOPx)>=3:
					rcb_OOPx=rcb_OOPx[-3:]
					rcbf_OOP=sum([1 for x in rcb_OOPx if 'rcbf' in x[:4]])/3
				rc0brf_OOP=0.33
				rc0br_OOPx=[x for x in statsOOP if 'rc0br' in x[:5]]
				if len(rc0br_OOPx)>=3:
					rc0br_OOPx=rc0br_OOPx[-3:]
					rc0brf_OOP=sum([1 for x in rc0br_OOPx if 'rc0brf' in x[:6]])/3
				rc00bf_OOP=0.33
				rc00b_OOPx=[x for x in statsOOP if 'rc00b' in x[:5]]
				if len(rc00b_OOPx)>=3:
					rc00b_OOPx=rc00b_OOPx[-3:]
					rc00bf_OOP=sum([1 for x in rc00b_OOPx if 'rc00bf' in x[:6]])/3
				rc00bcbf_OOP=0.33
				rc00bcb_OOPx=[x for x in statsOOP if 'rc00bcb' in x[:7]]
				if len(rc00bcb_OOPx)>=3:
					rc00bcb_OOPx=rc00bcb_OOPx[-3:]
					rc00bcbf_OOP=sum([1 for x in rc00bcb_OOPx if 'rc00bcbf' in x[:8]])/3
				c0bf_OOP=0.33
				c0b_OOPx=[x for x in statsOOP if 'c0b' in x[:3]]
				if len(c0b_OOPx)>=3:
					c0b_OOPx=c0b_OOPx[-3:]
					c0bf_OOP=sum([1 for x in c0b_OOPx if 'c0bf' in x[:4]])/3
				c0bcbf_OOP=0.33
				c0bcb_OOPx=[x for x in statsOOP if 'c0bcb' in x[:5]]
				if len(c0bcb_OOPx)>=3:
					c0bcb_OOPx=c0bcb_OOPx[-3:]
					c0bcbf_OOP=sum([1 for x in c0bcb_OOPx if 'c0bcbf' in x[:6]])/3
				c00bf_OOP=0.33
				c00b_OOPx=[x for x in statsOOP if 'c00b' in x[:4]]
				if len(c00b_OOPx)>=3:
					c00b_OOPx=c00b_OOPx[-3:]
					c00bf_OOP=sum([1 for x in c00b_OOPx if 'c00bf' in x[:5]])/3
				rf_OOP=0.33
				r_OOPx=[x for x in statsOOP if 'r' in x[:1]]
				if len(r_OOPx)>=3:
					r_OOPx=r_OOPx[-3:]
					rf_OOP=sum([1 for x in r_OOPx if 'rf' in x[:5]])/3
				rrc_OOP=0.33
				rr_OOPx=[x for x in statsOOP if 'rr' in x[:2]]
				if len(rr_OOPx)>=3:
					rr_OOPx=rr_OOPx[-3:]
					rrc_OOP=sum([1 for x in rr_OOPx if 'rrc' in x[:3]])/3
				crc_OOP=0.33
				cr_OOPx=[x for x in statsOOP if 'cr' in x[:2]]
				if len(cr_OOPx)>=3:
					cr_OOPx=cr_OOPx[-3:]
					crc_OOP=sum([1 for x in cr_OOPx if 'crc' in x[:3]])/3
				crcbc_OOP=0.33
				crcb_OOPx=[x for x in statsOOP if 'crcb' in x[:4]]
				if len(crcb_OOPx)>=3:
					crcb_OOPx=crcb_OOPx[-3:]
					crcbc_OOP=sum([1 for x in crcb_OOPx if 'crcbc' in x[:5]])/3
				

				r_OOP=[x for x in statsOOP]
				if len(r_OOP)>=3:
					r_OOPx=r_OOPx[-3:]
					r_OOP=sum([1 for x in r_OOPx if 'r' in x[:1]])/3
				rrr_OOP=0.33
				rr_OOPx=[x for x in statsOOP]
				if len(rr_OOPx)>=3:
					rr_OOPx=rr_OOPx[-3:]
					rrr_OOP=sum([1 for x in rr_OOPx if 'rrr' in x[:3]])/3
				rrcbcb_OOP=0.33
				rrcbc_OOPx=[x for x in statsOOP if 'rrcbc' in x[:5]]
				if len(rrcbc_OOPx)>=3:
					rrcbc_OOPx=rrcbc_OOPx[-3:]
					rrcbcb_OOP=sum([1 for x in rrcbc_OOPx if 'rrcbcb' in x[:6]])/3
				rrcbr_OOP=0.33
				rrcb_OOPx=[x for x in statsOOP if 'rrcb' in x[:4]]
				if len(rrcb_OOPx)>=3:
					rrcb_OOPx=rrcb_OOPx[-3:]
					rrcbr_OOP=sum([1 for x in rrcb_OOPx if 'rrcbr' in x[:5]])/3
				rrcbcbr_OOP=0.33
				rrcbcb_OOPx=[x for x in statsOOP if 'rrcbcb' in x[:6]]
				if len(rrcbcb_OOPx)>=3:
					rrcbcb_OOPx=rrcbcb_OOPx[-3:]
					rrcbcbr_OOP=sum([1 for x in rrcbcb_OOPx if 'rrcbcbr' in x[:7]])/3
				rrcbcbc_OOP=0.33
				rrcbcb_OOPx=[x for x in statsOOP if 'rrcbcb' in x[:6]]
				if len(rrcbcb_OOPx)>=3:
					rrcbcb_OOPx=rrcbcb_OOPx[-3:]
					rrcbcbc_OOP=sum([1 for x in rrcbcb_OOPx if 'rrcbcbc' in x[:7]])/3
				rrcbcbf_OOP=0.33
				rrcbcb_OOPx=[x for x in statsOOP if 'rrcbcb' in x[:6]]
				if len(rrcbcb_OOPx)>=3:
					rrcbcb_OOPx=rrcbcb_OOPx[-3:]
					rrcbcbf_OOP=sum([1 for x in rrcbcb_OOPx if 'rrcbcbf' in x[:7]])/3
				rrcbcbcbf_OOP=0.33
				rrcbcbcb_OOPx=[x for x in statsOOP if 'rrcbcbcb' in x[:8]]
				if len(rrcbcbcb_OOPx)>=3:
					rrcbcbcb_OOPx=rrcbcbcb_OOPx[-3:]
					rrcbcbcbf_OOP=sum([1 for x in rrcbcbcb_OOPx if 'rrcbcbcbf' in x[:9]])/3
				c_OOP=0.33
				c_OOPx=[x for x in statsOOP]
				if len(c_OOPx)>=3:
					c_OOPx=c_OOPx[-3:]
					c_OOP=sum([1 for x in c_OOPx if 'c' in x[:1]])/3

				rf=0.33
				rr=0.33
				rc=0.33
				rx=[x for x in statsIP if 'r' in x[:1]]
				if len(rx)>=3:
					rx=rx[-3:]
					rf=sum([1 for x in rx if 'rf' in x[:2]])/3
					rr=sum([1 for x in rx if 'rr' in x[:2]])/3
					rc=sum([1 for x in rx if 'rc' in x[:2]])/3

				

				rcbrr=0.33
				rcbrx=[x for x in statsIP if 'rcbr' in x[:4]]
				if len(rcbrx)>=3:
					rcbrx=rcbrx[-3:]
					rcbrr=sum([1 for x in rcbrx if 'rcbrr' in x[:5]])/3


				


				rcbrf=0.33
				rcbrx=[x for x in statsIP if 'rcbr' in x[:4]]
				if len(rcbrx)>=3:
					rcbrx=rcbrx[-3:]
					rcbrf=sum([1 for x in rcbrx if 'rcbrf' in x[:5]])/3
				rcb=0.33
				rcx=[x for x in statsIP if 'rc' in x[:2]]
				if len(rcx)>=3:
					rcx=rcx[-3:]
					rcb=sum([1 for x in rcx if 'rcb' in x[:3]])/3
				rc0=0.33
				rcx=[x for x in statsIP if 'rc' in x[:2]]
				if len(rcx)>=3:
					rcx=rcx[-3:]
					rc0=sum([1 for x in rcx if 'rc0' in x[:3]])/3
				rc0bc=0.33
				rc0bx=[x for x in statsIP if 'rc0b' in x[:4]]
				if len(rc0bx)>=3:
					rc0bx=rc0bx[-3:]
					rc0bc=sum([1 for x in rc0bx if 'rc0bc' in x[:5]])/3

				rc0bf=0.33
				rc0bx=[x for x in statsIP if 'rc0b' in x[:4]]
				if len(rc0bx)>=3:
					rc0bx=rc0bx[-3:]
					rc0bf=sum([1 for x in rc0bx if 'rc0bf' in x[:5]])/3
				rc0bc0bf=0.33
				rc0bc0bx=[x for x in statsIP if 'rc0bc0b' in x[:7]]
				if len(rc0bc0bx)>=3:
					rc0bc0bx=rc0bc0bx[-3:]
					rc0bc0bf=sum([1 for x in rc0bc0bx if 'rc0bc0bf' in x[:8]])/3
				rrcbrf=0.33
				rrcbrx=[x for x in statsIP if 'rrcbr' in x[:5]]
				if len(rrcbrx)>=3:
					rrcbrx=rrcbrx[-3:]
					rrcbrf=sum([1 for x in rrcbrx if 'rrcbrf' in x[:6]])/3
				rrc0bf=0.33
				rrc0bx=[x for x in statsIP if 'rrc0b' in x[:5]]
				if len(rrc0bx)>=3:
					rrc0bx=rrc0bx[-3:]
					rrc0bf=sum([1 for x in rrc0bx if 'rrc0bf' in x[:6]])/3
				rrc0bc0bf=0.33
				rrc0bc0bx=[x for x in statsIP if 'rrc0bc0b' in x[:8]]
				if len(rrc0bc0bx)>=3:
					rrc0bc0bx=rrc0bc0bx[-3:]
					rrc0bc0bf=sum([1 for x in rrc0bc0bx if 'rrc0bc0bf' in x[:9]])/3
				rc0bc0=0.33
				rc0bcx=[x for x in statsIP if 'rc0bc' in x[:5]]
				if len(rc0bcx)>=3:
					rc0bcx=rc0bcx[-3:]
					rc0bc0=sum([1 for x in rc0bcx if 'rc0bc0' in x[:6]])/3
				rc0bc0bc=0.33
				rc0bc0bx=[x for x in statsIP if 'rc0bc0b' in x[:7]]
				if len(rc0bc0bx)>=3:
					rc0bc0bx=rc0bc0bx[-3:]
					rc0bc0bc=sum([1 for x in rc0bc0bx if 'rc0bc0bc' in x[:8]])/3
				rc0br=0.33
				rc0bx=[x for x in statsIP if 'rc0b' in x[:4]]
				if len(rc0bx)>=3:
					rc0bx=rc0bx[-3:]
					rc0br=sum([1 for x in rc0bx if 'rc0br' in x[:5]])/3
				rc0bc0br=0.33
				rc0bc0bx=[x for x in statsIP if 'rc0bc0b' in x[:7]]
				if len(rc0bc0bx)>=3:
					rc0bc0bx=rc0bc0bx[-3:]
					rc0bc0br=sum([1 for x in rc0bc0bx if 'rc0bc0br' in x[:8]])/3
				rc0b=0.33
				rc0x=[x for x in statsIP if 'rc0' in x[:3]]
				if len(rc0x)>=3:
					rc0x=rc0x[-3:]
					rc0b=sum([1 for x in rc0x if 'rc0b' in x[:4]])/3



				statsIPMas=[['rf',rf],['rc0bf',rc0bf],
							['rc0bc0bf',rc0bc0bf],['rrcbrf',rrcbrf],
							['rrc0bc0bf',rrc0bc0bf],
							['rcbrf',rcbrf],['rc',rc],['rcb',rcb],
							['rc0bc',rc0bc],['rc0',rc0],
							['rcbrr',rcbrr],['rc0br',rc0br],
							['rc0bc0bc',rc0bc0bc],['rc0bc0',rc0bc0],['rr',rr]]
				statsOOPMas=[['rrf',rrf_OOP],['rrcbf',rrcbf_OOP],
							 ['rcbf',rcbf_OOP],
							 ['rc0brf',rc0brf_OOP],['rc00bf',rc00bf_OOP],
							 ['rc00bcbf',rc00bcbf_OOP],
							 ['crcbcbf',crcbcbf_OOP],['crcbf',crcbf_OOP],
							 ['crf',crf_OOP],
							 ['c0bf',c0bf_OOP],
							 ['c0bcbf',c0bcbf_OOP],
							 ['r',r_OOP],['rrc',rrc_OOP],['c',c_OOP],['c0',c0_OOP],
							 ['crc',crc_OOP],['crcbc',crcbc_OOP],['rrcbc',rrcbc_OOP],
							 ['rrcbr',rrcbr_OOP],['rrcbcb',rrcbcb_OOP],['rrr',rrr_OOP],
							 ['rrcbcbr',rrcbcbr_OOP],['rrcbcbc',rrcbcbc_OOP],['rrcbcbf',rrcbcbf_OOP],
							 ['rrcbcbcbf',rrcbcbcbf_OOP]]

				#Линия розыгрыша

				lineIP=''.join(statsOvTest(textForStat[-1]))
				
				def didI():
					last=lastHand()
					pos=position()
					if pos:
						if len(last)>=3:
							if '7_ee_Zy posts the' in last[-3] and 'folds'  not in last[-1]:return 1
							if pos=='oop' and 'is [' in last [-1]and 'folds'  not in last[-1]:return 1
							if 'raises to' in last[-1] and '7_ee_Zy' not in last[-1]and 'folds'  not in last[-1]:return 1
							if 'bets' in last[-1] and '7_ee_Zy' not in last[-1]and 'folds'  not in last[-1]:return 1
							if 'checks' in last[-1] and '7_ee_Zy' not in last[-1] and 'is [' in last[-2]: return  1

					return 0

				def action():
					import diapazon
					diapazonx=[]
					indicator=lastHand()[0].split(' ')
					indicator=indicator[-1]
					diapazonx=diapazon.diapazonPreFlop()
					while lastHand()[0].split(' ')[-1]==indicator:
						while rounddd()==0:
							while not didI() and lastHand()[0].split(' ')[-1]==indicator:
								chattx()
								diapazonx=diapazon.diapazonPercent(diapazonx,eval(lineIP))
							if position()=='oop':
								try:eval(lineIP)
								except NameError:
									if lineIP and lineIP[-1]=='c':
										if diapazon.evaluatePreFlop(diapazonx)>=0.55:bettx()
										else:checkkx()
									elif lineIP and lineIP[-1]=='r':
										if diapazon.evaluatePreFlop(diapazonx)>=0.75:
											if stack<=toCallx:calllx()
											bettx()
										elif diapazon.evaluatePreFlop(diapazonx)>=toCallx/(potx+toCallx):calllx()
								else:
									if lineIP and lineIP[-1]=='c':
										if diapazon.evaluatePreFlop(diapazonx.diapazonPercent(diapazonx,eval(lineIP)))>=0.55:bettx()
										else:checkkx()
									elif lineIP and lineIP[-1]=='r':
										if diapazon.evaluatePreFlop(diapazon.diapazonPercent(diapazonx,eval(lineIP)))>=0.75:
											if stack<=toCallx:calllx()
											bettx()
										elif diapazon.evaluatePreFlop(diapazon.diapazonPercent(diapazonx,eval(lineIP)))>=toCallx/(potx+toCallx):calllx()
							if position()=='ip':
								if not lineIP:
									if diapazon.evaluatePreFlop(diapazonx)>=0.55:bettx()
								else:
									try:eval(lineIP)
									except NameError:
										if lineIP and lineIP[-1]=='r':
											if diapazon.evaluatePreFlop(diapazonx)>=0.75:
												if stack<=toCallx:calllx()
												pushhx()
											elif diapazon.evaluatePreFlop(diapazonx)>=toCallx/(potx+toCallx):calllx()
									else:
										if lineIP and lineIP[-1]=='r':
											if diapazon.evaluatePreFlop(diapazon.diapazonPercent(diapazonx,eval(lineIP)))>=0.75:
												if stack<=toCallx:calllx()
												pushhx()
											elif diapazon.evaluatePreFlop(diapazon.diapazonPercent(diapazonx,eval(lineIP)))>=toCallx/(potx+toCallx):calllx()
						while rounddd()>0:
							while not didI() and lastHand()[0].split(' ')[-1]==indicator:
								chattx()
								diapazon=diapazon.diapazonPercent(diapazonx,eval(lineIP))
							if position()=='oop':
								try:eval(lineIP)
								except NameError:
									# print(evaluate.diapazonPercent(diapazon,0.33))
									# print(evaluate.evaluatePostFlop(evaluate.diapazonPercent(diapazon,0.33)))
									if diapazon.evaluatePostFlop(diapazon.diapazonPercent(diapazonx,0.33))>=0.5:bettx()
								else:
									if lineIP[-1]!='r' and lineIP[-1]!='b':
										if diapazon.evaluatePostFlop(diapazon.diapazonPercent(diapazonx,eval(lineIP)))>=0.5:bettx()
									
									else:
										if diapazon.evaluatePostFlop(diapazon.diapazonPercent(diapazonx,eval(lineIP)))>=0.75:
											if stack<=toCallx:calllx()
											pushhx()
										elif diapazon.evaluatePostFlop(diapazon.diapazonPercent(diapazonx,eval(lineIP)))>=toCallx/(potx+toCallx):calllx()
				action()

				# def actionx():
				# 	if didI()=='fold':return foldsx()
				# 	if didI()=='bet':return bettx()
				# 	if didI()=='check':return checkkx()
				# 	if didI()=='call':return calllx()
				# 	if didI()=='push':return pushhx()
				# 	if didI()=='raise':return bettx()

			else:
				closeWindow()
				time.sleep(1)
				pyautogui.click(x=479, y=34)
				time.sleep(1)

				break


			# # ------------tester--------------
			# # i=314
			# # while text:
			# # 	print(i,'  ',didI())
			# # 	i-=1
			# # 	text.pop()a