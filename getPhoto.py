#import Google
import goog
from PIL import Image
from resizeimage import resizeimage
import os
import requests
import random


def main():
	print('kikoo')
	refresh()

def refresh():
	my_photo()
	#my_people()


def my_photo():
	CLIENT_SECRET_FILE = 'credentials.json'
	API_NAME = 'photoslibrary'
	API_VERSION = 'v1'
	SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
	          'https://www.googleapis.com/auth/photoslibrary.sharing']
	# SCOPES = [
	#   'https://www.googleapis.com/auth/photoslibrary.readonly',
	#   'profile'
	# ]

	service = goog.createserv(API_NAME, API_VERSION, SCOPES)
	#service = Google.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

	print(dir(service))

	#myAlbums = service.albums().list().execute()
	#myAlbums_list = myAlbums.get('albums')

	album_id = 'APPIOSg94kaIdBlkgFmjTj3DYEcs1hmOcq2YF-bPXrCT6ELvgbx50gXmREhd6Irl_UMHdOtn1OBh'

	#album = service.albums().get(albumId=album_id).execute()
	#print(dir(album))
	filters = "{'filters':{'mediaTypeFilter':{'mediaTypes': ['PHOTO']} } }"


	request_body = {
    'pageSize': 100,
    #'albumId': album_id,
    'filters': {
        'mediaTypeFilter': {
            'mediaTypes': ['PHOTO']
		}
	}
	}
	#body={'albumId': album_id,'pageSize':100
	media_files = service.mediaItems().search(body=request_body).execute()['mediaItems']

	#print(media_files)
	destination_folder = os.getcwd() #current
	count = 0
	print(f"NB PHOTOS {len(media_files)}\n")
	#for img in media_files:
		#count = count + 1
	#print(img)
	img = media_files[random.randint(0, len(media_files)-1)]
	print(img)
	response = requests.get(img['baseUrl']+'=w3048-h2024')
	if response.status_code == 200:
		print('Downloading file {0}'.format(img['filename']))
		with open(os.path.join(destination_folder, "myrandompic.jpg"), 'wb') as f:
			f.write(response.content)
			f.close()
		#if count > 4:
		#	break	

		resize("myrandompic.jpg")


def resize(filename):
	#print(filename)
	with open(filename, 'r+b') as f:
	    with Image.open(f) as image:
	        cover = resizeimage.resize_cover(image, [528,880])
	        cover.save('output.jpg')

if __name__ == '__main__':
   main()