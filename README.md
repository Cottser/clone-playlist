# spotify-clone-playlist
Python script to clone Discover Weekly and/or Release Radar Spotify playlists to a personal, dated playlist.

## Prerequisites
Written against Python 2.7, it leans **HEAVILY** on the work of [Spotipy module](https://github.com/plamere/spotipy) to handle account authorization and abstraction of the Spotify API.

To install Spotipy: `pip install spotipy --upgrade`

The application needs to be registered via [My Applications](https://developer.spotify.com/my-applications/#!/applications) to obtain the needed information for the config file (commented config file is included in the repo). Note that you must enter a value in the Spotify Developer UI for the Redirect URI but it does not need to be a valid URI, the URI that is in the example config file will work fine.

## Running
The first time you run it, you will go through the OAuth authorization flow, so you should run the script via command line rather than crontab for the first run. Note: [The Spotipy documentation](http://spotipy.readthedocs.org/en/latest/#authorized-requests) has a description of the OAuth process to get a token.

Run from cron with the following syntax (timing in the examples is roughly based on EST):

```
00 5 * * mon ~/bin/spotify-clone-playlist/clone-playlist.py dw
00 5 * * fri ~/bin/spotify-clone-playlist/clone-playlist.py rr
```
