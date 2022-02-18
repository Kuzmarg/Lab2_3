import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_data():
    acct = input('Insert the username: ')
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    try:
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        return data
    except urllib.error.HTTPError:
        print('The nickname is wrong. Check it or try later.')
        return get_data()
