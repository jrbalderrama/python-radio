from datetime import datetime

class Player(object):

    @staticmethod
    def play(station):
        """
        Play an station.
        """
        print("\tPlaying {}".format(station.name))

    @staticmethod
    def record(station):
        """
        Record the stream of an station.
        """
        time = datetime.today()
        file = ''.join(c for c in station.name if c.isalnum()) + '_' + \
               time.strftime("%d%m%y-%H%M") + '.mp3'

        print("\tRipping {} at {}".format(station.name, file))
