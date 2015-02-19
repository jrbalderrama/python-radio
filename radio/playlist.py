"""
Play-list of radio stations.
"""
import bintrees
import configparser
import operator
import pkg_resources
import sys

from collections import OrderedDict
from fuzzywuzzy import process

from station import Station


class Playlist(object):
    """
    Play-list.
    """

    @staticmethod
    def load_playlist(resource='radios.ini'):
        """
        Initialise the radio station play list.
        """
        config = configparser.ConfigParser(allow_no_value=True)
        default_resource = pkg_resources.resource_filename(__name__, resource)
        default_file = open(default_resource)
        config.read_file(default_file)

        #config.read(config, encoding='utf-8')
        playlist = Playlist()
        for section in config.sections():
            items = dict(config.items(section))
            station = Station(section,
                              items.get('stream'),
                              items.get('website'),
                              items.get('format'),
                              items.get('keywords'))
            playlist.add_station(station)
        return playlist

    def __init__(self):
        self._stations = list()

    # def __iter__(self):
    #     for station in self._stations:
    #         yield station

    # required to support indexing
    def __getitem__(self, index):
        return self._stations[index]

    # # required to support random.choice()
    def __len__(self):
        return len(self._stations)

    def __str__(self):
        return repr(self._stations)

    @property
    def stations(self):
        return self._stations

    @stations.setter
    def stations(self, value):
        self._stations = value

    def match_station(self, description, use_keywords):
        """Match the 'description' with a station of the play-list.

        The matching uses a fuzzy method.

        """
        list_names = (x.name for x in self._stations)
        best_by_name = (process.extractOne(description, list_names))

        tree_matches = bintrees.AVLTree()
        tree_matches.insert(best_by_name[0], best_by_name[1])

        if use_keywords:
            _dict_keywords = dict((x.name, x.keywords) for x in self._stations)
            # ordered dictionary by station keywords
            dict_keywords = OrderedDict(sorted(_dict_keywords.items(),
                                               key=operator.itemgetter(0)))
            # best match (score included) by keywords
            tuple_keywords = process.extractOne(description,
                                                dict_keywords.values())
            # index of best by keywords in ordered dictionary
            index = list(dict_keywords.values()).index(tuple_keywords[0])
            tree_matches.insert(list(dict_keywords.keys())[index],
                                tuple_keywords[1])

            _dict_genre = dict((x.name, x.genre) for x in self._stations)
            # ordered dictionary by station name
            dict_genre = OrderedDict(sorted(_dict_genre.items(),
                                            key=operator.itemgetter(0)))
            # best match (score included) by genre
            tuple_genre = process.extractOne(description, dict_genre.values())
            # index of best by genre in ordered dictionary
            index = list(dict_genre.values()).index(tuple_genre[0])
            tree_matches.insert(list(dict_genre.keys())[index],
                                tuple_genre[1])

        # print(OrderedDict(sorted(tree_matches.iter_items(),
        #                          key=operator.itemgetter(1))))#).popitem()[0]

        bests = sorted(tree_matches.iter_items(), key=operator.itemgetter(1))
        return self.get_station(bests[-1][0])

    def search(self, description, use_keywords, limit):
        """
        Search stations matching a 'description'. Number of results is defined
        by the 'limit'.
        """
        names = (x.name for x in self._stations)
        matches_by_name = process.extract(description, names, limit=limit)

        tree_matches = bintrees.AVLTree(matches_by_name)
        print(tree_matches)

        result = sorted(tree_matches.iter_items(), key=operator.itemgetter(1),
                        reverse=True)[0:limit:]

        return (x[0] for x in result)

        # best_matches.extend(matches_by_name)
        #
        # #best_matches.extend(matches_by_name)
        # #print(best_matches)
        #
        # sorted_matches = sorted(best_matches, key=operator.itemgetter(1))
        # #print(deque(sorted_matches))
        # # return list without duplicates
        # return list(OrderedDict(sorted_matches).keys())

    def add_station(self, station):
        """
        Add a 'station' to the pl
        ay-list if it does not exist.
        """
        index = None
        try:
            index = self._stations.index(station)
        except ValueError:
            self._stations.append(station)
        finally:
            if index:
                print("'{}' exists as '{}'".format(station.name,
                                                   self._stations[index].name),
                      file=sys.stderr)

    def get_station(self, name):
        """
        Retrieve the station with associated to 'name' from the play-list.
        """
        return next((x for x in self._stations if x.name == name), None)

    # def merge(self, stations):
    #     """
    #     Merge the 'stations' to the play-list removing duplicates.
    #     """
    #     self._stations += [station for station in stations
    #                        if station not in self._stations]
