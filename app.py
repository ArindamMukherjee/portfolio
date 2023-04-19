from flask import Flask, render_template,jsonify

Projects=[
  {
     'id': 1,
     'title' : "Real-time Object Detection System using OpenCV and COCO Dataset",
  },

  {
     'id': 2,
     'title' : "Intelligent Robotic Navigation System using IR Sensor and NTP Time Synchronization",
  },

  {
     'id': 3,
     'title' : "Intelligent Power Monitoring System with Current Sensor and Relay Control",
  }
]

app = Flask(__name__) # creat an object 

@app.route("/")  # route the app
def home_page():
    return render_template("home.html",projects=Projects)
@app.route("/api/projects")
def show_json():
  return jsonify(Projects)

# @app.route("/projects"):
# def projects():
#   return 
if __name__ =="__main__":
  app.run(host = "0.0.0.0",port = "5000", debug = True) # 