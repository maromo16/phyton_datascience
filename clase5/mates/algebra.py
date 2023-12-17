def producto_vectores(vector1, vector2):
    vector3 = []
    for x in vector1: 
        aux = 0 
        for y in vector2: 
            aux = aux + (x*y)
            