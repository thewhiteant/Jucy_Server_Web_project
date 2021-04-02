from flask import Flask,request,render_template,url_for


app = Flask(__name__)

@app.route("/login/")
@app.route("/signin/")
@app.route('/')
def index():
    return render_template("login.html")



@app.route("/signup/")
@app.route("/register")
def signup():
    return render_template("/signup.html")




if __name__ == '__main__':
    app.run(debug=True)
