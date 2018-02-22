import json

import falcon


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

    def validate(self, body):
        allowed_keys = ('title', 'body')
        for k, v in body.items():
            if k in allowed_keys and isinstance(v, str):
                continue
            else:
                raise falcon.HTTPBadRequest('Invalid JSON Object')

    def on_post(self, req, resp):
        body = json.load(req.bounded_stream)
        self.validate(body)
        create_post(req.session, body['title'], body['body'])
        req.session.commit()
        resp.status = falcon.HTTP_CREATED
