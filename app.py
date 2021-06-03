from flask import Flask, session, redirect, request
import os

server_port = 5000
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') 

@app.route("/")
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect("/")
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect("/")

@app.route("/<user>")
def show_user(user):
    return "This is the profile of %s" % user


@app.route("/<user>/friends")
def show_user_friends(user):
    return "These are the %s's friends: <br> Obi Wan <br> Darth Vader <br> Grogu" % user

if __name__ == "__main__":
    app.run('0.0.0.0', port = server_port)