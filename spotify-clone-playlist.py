#!/usr/bin/python2
import os
import sys
import spotipy
import spotipy.util as util
import datetime
from spotipy.oauth2 import SpotifyOAuth
from ConfigParser import SafeConfigParser

scope = 'playlist-modify-private'

def _filter_tracks(track):
  if track['track'] is not None:
    return True
  else:
    return False

def get_source_tracks(playlist_id):
  results = sp.playlist_tracks(playlist_id)
  tracks = results['items']

  filtered_tracks = filter(_filter_tracks, tracks)
  track_ids = [track['track']['id'] for track in filtered_tracks]
  return track_ids


def create_playlist(playlist_type):
  pl_date = datetime.date.today().strftime('%Y-%m-%d')
  if playlist_type == 'dw':
    pl_name = '[] Discover %s'%(pl_date)
  elif playlist_type == 'rr':
    pl_name = '[] Release %s'%(pl_date)
  new_pl_id = sp.user_playlist_create(user, pl_name, public=False)
  return new_pl_id['id']


def add_tracks_new_playlist(new_pl_id, tracks):
  result = sp.user_playlist_add_tracks(user, new_pl_id, tracks)
  return

config_path = os.path.expanduser('~') + '/.config/spotify-clone-playlist.conf'
config = SafeConfigParser()
config.read(config_path)
client_id = config.get('credentials', 'id')
client_secret = config.get('credentials', 'secret')
callback_uri = config.get('credentials', 'callback_uri')
user = config.get('credentials', 'profile_uri').split(':')[2]
cache_path = os.path.expanduser('~') + '/.cache-' + user
songs = []

if sys.argv[1] == 'dw':
  pl_id = config.get('playlists','dw_uri')
elif sys.argv[1] == 'rr':
  pl_id = config.get('playlists','rr_uri')
else:
   print "Bad arguement! Either dw or rr."
   sys.exit(1)

auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=callback_uri, username=user, cache_path=cache_path)
sp = spotipy.Spotify(auth_manager=auth_manager)
created_pl_id = create_playlist(sys.argv[1])
songs = get_source_tracks(pl_id)
add_tracks_new_playlist(created_pl_id, songs)
