import urllib



def app(environ, start_response):

    #data = b"Hello, World!\n"

    query_str = environ["QUERY_STRING"]

    reqs = query_str.split('&')

    reqs1 = [urllib.unquote(x) + "\n\r" for x in reqs]

    data = "".join(reqs1)

    start_response("200 OK", [

        ("Content-Type", "text/plain"),

        ("Content-Length", str(len(data)))

    ])

    return iter([data])
