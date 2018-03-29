from pyvirtualdisplay import Display
from selenium import webdriver
import time
import sys

#sorteds.csv is a file I've been using that just lists all the domains we need to scrape separated by \n
m=open('sorteds.csv','r')
r=m.read()
m.close()
domains=r.replace('\r','').split('\n')

#starts the selenium driver
display = Display(visible=0, size=(800, 600))
display.start()
driver =webdriver.Chrome()

#function below creates a dictionary that numbers the domains, this is part of the method I use to restart the script when it breaks.
ddict={}
for i in range(0,len(domains)):
	ddict[domains[i]]=i

#This is also part of that method. while the actual scraper is running, it writes to log.txt to keep track of all the domains it's hit already
def getx():
	myfile=open('log.txt','r')
	mf=myfile.read()
	last=mf.split('\n')[len(mf.split('\n'))-2]
	print ('LAST            '+last)

	x=ddict[last]
	myfile.close()
	return x

#Here's the actual scraping part. It starts by using the two functions above to see where it left off in the log file,
#otherwise it starts from the beginning
#importantly, it's going to save all the .jpgs to the folder ./shots, so make sure that exists (or change it here)
#Getting a time-out error breaks the loop, unfortunately. The way I handle this is by running it on an EC2 (micro should work fine) and then
#using a bash command that restarts the script if it stops for whatever reason. It'll just check the log file every time and pick up where it left off

#command: http://rachbelaid.com/capturing-screenshots-of-website-with-python/

#while true ;
#>do
#>python screenshotter2.py
#>done

#that's it!

try:
	p=getx()
except:
	p=0
logfile=open('log.txt','a')
for i in range(p,len(domains)):
	try:
		print (domains[i])
		logfile.write(domains[i]+'\n')
		driver.get('http://www.'+domains[i])
		time.sleep(1)
		driver.save_screenshot('./shots/'+domains[i].replace('.','_')+'.jpg')
		print('click!')


	except:
		logfile.close()
		sys.exit()





