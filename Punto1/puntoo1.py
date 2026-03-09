def validar_jugada_chess(string_movimiento):
    nodo_actual = 0
    
    for letra in string_movimiento:
        
        if nodo_actual == 0:
            # tiene que empezar con letra minuscula si o si
            if letra >= 'a' and letra <= 'z':
                nodo_actual = 1
            else:
                nodo_actual = -1 
                
                
        elif nodo_actual == 1: # puede seguir teniendo letras como en el caso de kbp
            if letra >= 'a' and letra <= 'z':
                nodo_actual = 1
            elif letra == '-':
                nodo_actual = 2 # ->
            elif letra == ' ':
                nodo_actual = 4 # X
            else:
                nodo_actual = -1
                

        elif nodo_actual == 2:
            if letra == '>':
                nodo_actual = 3
            else:
                nodo_actual = -1
                
        elif nodo_actual == 4:
            if letra == 'X':
                nodo_actual = 5
            else:
                nodo_actual = -1
                
        elif nodo_actual == 5:
            if letra == ' ':
                nodo_actual = 3
            else:
                nodo_actual = -1
                
        
        elif nodo_actual == 3:
            if letra >= 'a' and letra <= 'z':
                nodo_actual = 6
            else:
                nodo_actual = -1
                
        elif nodo_actual == 6:
            if letra >= 'a' and letra <= 'z':
                nodo_actual = 6
            elif letra >= '0' and letra <= '9':
                nodo_actual = 7 
            else:
                nodo_actual = -1
                
        elif nodo_actual == 7:
            nodo_actual = -1
            
        if nodo_actual == -1:
            break

    if nodo_actual == 6 or nodo_actual == 7:
        return True
    else:
        return False


if __name__ == "__main__":
    
    lista_de_pruebas = ["p->k4", "kbp X qn", "q->r8", "n X p"] # meto los ejemplos del taller mas unos mios para probar bien la logica

    for prueba in lista_de_pruebas:
        es_valido = validar_jugada_chess(prueba)
        
        if es_valido == True:
            print("ACEPTA  -> " + prueba)
        else:
            print("RECHAZA -> " + prueba)
