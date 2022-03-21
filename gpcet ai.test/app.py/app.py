from Flask import  Flask

app=Flask(__name__)

@app.route('/')
def homepage():
        return('Hello GPCET-hi gids')

if (__name__=="__main__"):
    app.run()

