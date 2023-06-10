from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()



class Post(db.Model):
     __tablename__="Post"
     id=db.Column(db.Integer,primary_key=True)
     title=db.Column(db.String(100))
     body=db.Column(db.Text(500))
     image=db.Column(db.String)
     data=db.Column(db.LargeBinary ,default=None)


     def __str__(self):
          return self.title
     
     @classmethod
     def get_all_posts(cls):
         return cls.query.all()

    


     @classmethod
     def show_post(cls,id):
       return cls.query.get_or_404(id)
