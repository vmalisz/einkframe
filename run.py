import my_7in5
import getPhoto
from time import sleep
import os
import sys
import logging
from datetime import datetime,time
#from waveshare_epd import epd7in5_HD

def main():
	libdir = 'lib'
	picdir = 'pic'
	if os.path.exists(libdir):
		sys.path.append(libdir)

	#now = datetime.time(datetime.now())
	#print('RANGE - '+time_in_range(datetime.time(datetime.now())))
	while time_in_range(datetime.time(datetime.now())):
		try:
			#if os.path.isfile('output.jpg'):
			my_7in5.show_pic()
			sleep(5)
			#else:
			getPhoto.refresh()
			sleep(600)
			#my_7in5.show_pic()
		except KeyboardInterrupt: 
			print(f"CTRL + C\n")
			my_7in5.initclear(sleep=True)
	else:
		print('COME BACK TOMORROW')
		my_7in5.initclear(sleep=True)

def time_in_range(x):
    """Return true if x is in the range [start, end]"""
    #start =  datetime.time(datetime(2020,5,16,5,0))
    start = time(7,0,0)
    end =  time(23,0,0)
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

if __name__ == '__main__':
   main()