Title: SSL EOF Error
Date: 2014-10-15 10:20
Category: Python
Tags: SSL, poodle
Slug: ssl-eof-error
Author: Will Ogden
Summary: Suddenly getting c504 EOF SSL errors using Python 2.7?

###TL;DR

Our ([TrustedHousesitters.com](www.trustedhousesitters.com)) integration with the Mailchimp API (via Requests and [Mailsnake](https://github.com/michaelhelmick/python-mailsnake)) stopped working with the following error occurring on all https requests:

    _ssl.c:504: EOF occurred in violation of protocol

Although not confirmed from Mailchimp yet, it looks like this might be related to them (or someone upstream) mitigating the Poodle SSL vulnerability. The fix (for us) was to patch the python ssl module to force the use TLS1.0. [Code below source](http://stackoverflow.com/questions/14102416/python-requests-requests-exceptions-sslerror-errno-8-ssl-c504-eof-occurred):

    import ssl
    from functools import wraps
    def sslwrap(func):
        @wraps(func)
        def bar(*args, **kw):
            kw['ssl_version'] = ssl.PROTOCOL_TLSv1
            return func(*args, **kw)
        return bar

    ssl.wrap_socket = sslwrap(ssl.wrap_socket)

###Background

Another week, another SSL vulnerability. ["Poodle"](https://www.openssl.org/~bodo/ssl-poodle.pdf) as it's known affects SSL 3.0. There is no specific patch, instead removing SSL 3.0 support from your webserver is the recommended approach [good blog post here on this](https://scotthelme.co.uk/sslv3-goes-to-the-dogs-poodle-kills-off-protocol/). As the sysadmins the world over start pulling out v3.00 support, any clients reliant on this are going to have problems...old IE6 being one of the bigger ones. From our experience over the last day or two, it seems that Python clients could also be affected.

As mentioned above we leverage the Mailchimp API fairly heavily. We suddenly began getting SSL errors (interestingly we couldn't reproduce on MacOS, leading us to think it the issue was in the openssl implementation). Digging deeper we found information to suggest that by default Python will try and connect using SSLv2/v3. When we patched the Python ssl module to always use TLS1.0 the error stopped. So guessing there is an issue in the handshaking somewhere.  
