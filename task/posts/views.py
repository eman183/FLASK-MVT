from task.models import Post
from flask import render_template,redirect,url_for
from task.posts.postblueprint import post_blueprint


@post_blueprint.route("",endpoint='posts_get')
def get_posts():
    posts=Post.get_all_posts()
    return render_template("posts/post.html",posts=posts)



@post_blueprint.route("/<int:id>",endpoint='post_show')
def show_post(id):
     post=Post.get_specific_object(id)
     return render_template("posts/show.html",post=post)

@post_blueprint.route("/<int:id>/delete",endpoint='post_delete')
def delete_post(id):
     post=Post.get_specific_object(id)
     post.delete_post()
     url=url_for('posts.posts_get')
     return redirect(url)