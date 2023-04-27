import flask

from . import db_session
from .posts import Posts

blueprint = flask.Blueprint(
    'posts_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/posts')
def get_news():
    return "Обработчик в news_api"