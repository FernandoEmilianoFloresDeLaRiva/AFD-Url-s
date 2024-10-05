class ValidatorTxt:
    
    def __init__(self, data) -> None:
        self.data = data
    
    def validar_formato_estados(self):
        if ("states" in self.data) and (len(self.data["states"]) != 0):
            for state in self.data["states"]:
                if ("name" in state) and (len(state["name"]) != 0):
                    if "connections" in state:
                        if len(state["connections"]) != 0:
                            for connection in state["connections"]:
                                if ("to" in connection) and (len(connection["to"]) != 0):
                                    if ("conector" in connection) and (len(connection["conector"]) != 0):
                                        return True
                                    else:
                                        print("Una conexión no cuenta con el array: conector o es un array vacio")
                                        return False
                                else:
                                    print("Una conexión no cuenta con el atributo: to o es una cadena vacia")
                                    return False
                    else:
                        print("Un estado no cuenta con el array: connections, esta debe estar presente aún siendo un array vacio")
                        return False
                else:
                    print("Los estados no cuentan con el atributo: name o es una cade vacia")
                    return False
        else:
            print("El automata no cuenta con estados o es un arreglo vacio")
            return False

    def validar_existencia_alfabeto(self):
        if "alpha" in self.data and (len(self.data["alpha"]) != 0):
            for caracter in self.data["alpha"]:
                if caracter == "":
                    print("El alfabeto contiene una cadena vacia")
                    return False
        else:
            print("El automata no cuenta con un alfabeto, atributo: alpha o es un array vacio")
            return False
        return True
        
    def validar_existencia_estado_inicial(self):
        if "startState" in self.data and len(self.data["startState"]) != 0:
            # Usamos next() para buscar el estado inicial en el array de estados
            estado_inicial = next((state for state in self.data["states"] if state["name"] == self.data["startState"]), None)
            if estado_inicial:
                return True
        print("El autómata no declara un estado inicial o es una cadena vacía")
        return False

    def validar_existencia_estados_finales(self):
        if "endStates" in self.data and len(self.data["endStates"]) != 0:
            for endState in self.data["endStates"]:
                if endState != "":
                    # Usamos next() para buscar el estado final en el array de estados
                    estado_final = next((state for state in self.data["states"] if state["name"] == endState), None)
                    if estado_final is None:
                        print(f"El estado final '{endState}' no existe en el array de estados")
                        return False
                else:
                    print("Existe una cadena vacia en los estados finales")
                    return False
            return True
        else:
            print("El autómata no declara estados finales o es un array vacío")
            return False

    def validar_repeticion_estados(self):
        estados = []
        for state in self.data["states"]:
            estados.append(state["name"])
        repeticiones = dict(zip(estados, map(lambda x: estados.count(x), estados)))
        for repeticion in repeticiones.values():
            if repeticion > 1:
                return False
        return True

    def validar_repeticion_estados_finales(self):
        estados_finales = self.data["endStates"]
        repeticiones = dict(zip(estados_finales, map(lambda x: estados_finales.count(x), estados_finales)))
        for repeticion in repeticiones.values():
            if repeticion > 1:
                return False
        return True
        
    def validar_repetición_estados_conectados(self):
        estados_conectados = []
        for state in self.data["states"]:
            for connection in state["connections"]:
                estados_conectados.append(connection["to"])
            repeticiones = dict(zip(estados_conectados, map(lambda x: estados_conectados.count(x), estados_conectados)))
            for repeticion in repeticiones.values():
                if repeticion > 1:
                    return False
            estados_conectados = []
        return True

    def validar_repetición_conectores(self):
        conectores = []
        for state in self.data["states"]:
            for connection in state["connections"]:
                conectores.extend(connection["conector"])
            repeticiones = dict(zip(conectores, map(lambda x: conectores.count(x), conectores)))
            for repeticion in repeticiones.values():
                if repeticion > 1:
                    return False
            conectores = []
        return True
            
    def validar_data(self):

        validaciones = [
            self.validar_formato_estados,
            self.validar_existencia_alfabeto,
            self.validar_existencia_estado_inicial,
            self.validar_existencia_estados_finales,
            self.validar_repeticion_estados,
            self.validar_repeticion_estados_finales,
            self.validar_repetición_estados_conectados,
            self.validar_repetición_conectores
        ]

        return all(func() for func in validaciones)
