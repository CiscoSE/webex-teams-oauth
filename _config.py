# _config.py - configuration file

CLIENT_ID = ''        #Copy the Client ID from your integration here
CLIENT_SECRET = ''    #Copy the Client Secret from your integration here
AUTHORIZATION_BASE_URL = 'https://api.ciscospark.com/v1/authorize'
TOKEN_URL = 'https://api.ciscospark.com/v1/access_token'
SCOPE = 'spark:all'
REDIRECT_URI = 'https://xxxxxxxx.ngrok.io/callback' # replace xxxxxxxx with ngrok random 
												    # generated part of the domain name
												    # i.e. https://1a2b3c4d.ngrok.io/callback
