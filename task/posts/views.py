from task.models import Post
from flask import render_template
def get_posts():
    posts=Post.get_all_posts()
    return render_template("posts/post.html",posts=posts)
