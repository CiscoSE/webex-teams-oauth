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

# _config.py - configuration file

CLIENT_ID = ''        #Copy the Client ID from your integration here
CLIENT_SECRET = ''    #Copy the Client Secret from your integration here
AUTHORIZATION_BASE_URL = 'https://api.ciscospark.com/v1/authorize'
TOKEN_URL = 'https://api.ciscospark.com/v1/access_token'
SCOPE = 'spark:all'
REDIRECT_URI = 'https://xxxxxxxx.ngrok.io/callback' # replace xxxxxxxx with ngrok random 
												    # generated part of the domain name
												    # i.e. https://1a2b3c4d.ngrok.io/callback
