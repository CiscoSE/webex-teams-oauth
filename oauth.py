#!/usr/bin/env python3

"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template
from webexteamssdk import WebexTeamsAPI
from _config import *
import os

"""
requests_oauthlib requires secure transport.
Insecure transport is enabled here for this test environment.
Do not use insecure transport in production
"""

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# os.environ['DEBUG'] = '1'

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def login():

    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Webex Teams)
    using a URL with a few key OAuth parameters.
    """
    
    teams = OAuth2Session(CLIENT_ID, scope=SCOPE, redirect_uri=REDIRECT_URI)
    authorization_url, state = teams.authorization_url(AUTHORIZATION_BASE_URL)

    # State is used to prevent CSRF, keep this for later.
    
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/callback", methods=["GET"])
def callback():

    """
    Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """

    auth_code = OAuth2Session(CLIENT_ID, state=session['oauth_state'], redirect_uri=REDIRECT_URI)
    token = auth_code.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET,
                               authorization_response=request.url)
    
    """
    At this point you can fetch protected resources but lets save
    the token and show how this is done from a persisted token
    """

    session['oauth_token'] = token
    return redirect(url_for('.rooms'))

@app.route("/rooms", methods=["GET"])
def rooms():

    # Use returned token to make Teams API for list of spaces

    teams_token = session['oauth_token']
    api = WebexTeamsAPI(access_token=teams_token['access_token'])
    rooms = api.rooms.list(sortBy='lastactivity')
    return render_template('rooms.html', rooms=rooms)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
