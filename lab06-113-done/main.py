import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

def createVehicle(column_names,row):
    desc = ""
    result = copy.deepcopy(myVehicle)  
    for idx in range (0,len(column_names)):
        desc += column_names[idx] +": "+ row[idx] + ", "
        result[column_names[idx]] = row[idx]
    
    print(desc)
    return result

myInventoryList = []
for key, value in myVehicle.items():
    print(f"{key} : {value}")

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    column_names = []
    for row in csvReader:
        if lineCount == 0:
            column_names = row
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:
            currentVehicle = createVehicle(column_names,row)
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')


for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print(f"{key} : {value}", end = ' ')
        print("-----", end = ' ')
    print(" ")


# print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
# currentVehicle = copy.deepcopy(myVehicle)  
# currentVehicle["vin"] = row[0]  
# currentVehicle["make"] = row[1]  
# currentVehicle["model"] = row[2]  
# currentVehicle["year"] = row[3]  
# currentVehicle["range"] = row[4]  
# currentVehicle["topSpeed"] = row[5]  
# currentVehicle["zeroSixty"] = row[6]  
# currentVehicle["mileage"] = row[7]  