# intialize app
from flask import Flask
from task.config import project_config
from task.models import  db 
from flask_migrate import Migrate
# from flask_migrate import Migrate


def create_app(config_name):
    app=Flask(__name__)
    app_config=project_config[config_name]
    # print(app_config)
    app.config["SQLALCHEMY_DATABASE_URI"]=app_config.SQLALCHEMY_DATABASE_URI

    app.config.from_object(app_config)
    db.init_app(app)
    #add migration
    migrate=Migrate(app,db,render_as_batch=True)
  
    # from task.posts.views import get_posts
    # app.add_url_rule("/posts",view_func=get_posts,endpoint="get.posts")
    # from task.posts import post_blueprint
    # app.register_blueprint(post_blueprint)
    from task.posts.postblueprint import post_blueprint
    app.register_blueprint(post_blueprint)
    return app
# create_app()