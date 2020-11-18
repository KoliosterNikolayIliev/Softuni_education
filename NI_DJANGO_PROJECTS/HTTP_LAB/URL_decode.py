from urllib.parse import *


def decode_url(urls):
    encoded = []
    for i in urls:
        encoded.append(unquote(i))
    return encoded


decoded_urls = ['http://www.google.bg/search?q=C%23',
                'https://mysite.com/show?n%40m3= p3%24h0',
                'http://url-decoder.com/i%23de%25?id=23',
                ]

[print(x) for x in decode_url(decoded_urls)]
