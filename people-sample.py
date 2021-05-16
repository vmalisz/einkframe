def my_people():
	CLIENT_SECRET_FILE = 'credentials.json'	
	API_NAME = 'people'
	API_VERSION = 'v1'
	SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
	#SCOPES = ['https://www.googleapis.com/auth/photoslibrary']	

	service = goog.createserv(API_NAME, API_VERSION,SCOPES)
	#service = Google.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
	results = service.people().connections().list(
	    resourceName='people/me',
	    pageSize=10,
	    personFields='names,emailAddresses').execute()
	connections = results.get('connections', [])

	for person in connections:
	    names = person.get('names', [])
	    if names:
	        name = names[0].get('displayName')
	        print(name)