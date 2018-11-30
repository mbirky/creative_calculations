'''
The creative calculations website.

The index page will be the latest post and a user can find a specific post by
specifiging the post name
'''

from flask import Flask, abort, send_file
app = Flask(__name__) # pylint: disable=invalid-name

@app.route('/')
def index():
    ''' This will point to the latest post '''
    return send_file('posts/helloworld.html')

@app.route('/<post_name>')
def post(post_name):
    ''' Returns the post with the specified name '''
    return f'{post_name}'

@app.errorhandler(404)
def page_not_found(error): # pylint: disable=unused-argument
    ''' Default for 404 Errors '''
    return "404: Not all who wander are lost, but you are.", 404
