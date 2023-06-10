from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Category(db.Model):
     __tablename__="Category"
     id=db.Column(db.Integer,primary_key=True)
     title=db.Column(db.String(20))

     def __str__(self):
          return self.title

class Post(db.Model):
     __tablename__="Post"
     id=db.Column(db.Integer,primary_key=True)
     title=db.Column(db.String(100))
     body=db.Column(db.Text(500))
     image=db.Column(db.String)
     data=db.Column(db.LargeBinary ,default=None)
     Category_id=db.Column(db.Integer,db.ForeignKey("Category.id"),nullable=True)
     def __str__(self):
          return self.title
     


     
     @classmethod
     def get_all_posts(cls):
         return cls.query.all()

  
     @classmethod
     def get_specific_object(cls, id):
        return  cls.query.get_or_404(id)
     

  
     def delete_post(self):
          db.session.delete(self)
          db.session.commit()
          return True
     



     @classmethod
     def get_all_category(cls):
         return cls.query.all()