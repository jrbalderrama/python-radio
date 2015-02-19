"""Radio receiver/recorder."""

import random
import sys

from player import Player
from playlist import Playlist


class Console(object):
    """Console """

    def __init__(self):
        self._playlist = Playlist.load_playlist()

    @property
    def playlist(self):
        """
        Get the list of available radio stations.
        """
        return self._playlist

    @playlist.setter
    def playlist(self, playlist):
        """
        Set the list of radio stations.
        """
        self._playlist = playlist

    def list(self):
        """
        Print the available radio stations.
        """
        for _station in self._playlist:
            print(_station)

    def search(self, description, use_keywords=False, limit=5):
        """
        Search a list of stations.
        """
        for name in self._playlist.search(description, use_keywords, limit):
            station = self._playlist.get_station(name)
            print(station)

    def shuffle(self):
        """
        Play a random station.
        """
        if self._playlist:
            station = random.choice(self._playlist)
            Player.play(station)

    def tune(self, description, use_keywords=False):
        """
        Play best matched station.
        """
        station = self._playlist.match_station(description, use_keywords)
        Player.play(station)

    def record(self, description, use_keywords=True):
        """
        Save the stream of the station 'name' to the file 'output'.
        """
        station = self._playlist.match_station(description, use_keywords)
        Player.record(station)

    def info(self, name):
        """Show detailed information about the station with name 'name'.

        :param str name:
        :returns: None

        """

        station = self._playlist.get_station(name)
        if station:
            station.get_description()
        else:
            print("\tNo references for '{}'\n".format(name), file=sys.stderr)

console = Console()

# console.list()
# console.shuffle()
# console.tune("Rai classic")
# console.tune("Rai classic", True)
# console.tune("Rai hit radio", True)
# console.search("Rai radiofd")
# console.search("Rai web", True)
# console.record("parliament")
# console.info("Rai WebRadio6")
console.info("Rai WebRadio6")

#print(console.playlist)

# import time
# import sys
#
# while True:
#     for i in range(100):
#         time.sleep(0.1)
#         #sys.stdout.write("\r%d%%" % i)
#         sys.stdout.write('\r{}'.format('.'*(i//18)))
# #    sys.stdout.flush()
#
#     for i in range(100, 0, -1):
#         time.sleep(0.1)
#     #sys.stdout.write("\r%d%%" % i)
#         sys.stdout.write('\r{}'.format(' '*((i+1)//18)))
#         sys.stdout.write('\r{}'.format('.'*(i//18)))
# #    sys.stdout.flush()
