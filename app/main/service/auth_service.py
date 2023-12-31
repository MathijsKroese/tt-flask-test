import json
from flask import request, jsonify, g
from six.moves.urllib.request import urlopen
from functools import wraps
from jose import jwt


AUTH0_DOMAIN = "dev-8afmu4tbz4cfhp1b.us.auth0.com"
ALGORITHMS = "RS256"


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# @app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


def get_token_auth_header():
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                         "description": "Authorization header expected"}, 401)

    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                         "description": "Authorization header must start with Bearer"}, 401)

    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                         "description": "No token found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                         "description": "Authorization must be Bearer token"}, 401)

    token = parts[1]
    return token


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience="/private",
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                 "description": "Token has expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                 "description": "Incorrect claims. Please check audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                 "description": "Unable to parse authentication token"}, 401)

            g.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                         "description": "Unable to find appropriate key"}, 401)

    return decorated


def requires_scope(required_scope):
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
        token_scopes = unverified_claims["scope"].split()
        for token_scope in token_scopes:
            if token_scope == required_scope:
                return True
    return False
