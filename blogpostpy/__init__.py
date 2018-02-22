import sqlite3

import falcon

from blogpostpy import posts

# TODO this wont survive packaing
_db_con = sqlite3.connect('blog.db')

class DBCursor(object):
    """database connection"""

    def process_resource(self, req, resp, resource, params):
        """attach db connection for routed requests"""
        req.session = _db_con

app = falcon.API(middleware=DBCursor())
app.add_route('/posts', posts.GetPostResource())
app.add_route('/post', posts.CreatePostResource()) 
