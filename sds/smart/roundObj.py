def RoundObjects(object, val):
    for key in object.keys():
        if val == 0:
            object[key] = round(object[key])
        else:
            object[key] = round(object[key], val)
    return object
