import pickle
import pandas as pd


with open("./artifacts/house_prices_model.pickle", "rb") as file:
    model = pickle.load(file)


def predict_price(longitude,latitude,housing_median_age,median_income,ocean_proximity,rooms_per_household,bedrooms_per_room,population_per_household):
    lst = list()
    lst.append(longitude)
    lst.append(latitude)
    lst.append(housing_median_age)
    lst.append(median_income)
    lst.append(ocean_proximity)
    lst.append(rooms_per_household)
    lst.append(bedrooms_per_room)
    lst.append(population_per_household)
    single_house = pd.Series(lst).values.reshape(-1,8)
    return model.predict(single_house)
prediction = predict_price(-119.01,36.06,25.0,1.6812,1,4.192201,0.213039,3.877437)
print(prediction)