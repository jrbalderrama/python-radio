# -*- coding: utf-8 -*-
"""Player class and utilitary functions.

"""
from datetime import datetime


class Player(object):
    """Station player

    """

    @staticmethod
    def play(station):
        """Play an station.

        :param Station station:
        :returns: None

        """
        print('\tPlaying {}'.format(station.name))

    @staticmethod
    def record(station):
        """Record the stream of an station.

        :param Station station:
        :returns: None

        """
        print('\tRipping {}'.format(create_segment_filename(station.name)))


def create_segment_filename(station_name):
    """Create a radio programme segment name at current time.

    :param str station_name:
    :returns:
    :rtype: def

    """
    time = datetime.today()
    return '{}_{}.mp3'.format(''.join(x for x in station_name if x.isalnum()),
                              time.strftime('%d%m%y-%H%M'))
