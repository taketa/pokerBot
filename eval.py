import os
import shutil
import pyautogui
import time
import io
def velueEval():
	roi=[]
	directory=[x[:-1] for x in os.popen('ls ~/.wine/drive_c/Program\ Files\ \(x86\)/Full\ Tilt\ Poker/HandHistory/reserv/*Summary.txt')]
	for x in directory:
		dd=[y for y in io.open(x,'r',encoding='utf16')]
		if '7_ee_Zy finished in 1st place' in dd[-1]:roi.append(1)
		else:roi.append(0)
	print(len(roi))
	roiWin=sum(roi)
	roiLost=len(roi)-roiWin
	overal=roiWin*1.86-roiLost
	roi=(overal/len(roi))-1
	# for x in directory:
		
		
	# 	if '7_ee_Zy finished in 1st place' in open(x)[-1]:roi.append(1)
	# 	else:roi.append(0)


	return roi
print(velueEval())