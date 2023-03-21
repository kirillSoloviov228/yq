from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def requestdata():
    return "Hello! Your IP is {} and you are using {}: ".format(request.remote_addr,
request.user_agent)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

@app.route('/user/<id>')
def user_profile(id):
    return "Profile page of user #{}".format(id)

if __name__ == "__main__":
    app.run(debug=True)