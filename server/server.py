from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/house_price_prediction',methods=['POST'])
def house_price_prediction():
    longitude = float(request.form["longitude"])
    latitude = float(request.form["latitude"])
    housing_median_age = float(request.form["housing_median_age"])
    median_income = float(request.form["median_income"])
    ocean_proximity = float(request.form["ocean_proximity"])
    rooms_per_household = float(request.form["rooms_per_household"])
    bedrooms_per_room = float(request.form["bedrooms_per_room"])
    population_per_household = float(request.form["population_per_household"])
    response = jsonify({"Estimated Price":
    util.predict_price(longitude,latitude,housing_median_age,
                       median_income,ocean_proximity,rooms_per_household,
                       bedrooms_per_room,population_per_household)})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response
if __name__ == "__main__":
    print("Starting Python Flask Server for Real Estate Price Prediction")
    app.run()