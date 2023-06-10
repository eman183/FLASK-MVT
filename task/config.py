# from doctest import debug
# from pickle import FALSE, TRUE
# from pyclbr import Class
# from re import DEBUG

# app=l
class Config():
    def init_config():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///project.db"



class ProductionConfig(Config):
    DEBUG=False
    #path postgres
    #postgresql:://username:password@localhost:portnumber/databasename
    SQLALCHEMY_DATABASE_URI= "postgresql://taskflask:123@localhost:5432/system"





project_config= {
    "dev": DevelopmentConfig,
    "prd":ProductionConfig
}