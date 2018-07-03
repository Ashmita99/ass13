#question1
import pprint
import sys
import os
import subprocess
import spotipy
import spotipy.util as util
if len(sys.argv) > 2:
username = sys.argv[1]
playlist_name = sys.argv[2]
playlist_description = sys.argv[3]
else :
print("Usage: %s username playlist-name playlist-description" %
(sys.argv[0],))
sys. exit ()
token = util.prompt_for_user_token(username)
if token:
sp = spotipy.Spotify(auth=token)
sp.trace = False
playlists = sp.user_playlist_create(username, playlist_name,
playlist_description)
pprint .pprint(playlists)
else :
print ("Can't get token for", username)


#question2
#Google : 172.217.9.164
#Facebook: 157.240.18.35

#question3
import tweepy, re, operator
from paralleldots import set_api_key, sentiment
# Authentication Consumer Key
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
# Authentication Access Tokens
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(oauth)
def get_tweet():
hash_tag = input("\nEnter the word without the hashtag")
hash_tag = "#" + hash_tag
tweets = api.search(hash_tag)
return tweets


#question4

An IDE is an integrated development environment - a suped-up text editor
with additional support for developing (such as forms designers, resource
editors, etc), compiling and debugging applications. e.g Eclipse, Visual
Studio.
A Library is a chunk of code that you can call from your own code, to help
you do things more quickly/easily. For example, a Bitmap Processing library
will provide facilities for loading and manipulating bitmap images, saving
you having to write all that code for yourself. Typically a library will only
offer one area of functionality (processing images or operating on zip files)
An API (application programming interface) is a term meaning the
functions/methods in a library that you can call to ask it to do things for you
- the interface to the library.
An SDK (software development kit) is a library or group of libraries (often
with extra tool applications, data files and sample code) that aid you in
developing code that uses a particular system (e.g. extension code for using
features of an operating system (Windows SDK), drawing 3D graphics via a
particular system (DirectX SDK), writing add-ins to extend other
applications (Office SDK), or writing code to make a device like an Arduino
or a mobile phone do what you want). An SDK will still usually have a single
focus.
A toolkit is like an SDK - it's a group of tools (and often code libraries) that
you can use to make it easier to access a device or system... Though perhapswith more focus on providing tools and applications than on just code
libraries.
A framework is a big library or group of libraries that provides many
services (rather than perhaps only one focussed ability as most
libraries/SDKs do). For example, .NET provides an application framework -
it makes it easier to use most (if not all) of the disparate services you need
(e.g. Windows, graphics, printing, communications, etc) to write a vast
range of applications - so one "library" provides support for pretty much
everything you need to do. Often a framework supplies a complete base on
which you build your own code, rather than you building an application that
consumes library code to do parts of its work.


#question5
import pprint
import sys
import os
import subprocess
import spotipy
import spotipy.util as util
if len(sys.argv) > 2:
username = sys.argv[1]
playlist_name = sys.argv[2]
playlist_description = sys.argv[3]
else :
print("Usage: %s username playlist-name playlist-description" %
(sys.argv[0],))
sys. exit ()
token = util.prompt_for_user_token(username)
if token:
sp = spotipy.Spotify(auth=token)
sp.trace = False
playlists = sp.user_playlist_create(username, playlist_name,
playlist_description)
pprint .pprint(playlists)
else :
print ("Can't get token for", username)




