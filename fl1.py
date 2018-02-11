from flask import Flask, jsonify, request,render_template
from navigation import time_dist
from jericho import * 


app = Flask(__name__)

@app.route("/_get_time_dist")
def _get_time_dist():
    Iorigin = request.args.get('origin',0)
    Idestination = request.args.get('destination',0)
    such = time_dist(Iorigin,Idestination)
    result = str(such[0]) + str(such[1])
    return jsonify(result=result)

@app.route("/")
def root():
    getAllVehicles()
    return render_template('ask.html')

@app.route("/result",methods = ['POST','GET'])
def hello():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        such = time_dist(origin,destination)
        return render_template('result.html',duration = str(such[0]),distance = str(such[1]))

    else:
        return "ERROR"


if __name__ == "__main__":
  app.run(debug = True)