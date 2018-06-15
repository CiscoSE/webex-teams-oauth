# _config.py - configuration file

CLIENT_ID = 'Cc22c6e7c21513b47bb9a96557fbdd6c29c9bd4a3308cd6198af26ea81047234d'        #Copy the Client ID from your integration here
CLIENT_SECRET = 'b34f86dbe4a33eb9f2157f83949da9625ff0f4bb0e9d9288a0db39c2b9caa8ee'    #Copy the Client Secret from your integration here
AUTHORIZATION_BASE_URL = 'https://api.ciscospark.com/v1/authorize'
TOKEN_URL = 'https://api.ciscospark.com/v1/access_token'
SCOPE = 'spark:all'
REDIRECT_URI = 'https://06e2b743.ngrok.io/callback' # replace xxxxxxxx with ngrok random 
												    # generated part of the domain name
												    # i.e. https://1a2b3c4d.ngrok.io/callback
