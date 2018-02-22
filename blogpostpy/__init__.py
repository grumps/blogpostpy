import sqlite3
import os

import falcon

from blogpostpy import posts

path, file_name = os.path.split(__file__)
_db_con = sqlite3.connect(os.path.join(path, 'blog.db'))

class DBCursor(object):
    """database connection"""

    def process_resource(self, req, resp, resource, params):
        """attach db connection for routed requests"""
        req.session = _db_con

app = falcon.API(middleware=DBCursor())
app.add_route('/posts', posts.GetPostResource())
app.add_route('/post', posts.CreatePostResource()) 
