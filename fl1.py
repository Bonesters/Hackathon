from flask import Flask, jsonify, request,render_template, make_response
from navigation import time_dist
from jericho import * 


app = Flask(__name__,template_folder='.')

@app.route("/_get_time_dist")
def _get_time_dist():
    print("--+--+--+--")
    Iorigin = request.args.get('origin',0)
    Idestination = request.args.get('destination',0)
    such = time_dist(Iorigin,Idestination)
    result = str(such[0]) + str(such[1])
    return jsonify(result=result)

@app.route("/_graph_",methods=['POST','GET'])
def _graph_():
    truck = request.args['truck']
    startDate = request.args['startDate']
    endDate = request.args['endDate']
    print(truck + " " + startDate + " " + endDate)
    #grab from sql
    return make_response(jsonify(statusText=result))


@app.route("/truck_hours")
def truck_hours():
    truck = request.args.ge('truck')
    startDate = request.args['startDate']
    endDate = request.args['endDate']
    print(truck + " " + startDate + " " + endDate)
    #TODO run SQL statement and return results
    resp = make_response(jsonify('hello'))
    resp.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return resp


@app.route("/truckSET",methods=['POST','GET'])
def caeltest():
    dictor = request.args.to_dict()
    startDate = dictor['startDate']
    endDate = dictor['endDate']
    truck = request.args['truck']
    response = timePerTruckPerDayRange(startDate,endDate,truck)
    resp = make_response(jsonify(response))
    #resp.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return resp

@app.route("/")
def root():
    return render_template('index.html')

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