<
from flask import Flask , request ,render_template ,session 

app = Flask(__name__)
app.secret_key="my_secret"
@app.route('/')
def hello():
    return "Hello"
@app.route("/welcome")
def welcome():
    return "You are Welcome"
# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         username=request.form['username']
#         session['user']=username
#         return "logged in"
#     return render_template('login.html')

from flask import Flask, request, render_template, session

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST': 
        username = request.form['username']
        session['user'] = username
        return "logged in"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html')
@app.route('/search')
def search():
    name=request.args.get('name')
    # return render_template('search.html',name=name)
    return name
@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    return a+b
if __name__ == '__main__':

from flask import Flask , request ,render_template ,session 

app = Flask(__name__)
app.secret_key="my_secret"
@app.route('/')
def hello():
    return "Hello"
@app.route("/welcome")
def welcome():
    return "You are Welcome"
# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         username=request.form['username']
#         session['user']=username
#         return "logged in"
#     return render_template('login.html')

from flask import Flask, request, render_template, session

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST': 
        username = request.form['username']
        session['user'] = username
        return "logged in"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html')
@app.route('/search')
def search():
    name=request.args.get('name')
    # return render_template('search.html',name=name)
    return name
@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    return a+b
if __name__ == '__main__':

    app.run(debug=True)