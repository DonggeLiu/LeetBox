"""
Question:
https://leetcode.com/problems/encode-and-decode-tinyurl/description/
"""


class Codec:
    """
    Although one dictionary is sufficient and more straightforward,
    having two dictionaries will allow much faster bidirectional lookups
    """
    _long_dict = {}
    _short_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if self._long_dict.get(longUrl):
            return
        
        key = len(self._short_dict)+1
        self._long_dict[longUrl] = key
        self._short_dict[key] = longUrl
        return key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self._short_dict.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
