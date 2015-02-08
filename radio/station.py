"""Radio station."""
from urllib.parse import urlparse


class Station(object):
    """
    Radio station.
    """
    def __init__(self, name, stream,
                 website=None, genre=None, keywords=None):
        self._name = name
        self._stream = stream
        self._website = website
        self._genre = genre
        self._keywords = keywords

    def __eq__(self, other):
        separator = '/'
        s_url = urlparse(self._stream)
        o_url = urlparse(other.stream)
        netloc_p = s_url.netloc == o_url.netloc
        path_p = s_url.path.rstrip(separator) == o_url.path.rstrip(separator)
        query_p = s_url.query == o_url.query
        return netloc_p and path_p and query_p

    def __str__(self):
        return self._name

    def __repr__(self):
        return "<{}.{} object with name '{}'>".format(self.__class__.__module__,
                                                      self.__class__.__name__,
                                                      self._name)

    @property
    def name(self):
        """
        Station name.
        """
        return self._name

    @property
    def stream(self):
        """
        Station URL stream.
        """
        return self._stream

    @property
    def website(self):
        """
        Station URL Web site.
        """
        return self._website

    @property
    def keywords(self):
        """
        Station keywords.
        """
        return self._keywords

    @property
    def genre(self):
        """
        Station programming format.
        """
        return self._genre
