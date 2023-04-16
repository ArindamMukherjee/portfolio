from flask import Flask, render_template

app = Flask(__name__) # creat an object 

@app.route("/")  # route the app
def home_page():
    return render_template("home.html")
if __name__ =="__main__":
  app.run(host = "0.0.0.0",port = "5000", debug = True) # 