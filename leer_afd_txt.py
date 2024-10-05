def leer_automata_de_txt(ruta_txt):
    automata = {
        "states": [],
        "startState": None,
        "endStates": [],
        "alpha": []
    }

    estados = {}

    with open(ruta_txt, 'r') as archivo:
        lineas = archivo.readlines()        
        automata["startState"] = lineas[0].strip()        
        automata["endStates"] = lineas[1].strip().split(',')
        automata["alpha"] = lineas[2].strip().split(',')        
        for linea in lineas[3:]:
            partes = linea.strip().split(',')
            from_state = partes[0]
            to_state = partes[1]
            conectores = partes[2:]        
            if from_state not in estados:
                estados[from_state] = {
                    "name": from_state,
                    "connections": []
                }
            estados[from_state]["connections"].append({
                "to": to_state,
                "conector": conectores
            })
    automata["states"] = list(estados.values())
    return automata