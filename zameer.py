#SOURCE : BY Faraz Ali ID
#GITHUB  : 
#--------------------------------------------------------------------------#

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python Rashid.py')
os.system('git pull -q')
print(' [Hello] Connect Me whtsapp')
os.system('xdg-open https://api.whatsapp.com/send/?phone=923206691045&text&type=phone_number&app_absent=0')
input(' [Enter] Press Enter ')
os.system('xdg-open https://www.facebook.com/profile.php?id=100050407188659')

try:
	ah = os.listdir('/sdcard')
	if ['Android'] in ah:pass
except:print(' \n allow storage permission ...!');time.sleep(1);os.system('termux-setup-storage');exit()

W = '\033[97;1m'
R = '\033[91;1m'
