class Codec:
    mapping = dict()
    i = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        shortUrl = 'http://tinyurl.com/{}'.format(self.i)
        self.mapping[shortUrl] = longUrl
        self.i += 1
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.mapping[shortUrl]

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))