def revisar_si_es_id(palabra_ingresada):
    if len(palabra_ingresada) == 0:
        return False
        
    estado_automata = 0 # estado inicial
    for letrita in palabra_ingresada:
        
        if estado_automata == 0:    
            if (letrita >= 'a' and letrita <= 'z') or (letrita >= 'A' and letrita <= 'Z'):
                estado_automata = 1 
            else:
                estado_automata = -1 
                
        elif estado_automata == 1:#En esta parte basicamente verificamos que en la cadena no haya nada que no sean letras o numeros
            es_letra_min = (letrita >= 'a' and letrita <= 'z')
            es_letra_mayus = (letrita >= 'A' and letrita <= 'Z')
            es_un_numero = (letrita >= '0' and letrita <= '9')
            
            if es_letra_min or es_letra_mayus or es_un_numero:
                estado_automata = 1
            else:
                estado_automata = -1 
                
        if estado_automata == -1:
            break
            
    if estado_automata == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    
    cadenas_test = ["variable1", "Cristian", "Andres321", "1Reinales", "ID"]

    for prueba in cadenas_test:
        
        resultado_final = revisar_si_es_id(prueba)
        
        if resultado_final == True:
            print("SI ACEPTA la cadena -> " + prueba)
        else:
            print("NO ACEPTA la cadena -> " + prueba)
