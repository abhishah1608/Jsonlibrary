import jsonpickle

def convertObjToJson(obj):
    return jsonpickle.encode(obj,unpicklable=False)


def convertJsonToObj(str):
    return  jsonpickle.decode(str)