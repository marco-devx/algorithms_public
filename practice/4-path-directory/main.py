"""
    Bluedash
    Hoy aprenderemos:
    - Strings (Datos primitivos)
        Cadena de texto ("" o '')
    - Bucles
        for:
            lo puedes cuando, debes
            recorrer un objeto iterador
        while**
    - Arrays (listas)
    - Intro de algoritmos
"""

def canonical_path (path):
    result = []
    for directory in path.split("/"):
        if directory in [".", ""]:
            continue

        if directory == "..":
            if result:
                result.pop()
        else:
            result.append(directory)

    print("/"+"/".join(result))


canonical_path("/home/../../../../user/Documents/../Pictures")
# "/user/Pictures"


