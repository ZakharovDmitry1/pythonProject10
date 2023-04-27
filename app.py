import os

from waitress import serve

from app import app
from app.data import db_session


def main():
    db_session.global_init("app/db/blogs.db")
    port = int(os.environ.get("PORT", 5000))
    serve(app, port=port, host='0.0.0.0')


if __name__ == '__main__':
    main()

