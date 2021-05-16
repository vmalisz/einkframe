#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
#test
#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
#libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
libdir = 'lib'
#picdir = os.getcwd()
picdir = 'pic'
if os.path.exists(libdir):
    print('yay!')
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_HD
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

#GPIO.setmode(GPIO.BOARD)

def show_pic():

    logging.basicConfig(level=logging.DEBUG)

    try:
        #logging.info("epd7in5_HD Demo")

        epd = epd7in5_HD.EPD()
        #logging.info("init and Clear")
        epd.init()
        epd.Clear()

        #font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        #font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

     
        logging.info("3.read bmp file")
        #Himage = Image.open(os.path.join(picdir, '7in5_HD.bmp'))
        try:
            Himage = Image.open('output.jpg')
        except Exception as e:
            print(f'pb open img >>> {e}')

        epd.display(epd.getbuffer(Himage))
        #time.sleep(10)

        # logging.info("4.read bmp file on window")
        # Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
        # bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
        # Himage2.paste(bmp, (50,10))
        # epd.display(epd.getbuffer(Himage2))
        # time.sleep(2)

        #logging.info("Clear...")
        #epd.init()
        #epd.Clear()

        #logging.info("Goto Sleep...")
        #epd.sleep()
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd7in5_HD.epdconfig.module_exit()
        exit()
