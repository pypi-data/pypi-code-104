__all__ = ()

from ..utils import IgnoreCaseString

METHOD_ANY = '*'
METHOD_CONNECT = 'CONNECT'
METHOD_HEAD = 'HEAD'
METHOD_GET = 'GET'
METHOD_DELETE = 'DELETE'
METHOD_OPTIONS = 'OPTIONS'
METHOD_PATCH = 'PATCH'
METHOD_POST = 'POST'
METHOD_PUT = 'PUT'
METHOD_TRACE = 'TRACE'

METHOD_GET_ALL = frozenset((METHOD_GET, METHOD_HEAD, METHOD_OPTIONS))
METHOD_POST_ALL = frozenset((METHOD_PATCH, METHOD_POST, METHOD_PUT))

METHOD_ALL = frozenset((METHOD_CONNECT, METHOD_HEAD, METHOD_GET, METHOD_DELETE, METHOD_OPTIONS, METHOD_PATCH,
    METHOD_POST, METHOD_PUT, METHOD_TRACE))


ACCEPT = IgnoreCaseString('Accept')
ACCEPT_CHARSET = IgnoreCaseString('Accept-Charset')
ACCEPT_ENCODING = IgnoreCaseString('Accept-Encoding')
ACCEPT_LANGUAGE = IgnoreCaseString('Accept-Language')
ACCEPT_RANGES = IgnoreCaseString('Accept-Ranges')
ACCESS_CONTROL_MAX_AGE = IgnoreCaseString('Access-Control-Max-Age')
ACCESS_CONTROL_ALLOW_CREDENTIALS = IgnoreCaseString('Access-Control-Allow-Credentials')
ACCESS_CONTROL_ALLOW_HEADERS = IgnoreCaseString('Access-Control-Allow-Headers')
ACCESS_CONTROL_ALLOW_METHODS = IgnoreCaseString('Access-Control-Allow-Methods')
ACCESS_CONTROL_ALLOW_ORIGIN = IgnoreCaseString('Access-Control-Allow-Origin')
ACCESS_CONTROL_EXPOSE_HEADERS = IgnoreCaseString('Access-Control-Expose-Headers')
ACCESS_CONTROL_REQUEST_HEADERS = IgnoreCaseString('Access-Control-Request-Headers')
ACCESS_CONTROL_REQUEST_METHOD = IgnoreCaseString('Access-Control-Request-Method')
AGE = IgnoreCaseString('Age')
ALLOW = IgnoreCaseString('Allow')
AUTHORIZATION = IgnoreCaseString('Authorization')
CACHE_CONTROL = IgnoreCaseString('Cache-Control')
CONNECTION = IgnoreCaseString('Connection')
CONTENT_DISPOSITION = IgnoreCaseString('Content-Disposition')
CONTENT_ENCODING = IgnoreCaseString('Content-Encoding')
CONTENT_LANGUAGE = IgnoreCaseString('Content-Language')
CONTENT_LENGTH = IgnoreCaseString('Content-Length')
CONTENT_LOCATION = IgnoreCaseString('Content-Location')
CONTENT_MD5 = IgnoreCaseString('Content-MD5')
CONTENT_RANGE = IgnoreCaseString('Content-Range')
CONTENT_TRANSFER_ENCODING = IgnoreCaseString('Content-Transfer-Encoding')
CONTENT_TYPE = IgnoreCaseString('Content-Type')
COOKIE = IgnoreCaseString('Cookie')
DATE = IgnoreCaseString('Date')
DESTINATION = IgnoreCaseString('Destination')
DIGEST = IgnoreCaseString('Digest')
ETAG = IgnoreCaseString('Etag')
EXPECT = IgnoreCaseString('Expect')
EXPIRES = IgnoreCaseString('Expires')
FORWARDED = IgnoreCaseString('Forwarded')
FROM = IgnoreCaseString('From')
HOST = IgnoreCaseString('Host')
IF_MATCH = IgnoreCaseString('If-Match')
IF_MODIFIED_SINCE = IgnoreCaseString('If-Modified-Since')
IF_NONE_MATCH = IgnoreCaseString('If-None-Match')
IF_RANGE = IgnoreCaseString('If-Range')
IF_UNMODIFIED_SINCE = IgnoreCaseString('If-Unmodified-Since')
KEEP_ALIVE = IgnoreCaseString('Keep-Alive')
LAST_EVENT_ID = IgnoreCaseString('Last-Event-ID')
LAST_MODIFIED = IgnoreCaseString('Last-Modified')
LINK = IgnoreCaseString('Link')
LOCATION = IgnoreCaseString('Location')
MAX_FORWARDS = IgnoreCaseString('Max-Forwards')
ORIGIN = IgnoreCaseString('Origin')
PRAGMA = IgnoreCaseString('Pragma')
PROXY_AUTHENTICATE = IgnoreCaseString('Proxy-Authenticate')
PROXY_AUTHORIZATION = IgnoreCaseString('Proxy-Authorization')
RANGE = IgnoreCaseString('Range')
REFERER = IgnoreCaseString('Referer')
RETRY_AFTER = IgnoreCaseString('Retry-After')
SEC_WEBSOCKET_ACCEPT = IgnoreCaseString('Sec-WebSocket-Accept')
SEC_WEBSOCKET_VERSION = IgnoreCaseString('Sec-WebSocket-Version')
SEC_WEBSOCKET_PROTOCOL = IgnoreCaseString('Sec-WebSocket-Protocol')
SEC_WEBSOCKET_EXTENSIONS = IgnoreCaseString('Sec-WebSocket-Extensions')
SEC_WEBSOCKET_KEY = IgnoreCaseString('Sec-WebSocket-Key')
SEC_WEBSOCKET_KEY1 = IgnoreCaseString('Sec-WebSocket-Key1')
SERVER = IgnoreCaseString('Server')
SET_COOKIE = IgnoreCaseString('Set-Cookie')
TE = IgnoreCaseString('TE')
TRAILER = IgnoreCaseString('Trailer')
TRANSFER_ENCODING = IgnoreCaseString('Transfer-Encoding')
UPGRADE = IgnoreCaseString('Upgrade')
WEBSOCKET = IgnoreCaseString('WebSocket')
URI = IgnoreCaseString('URI')
USER_AGENT = IgnoreCaseString('User-Agent')
VARY = IgnoreCaseString('Vary')
VIA = IgnoreCaseString('Via')
WANT_DIGEST = IgnoreCaseString('Want-Digest')
WARNING = IgnoreCaseString('Warning')
WWW_AUTHENTICATE = IgnoreCaseString('WWW-Authenticate')
X_FORWARDED_FOR = IgnoreCaseString('X-Forwarded-For')
X_FORWARDED_HOST = IgnoreCaseString('X-Forwarded-Host')
X_FORWARDED_PROTO = IgnoreCaseString('X-Forwarded-Proto')
