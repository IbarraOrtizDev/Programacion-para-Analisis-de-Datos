def jsonResponse(dataArray):
    return {
            "id": dataArray[0],
            "title": dataArray[1],
            "price": dataArray[2],
            "marca": dataArray[3],
            "imagenProducto": dataArray[4],
            "rating": dataArray[5],
            "linkProduct": dataArray[6],
            "store": dataArray[7],
            "ean": dataArray[8]
        }

def arrayJsonResponse(data):
    return [jsonResponse(d) for d in data]