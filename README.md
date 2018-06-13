# Webex Teams integration using OAuthlib authentication
A simple python Flask application that uses the Webex Teams OAuth 2 authentication flow to log in a user and return the last 10 active spaces the user is in.

## How to setup the application
1. Install [ngrok](https://ngrok.com/) to expose the Flask application

2. Open a new console window and start ngrok to expose port 5000 of your local machine to the internet

```
ngrok http 5000
```

3. Configure a new integration from the [Cisco Webex for Developers](https://developer.webex.com/add-integration.html) integration creation page
* Enter the name of your integration
* Enter a contact email
* Pick an icon
* Give your integration a description
* Enter the Redirect_URI
	
	Use the ngrok https forwarding uri and append /callback to the end

	ex. https://fh47sk3u.ngrok.io/callback

	**Note:**
	_You will need this Redirect_URI for the application setup later._
	_If you close ngrok and start it again the random https URI will change and you will have modify it in the integration._

* Select the **spark:all** scope
* Click the "Create Integration" button

4. After the integration is created save the **Client ID** and **Client Secret** somewhere secure for later use in the Flask app configuration
	
	The **Client Secret** will only be shown once so please copy and keep it safe! You can always regenerate it, but you will not 	see this one again.

5. Clone the repository and setup the application environment
	From a bash shell:

```
git clone https://github.com/CiscoSE/teams-oauth-flask
cd teams-oauth-flask
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
```

6. Edit the _config.py file to add the Client ID, Client Secret and Redirect_URI

```
CLIENT_ID = ''        #Copy the Client ID from your integration here
CLIENT_SECRET = ''    #Copy the Client Secret from your integration here
AUTHORIZATION_BASE_URL = 'https://api.ciscospark.com/v1/authorize'
TOKEN_URL = 'https://api.ciscospark.com/v1/access_token'
SCOPE = 'spark:all'
REDIRECT_URI = 'https://<ngrok https URI>/callback'   #Copy your active ngrok https URI + /callback
```

## How to run
From a bash shell:

```
python3 oauth.py
```

## How to test

1. Open a browser and go to your active ngrok https URI
	
	ex. https://fh47sk3u.ngrok.io

	You should be redirected to the Webex Teams authentication page and upon successful login a list of the last 10 active spaces should be displayed