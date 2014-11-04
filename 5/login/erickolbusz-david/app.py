from flask import Flask, render_template, request, redirect, session
import mongo

app = Flask(__name__)
id=0
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#login page
@app.route("/")
def index():
    user = request.args.get("username","None")
    pw = request.args.get("password","None")
    if (user == "None" and pw == "None"):
      return render_template ("login.html") #have a button that redirects to /register
    if mongo.login(user,pw):
      session ['username'] = username
      return redirect("/welcome")
    

@app.route("/register")
def register():
    user = request.args.get("username","None")
    pw = request.args.get("password","None")
    register = request.args.get("register")
    if (submit == "Register")
        error = mongo.add_account(user,pw)
        if (error == 0):
                      #why is this indentation here
                      flash("Successfully registered")
                      return redirect ("/")
        if (error == 1):
                      flash("Account already exists")
        if (error == 2):
                      flash("Username too short, must be at least 6 characters")
        else:
                      #error = 3
                      flash("Password too short, must be at least 8 characters")
    #flash the message
    return render_template ("register.html") #have a button that redirects to /
    
@app.route("/welcome")
def welcome():
    return render_template ("welcome.html") #button for other page (?) and for /logout
                      
@app.route('/logout')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.debug = True
    app.run()
