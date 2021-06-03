
def application(env, start_response):
    start_response('200 OkkK', [('Content-Type', 'text/html')])
    return [b"uWSGI Test..."]
