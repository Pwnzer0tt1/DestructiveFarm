from functools import wraps
from flask import request, Response

from server import reloader

def authenticate():
    return Response(
        'Could not verify your access level for that URL. '
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        config = reloader.get_config()
        if "SERVER_PASSWORD" not in config or config["SERVER_PASSWORD"] is None:
            return f(*args, **kwargs)
        if auth is None or auth.password != config['SERVER_PASSWORD']:
            return authenticate()
        return f(*args, **kwargs)
    return decorated


def api_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        config = reloader.get_config()
        if "API_TOKEN" not in config or config["API_TOKEN"] is None:
            return f(*args, **kwargs)
        if request.headers.get('X-Token', '') != config['API_TOKEN']:
            return Response('Provided token is invalid.', 403)
        return f(*args, **kwargs)
    return decorated

