from flask import Flask, render_template

Projects=[
  {
     'id': 1,
     'title' : "Autonomious Drone",
  },

  {
     'id': 2,
     'title' : "Obstacle avoider using Ultrasonic Sensor",
  },

  {
     'id': 3,
     'title' : "VRV",
  }
]

app = Flask(__name__) # creat an object 

@app.route("/")  # route the app
def home_page():
    return render_template("home.html",projects=Projects)

# @app.route("/projects"):
# def projects():
#   return 
if __name__ =="__main__":
  app.run(host = "0.0.0.0",port = "5000", debug = True) # 