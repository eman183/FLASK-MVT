# intialize app
from flask import Flask
from task.config import project_config
from task.models import  db ,Post
# from flask_migrate import Migrate


def create_app(config_name):
    app=Flask(__name__)
    app_config=project_config[config_name]
    # print(app_config)
    app.config["SQLALCHEMY_DATABASE_URI"]=app_config.SQLALCHEMY_DATABASE_URI

    app.config.from_object(app_config)
    db.init_app(app)
  
    from task.posts.views import get_posts
    app.add_url_rule("/posts",view_func=get_posts,endpoint="get.posts")
    return app
# create_app()