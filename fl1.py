from flask import Flask, jsonify, request,render_template, make_response
from jericho import * 


app = Flask(__name__,template_folder='.')


@app.route("/truckAVG",methods=['POST','GET'])
def truck_hours():
    dictor = request.args.to_dict()
    startDate = dictor['startDate']
    endDate = dictor['endDate']
    
    response = timePerTruck(startDate,endDate)

    print(response)

    resp = make_response(jsonify(response))
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

if __name__ == "__main__":
  app.run(debug = True)