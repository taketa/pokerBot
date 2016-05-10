#!/usr/bin
# -*- coding: utf-8 -*-
import diapazon
from poker import poker
from poker.utils import pretty_args
# print(str(''.join(diapazon.myCardss)))
# print(diapazon.bordx)
def evaluatePreFlop(diapazonx):
	evaluatex=[]
	sumEvaluate=[]
	enum = pretty_args(poker.monte_carlo)
	for x in diapazonx:
		evaluatex.append(enum([str(''.join(diapazon.myCardss)), x], trials=100))
	[sumEvaluate.append(x[0]) for x in evaluatex]
	evaluatex=sum(sumEvaluate)/len(sumEvaluate)

	return evaluatex
def evaluatePostFlop(diapazonx):
	evaluatex=[]
	sumEvaluate=[]
	enum = pretty_args(poker.full_enumeration)
	for x in diapazonx:
		evaluatex.append(enum([str(''.join(diapazon.myCardss)), x],str(''.join(diapazon.bordx))))
		# print(x+'	',enum([str(''.join(diapazon.myCardss)), x],str(''.join(diapazon.bordx))))
	[sumEvaluate.append(x[0]) for x in evaluatex]
	evaluatex=sum(sumEvaluate)/len(sumEvaluate)

	return evaluatex
def diapazonPercent(diapazon,percent):
	diapazonPercent=int(len(diapazon)*percent)
	diapazonPercent=diapazon[:diapazonPercent]
	return diapazonPercent
# print(evaluatePreFlop(diapazonPercent(diapazon.diapazonPreFlop(),0.33)))


# print(diapazon.diapazonPokerStove(diapazon.diapazon()))