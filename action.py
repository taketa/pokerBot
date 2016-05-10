#!/usr/bin
# -*- coding: utf-8 -*-

def action():
	indicator=lastHand()[0].split(' ')
	indicator=indicator[-1]
	diapazon=diapazon.diapazonPreFlop()
	while lastHand()[0].split(' ')[-1]==indicator:
		while rounddd()==0:
			while not didI() and lastHand()[0].split(' ')[-1]==indicator:
				chattx()
				diapazon=evaluate.diapazonPercent(diapazon,eval(lineIP))
			if position()=='oop':
				if lineIP and lineIP[-1]=='c':
					if evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=0.55:bettx()
					else:checkkx()
				elif lineIP and lineIP[-1]=='r':
					if evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=0.75:
						if stack<=toCallx:calllx()
						bettx()
					elif evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=toCallx/(potx+toCallx):calllx()
			if position()=='ip':
				if not lineIP:
					if evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=0.55:bettx()
				elif lineIP and lineIP[-1]=='r':
					if evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=0.75:
						if stack<=toCallx:calllx()
						pushhx()
					elif evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=toCallx/(potx+toCallx):calllx()
		while rounddd()>0:
			while not didI() and lastHand()[0].split(' ')[-1]==indicator:
				chattx()
				diapazon=evaluate.diapazonPercent(diapazon,eval(lineIP))
			if position()=='oop':
				if lineIP[-1]!='r' and lineIP[-1]!='b':
					if evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=0.5:bettx()
				
				else:
					if evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=0.75:
						if stack<=toCallx:calllx()
						pushhx()
					elif evaluate.evaluatePreFlop(evaluate.diapazonPercent(diapazon,eval(lineIP)))>=toCallx/(potx+toCallx):calllx()




						
					

