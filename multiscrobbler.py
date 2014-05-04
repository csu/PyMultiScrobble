import pylast
import time
import Private

class MultiScrobbler(object):
    def __init__(self):
        self.accounts = []

    def addUser(self, user, password):
        self.accounts.append(pylast.LastFMNetwork(api_key=Private.LASTFM_API_KEY, api_secret=Private.LASTFM_API_SECRET, username=user, password_hash=pylast.md5(password)))

    def scrobbleAll(self, artist, song):
        for user in self.accounts:
            user.scrobble(artist, song, now)