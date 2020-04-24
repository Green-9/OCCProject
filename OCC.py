from flask import Flask
app = Flask(__name__)
## Made the app called name?
@app.route('/')
def MainPage(): 
    return 'Hello World'
    ## When import flask, we made a little site. Now when we go on the site,
    ## after the slash, 'hello' is like the about page

@app.route('/About/')
## Now if I search "localhost:5000", it will return Hello World on the About page
def AboutPage(): 
    return 'Hi! Welcome to the \'About\' page.'
