#!/bin/py

from instagram.client import InstagramAPI

import json

#gets access token code 
"""
api = InstagramAPI(client_id="1d8fe0ccd3424a85a80c1f70ccb1a905", client_secret="e343e0da1cdd49cc8ec9dd72ee08103d", redirect_uri="http://www.google.com")
redirect_uri = api.get_authorize_login_url(scope = ["basic"])
print redirect_uri #code=83c3c8ac43e94bf2a8365330bfdb6a15
access_token = api.exchange_code_for_access_token(83c3c8ac43e94bf2a8365330bfdb6a15) #token=
"""


#gets access token 
"""
api = InstagramAPI(client_id="1d8fe0ccd3424a85a80c1f70ccb1a905", client_secret="e343e0da1cdd49cc8ec9dd72ee08103d", redirect_uri="http://www.google.com")
redirect_uri = api.get_authorize_login_url(scope = ["basic"])
access_token = api.exchange_code_for_access_token("83c3c8ac43e94bf2a8365330bfdb6a15")
print access_token
#(u'1598175673.1d8fe0c.ed8d8da7597046deb1b432a9dcdaf6ec', {u'username': u'whaawhaa325', u'bio': u'', u'website': u'', u'profile_picture': u'https://instagramimages-a.akamaihd.net/profiles/anonymousUser.jpg', u'full_name': u'', u'id': u'1598175673'})
"""

access_token = "1598175673.1d8fe0c.ed8d8da7597046deb1b432a9dcdaf6ec"
user_info = {u'username': u'whaawhaa325', u'bio': u'', u'website': u'', u'profile_picture': u'https://instagramimages-a.akamaihd.net/profiles/anonymousUser.jpg', u'full_name': u'', u'id': u'1598175673'}

api = InstagramAPI(access_token=access_token)


resp, page = api.tag_recent_media(5, 1, "ucdavis")
print resp
for media in resp:
	print media.images['standard_resolution']

