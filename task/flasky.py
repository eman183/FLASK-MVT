from task import create_app




app = create_app('dev')
if __name__=="__main":
    app.run()