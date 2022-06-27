def cars_shcema(data):
    return{
        "Name":str(data["Name"]),
        "Miles_per_Gallon":int(data["Miles_per_Gallon"]),
        "Cylinders":int(data["Cylinders"]),
        "Displacement":int(data["Displacement"]),
        "Horsepower":int(data["Horsepower"]),
        "Weight_in_lbs":int(data["Weight_in_lbs"]),
        "Acceleration":int(data["Acceleration"]),
        "Year":str(data["Year"]),
        "Origin":str(data["Origin"])
    }

def car_serial(datas):
    return [cars_shcema(data) for data in datas]
