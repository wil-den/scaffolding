from pathlib import Path
from ..main import bp
from flask import Response, send_from_directory
from flask.helpers import make_response

parent = Path(__file__).parent.absolute()
STATIC = parent / "static"


@bp.route('/', defaults={'path': 'index.html'})
@bp.route('/<path:path>')
def all_static_files(path) -> Response:
    resp = send_from_directory(STATIC, path, max_age=0)
    if path.endswith('.js'):
        resp.mimetype = 'text/javascript'
    elif path.endswith('.css'):
        resp.mimetype = 'text/css'
    elif path.endswith('.html'):
        resp.mimetype = 'text/html'
    return resp
    

