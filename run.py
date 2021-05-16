import my_7in5
import getPhoto
from time import sleep

while True:
	getPhoto.refresh()
	sleep(90)
	my_7in5.show_pic()