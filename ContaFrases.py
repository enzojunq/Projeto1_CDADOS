def remove_pontos(frase):

    alfabeto = ["a" , "b" , "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #, "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    frasefin = []

    palavra = []

    for i in frase:

        if i.isupper():
             g = i.lower()
             i = g

        if i in alfabeto:
            palavra.append(i)
        
    
        elif i not in alfabeto:
        
            if len(palavra) != 0:

            
                new = "".join(palavra)
                frasefin.append(new)
                palavra = []

    return frasefin

frase3 = "Essa  essa frase: eu estou$$ usaNdo como um tEste, teste usando um um um , um"   
 
frasefin = (remove_pontos(frase3))

print(frasefin)

palavrascont = {} # fora do  If review = conteudo

for i in range(len(frasefin)):

        palavra = frasefin[i]

        if palavra in palavrascont:
            palavrascont[palavra] += 1
           
            
        elif palavra not in palavrascont:
            palavrascont[frasefin[i]] = 1

print(palavrascont)

print(palavrascont.values())

totalpalavrascont = 0  # vai fora do If review = conteudo

totalpalavrascont += sum(palavrascont.values())

print(totalpalavrascont)

print(palavrascont["um"])





    