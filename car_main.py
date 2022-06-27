from queue import Empty
from pydantic import BaseModel
import pymongo
from fastapi import FastAPI
import uvicorn
from cars_models import car_serial, cars_shcema

client = pymongo.MongoClient(
    "mongodb+srv://mongouser:mongopwd@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
database = client['mydatabase']
car_collection = database['Cars_DataBase']


app = FastAPI()


class CarModel(BaseModel):
    Name: str
    Miles_per_Gallon: int
    Cylinders: int
    Displacement: int
    Horsepower: int
    Weight_in_lbs: int
    Acceleration: int
    Year: str
    Origin: str


@app.get('/api/ViewAll', tags=['Cars'])
def view_all():
    try:
        result = car_serial(car_collection.find())
        return {"data": result}

    except Exception as e:
        print("Error in viewing data" + str(e))
        return "failed to view"


@app.post('/api/add', tags=['Cars'])
def add(car: CarModel):
    try:
        car_collection.insert_one(car.dict())
        return "Added Successfully"
    except Exception as e:
        print("Error in viewing data" + str(e))
        return "failed to view"


@app.put('/api/update/{Name}', tags=['Cars'])
def update(Name, car: CarModel):

    try:

        update_car = (car.dict())
        car_collection.update_one({"Name": Name}, {"$set": update_car})
        return "updated Successfully"
    except Exception as e:
        print("Error in viewing data" + str(e))
        return "failed to view"


@app.delete('/api/delete/{Name}', tags=['Cars'])
def dalete(Name):
    try:

        car_collection.delete_one({"Name": Name})
        return "deleted Successfully"

    except Exception as e:
        print("Error in viewing data" + str(e))
        return "failed to view"

@app.get('/api/updateBykeyvalue/{key}/{value}', tags=['Cars'])
def get_keyvalue(key,value):
    try:
        result=car_serial(car_collection.find({key:value}))
        if len(result)==0:
            return "no match found"
        return {"data":result}

    except Exception as e:
        print("Error in viewing data" + str(e))
        return "failed to view"

if __name__ == '__main__':
    uvicorn.run("car_main:app", reload=True, access_log=False)
