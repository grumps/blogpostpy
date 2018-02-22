import sqlite3

import falcon

from blogpostpy import posts

# TODO this wont survive packaing
_db_con = sqlite3.connect('blog.db')

class DBCursor(object):
    """cursor middleware"""

    def process_resource(self, req, resp, resource, params):
        """cursor routed routed requests"""
        req.session = _db_con.cursor()

    def process_response(self, req, resp, resource, req_succeeded):
        """close the session on the way out if a cursor was created"""
        if req.session:
            req.session.close()

app = falcon.API(middleware=DBCursor())
app.add_route('/posts', posts.GetPostResource())
app.add_route('/post', posts.CreatePostResource()) 
