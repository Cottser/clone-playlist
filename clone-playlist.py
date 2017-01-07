#!/usr/bin/python2
import os
import sys
import spotipy
import spotipy.util as util
import datetime
from ConfigParser import SafeConfigParser


def get_source_tracks(username, playlist_id):
  results = sp.user_playlist_tracks(username, playlist_id)
  tracks = results['items']
  track_ids = [track['track']['id'] for track in tracks]
  return track_ids


def create_playlist(playlist_type):
  pl_date = datetime.date.today().strftime('%Y-%m-%d')
  if playlist_type == 'dw':
    pl_name = 'Discover Weekly for %s'%(pl_date)
  elif playlist_type == 'tbt':
    pl_name = 'TBT for %s'%(pl_date)
  new_pl_id = sp.user_playlist_create(user, pl_name, public=False)
  return new_pl_id['id']


def add_tracks_new_playlist(new_pl_id, tracks):
  result = sp.user_playlist_add_tracks(user, new_pl_id, tracks)
  return

config_path = os.path.expanduser('~') + '/.spotify_pl.conf'
config = SafeConfigParser()
config.read(config_path)
client_id = config.get('credentials', 'id')
client_secret = config.get('credentials', 'secret')
callback_uri = config.get('credentials', 'callback_uri')
user = config.get('credentials', 'profile_uri').split('/')[4]
songs = []

if sys.argv[1] == 'dw':
  pl_user = config.get('playlists','dw_uri').split(':')[2]
  pl_id = config.get('playlists','dw_uri').split(':')[4]
elif sys.argv[1] == 'tbt':
  pl_user = config.get('playlists','tbt_uri').split(':')[2]
  pl_id = config.get('playlists','tbt_uri').split(':')[4]
else:
   print "Bad arguement! Either dw or tbt."
   sys.exit(1)

token = util.prompt_for_user_token(user, scope='playlist-modify-private', client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth=token)
created_pl_id = create_playlist(sys.argv[1])
songs = get_source_tracks(pl_user, pl_id)
add_tracks_new_playlist(created_pl_id, songs)
