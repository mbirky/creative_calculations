'''
The creative calculations website.

The index page will be the latest post and a user can find a specific post by
specifiging the post name
'''

import sys
from os import listdir

from flask import Flask, abort, send_file, render_template
app = Flask(__name__) # pylint: disable=invalid-name

POSTS_DIR = 'creative_calculations/posts/'

def render_blog_post(post_name):
    '''
    Reads the blog post file and passes the the variables to the template
    before returning the rendered template.
    '''
    with open(f'{POSTS_DIR}{post_name}', 'r') as file:
        title = file.readline()
        paragraphs = []
        paragraph = file.readline()
        while paragraph:
            paragraphs.append(paragraph)
            paragraph = file.readline()
    posts = [post for post in listdir(POSTS_DIR) if post != post_name]
    return render_template('blog_post.html', title=title, paragraphs=paragraphs, posts=posts)

@app.route('/')
def index():
    ''' This will point to the latest post '''
    return render_blog_post('helloworld')

@app.route('/<post_name>')
def post(post_name):
    ''' Returns the post with the specified name '''
    if post_name not in listdir(POSTS_DIR):
        abort(404)
    return render_blog_post(post_name)

@app.errorhandler(404)
def page_not_found(error): # pylint: disable=unused-argument
    ''' Default for 404 Errors '''
    return "404: Not all who wander are lost, but you are.", 404
