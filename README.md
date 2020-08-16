# clone-playlist
Python program to clone Discover Weekly and/or Release Radar Spotify playlists to a personal, dated playlist.

## Prerequisites
Written against Python 2.7, it leans **HEAVILY** on the work of [Spotipy module](https://github.com/plamere/spotipy) to handle account authorization and abstraction of the Spotify API. The description of the OAuth process to get a token resides in the [Spotipy documentation](http://spotipy.readthedocs.org/en/latest/#authorized-requests).  The application needs to be registered via [My Applications](https://developer.spotify.com/my-applications/#!/applications) to obtain the needed information for the config file (commented file is included in the repo).


## Running
Run from cron with the following syntax:

00 7 * * mon /opt/clone-playlist/clone-playlist.py dw

00 9 * * fri /opt/clone-playlist/clone-playlist.py rr
