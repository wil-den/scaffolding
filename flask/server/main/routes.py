from ..main import bp
from flask.helpers import make_response

@bp.get("/")
@bp.get("/index")
def index():
    return make_response("Hi!")