def contadora(sequencia):
    letra = ""
    output = []
    count = 1


    if sequencia:
        for i in range(len(sequencia)):
            print(i, sequencia[i], letra)
            if sequencia[i] != letra:
                if letra != "":
                    output.append(save)
                letra = sequencia[i]
                count = 1
                save = (letra, count)

            else:
                count += 1
                save = (letra, count)

            if i == len(sequencia) - 1:
                    output.append(save)
        
        return output
    
    else: 
        return "Nada foi digitado."

sequencia = input("Digita uma sequência de caracteres: ")
print(contadora(sequencia))
