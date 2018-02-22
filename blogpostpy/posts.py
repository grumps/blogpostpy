import json


CREATE_POST_SQL = """
INSERT INTO posts (title, body)
VALUES (:title, :body);
""".strip()

GET_POSTS_SQL = """
SELECT * FROM posts;
""".strip()


def get_posts(session):
    return session.execute(GET_POSTS_SQL).fetchall()


def create_post(session, title, body):
    return session.execute(CREATE_POST_SQL, {'title': title, 'body': body})


class GetPostResource(object):
    def on_get(self, req, resp):
        # run query
        # return response array
        resp.body = 'OK'


class CreatePostResource(object):
    def on_post(self, req, resp):
        # check title
        # check body
        # response
        resp.body = 'OK'

