"""Radio receiver/recorder."""

import random

from player import Player
from playlist import Playlist
from station import Station


class Console(object):
    """Console """

    @staticmethod
    def cap(string, length):
        """
        Cap a 'string' to a certain 'length', if 'length' is exceeded appending
        dots (...) after it.
        """
        return string if len(string) <= length else string[0:length-3] + '...'

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
            if _station.website:
                print("\t{:{}} {}".format(self.cap(_station.name, 25),
                                          25, _station.website))
            else:
                print("\t{}".format(_station.name))

    def search(self, description, use_keywords=False, limit=5):
        """
        Search a list of stations.
        """
        for name in reversed(self._playlist.search(description, use_keywords, limit)):
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
        # str.lower
        station = self._playlist.match_station(description, use_keywords)
        Player.play(station)

    def record(self, description, use_keywords=True):
        """
        Save the stream of the station 'name' to the file 'output'.
        """
        station = self._playlist.match_station(description, use_keywords)
        Player.record(station)

#console = Console()
#
# #console.list()
# #console.shuffle()
# console.tune("Rai classic")
# console.tune("Rai classic", True)
# console.search("Rai Radio")
# console.search("Rai Radio", True)
#console.record("parliament")

# print(console.playlist)
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
#
#
#
# from station import Station
#
# r = Station("radio NRJ the best BBC this is a really long name for a radio", "http://pluzz.tvfrance.fr/radio", None, ":music:news")
# s = Station("station", "http://www.google.com/radio")
#
# f = Station("Frequence ONE", "http://one.ie/An", None, ":pop:hiphop:electro")
#
# playlist = Playlist()
# playlist.add_station(f)
# playlist.add_station(s)
# playlist.add_station(f)
#
# console = Console()
# console.playlist = playlist
# console.list()
#
# console.shuffle()
