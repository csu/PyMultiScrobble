import pylast
import time
import Private

class MultiScrobbler(object):
    def __init__(self):
        self.accounts = []

    def addAccount(self, user, password):
        password = pylast.md5(password)
        network = pylast.LastFMNetwork(api_key=Private.LASTFM_API_KEY, api_secret=Private.LASTFM_API_SECRET, username=user, password_hash=password)
        # print 'added user: ' + str(network)
        self.accounts.append(network)

    def scrobbleAll(self, artist, song):
        now = int(time.time())
        for user in self.accounts:
            # print 'scrobbling: ' + artist + ' ' + song + ' to ' + str(user)
            user.scrobble(artist, song, now)