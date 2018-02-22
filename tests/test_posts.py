# Sample Test passing with nose and pytest
from falcon import testing
import pytest

import blogpostpy

@pytest.fixture()
def client():
    return testing.TestClient(blogpostpy.app)

def test_get_posts(client):
    result = client.simulate_get('/posts')
    # we get an "array" back
    assert type(result.json) == list
    # we get object with id, title, body
    assert ('id', 'title', 'body') == result.json()[0].keys()
    
def test_create_post(client):
    post_msg = {u'title': u'Double Under', u'body': u'Magic Methods'}
    result = client.simulate_post('/post', json=post_msg)
    assert result.status == '201 Created'

