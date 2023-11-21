import json

def readJsonFile(filename):
    data = ""
    try:
        with open(filename) as jsonFile:
            data = json.load(jsonFile)
    except IOError:
        print("could not read file")
    except Exception as e:
        print("global exception occured")
        raise e
    
    return data
    