import json

import falcon


CREATE_POST_SQL = """
INSERT INTO posts (title, body)
VALUES (:title, :body);
""".strip()

POST_FIELDS = ('post_id', 'title', 'body')
GET_POSTS_SQL = """
SELECT post_id, title, body FROM posts;
""".strip()


def get_posts(session):
    rows = session.execute(GET_POSTS_SQL).fetchall()
    return [dict(zip(POST_FIELDS, r)) for r in rows]


def create_post(session, title, body):
    return session.execute(CREATE_POST_SQL, {'title': title, 'body': body})


class GetPostResource(object):
    def on_get(self, req, resp):
        results = get_posts(req.session)
        resp.body = json.dumps(results)


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
