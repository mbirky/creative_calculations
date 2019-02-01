"""
The creative calculations website.

The index page will be the latest post and a user can find a specific post by
specifiging the post name
"""

import sys
from os import listdir

from flask import Flask, abort, send_file, render_template

APP = Flask(__name__)

POSTS_DIR = "creative_calculations/templates/posts/"

FORMAT_POST = lambda post: " ".join([name.capitalize() for name in post.split("_")])


def render_blog_post(post_name):
    """
    Reads the title and paragraphs from the blog post file, collects the other
    posts, and then passes the variables to the template before returning the
    rendered template.
    """
    posts = [post[:-5] for post in listdir(POSTS_DIR) if post != f"{post_name}.html"]
    return render_template(
        "blog_post.html", post_name=post_name, posts=posts, format_post=FORMAT_POST
    )


@APP.route("/")
def index():
    """ This will point to the latest post """
    return render_blog_post("hello_world")


@APP.route("/<post_name>")
def post(post_name):
    """ Returns the post with the specified name """
    if f"{post_name}.html" not in listdir(POSTS_DIR):
        abort(404)
    return render_blog_post(post_name)


@APP.errorhandler(404)
def page_not_found(error):  # pylint: disable=unused-argument
    """ Default for 404 Errors """
    return "404: Not all who wander are lost, but you are.", 404
