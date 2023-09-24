frase3 = "um dôis TRes quatro cinco seis sete oito nove dez onze doze quatro quatro quatro" 

frase4 = " um dois tres quatro cinco sete seis oito nove"
def remove_pontos(frase):

    alfabeto = ["a" , "b" , "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #, "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    acentos = ["á" , "é", "í" , "ó" , "ú" , "ñ" , "â" , "ê" , "î" , "ô" , "û" , "à" , "è" , "ì" , "ù" , "ò"]
    frasefin = []

    palavra = []

    for i in frase:

        if i.isupper():
             g = i.lower()
             i = g

        if i == "á"or i == "â" or i == "à":
             i = "a"

        elif i == "é"or i == "ê" or i == "è":
             i = "e"

        elif i == "í"or i == "î" or i == "ì":
             i = "i"

        elif i == "ú"or i == "û" or i == "ù":
             i = "u"

        elif i == "ó"or i == "ô" or i == "ò":
             i = "o"

        elif i == "ñ":
             i = "n"
        

        if i in alfabeto:
            palavra.append(i)
        
    
        elif i not in alfabeto:
        
            if len(palavra) != 0:

            
                new = "".join(palavra)
                frasefin.append(new)
                palavra = []

    if len(palavra) > 1:
         
        new2 = "".join(palavra)
        frasefin.append(new2)
        palavra = []

    return frasefin

  
 
#frasefin = (remove_pontos(frase3))

#print(frasefin)

#palavrascont = {} # fora do  If review = conteudo

def conta_palavras(listapal , dicpalavras):
     
    for i in range(len(listapal)):

        palavra = listapal[i]

        if palavra in dicpalavras:
            dicpalavras[palavra] += 1
           
            
        elif palavra not in dicpalavras:
            dicpalavras[listapal[i]] = 1
    
    return dicpalavras

#palavrasconteudo = conta_palavras(frasefin , palavrascont)

#print(palavrasconteudo)

#print(palavrasconteudo.values())

#totalpalavrascont = 0  # vai fora do If review = conteudo

#totalpalavrascont += sum(palavrasconteudo.values())

#print(totalpalavrascont)

#print(palavrascont["quatro"])

# 1 = conteudo 2 = amazon 3 = edicao

classificacao = 1

palavrascont = {}
palavrasamazon = {}
palavrasedicao = {}

totalpalavrascont = 0
totalpalavrasamazon = 0
totalpalavrasedicao = 0

if classificacao == 1:

    listafrase = remove_pontos(frase3)

    totalpalavras = conta_palavras(listafrase , palavrascont)

    totalpalavrascont = sum(totalpalavras.values())

elif classificacao == 2:

    listafrase = remove_pontos(frase3)

    totalpalavras = conta_palavras(listafrase , palavrasamazon)

    totalpalavrasamazon = sum(totalpalavras.values())

elif classificacao == 3:

    listafrase = remove_pontos(frase3)

    totalpalavras = conta_palavras(listafrase , palavrasedicao)

    totalpalavrasedicao = sum(totalpalavras.values())


print("Total de palavras em conteudo: " + str(totalpalavrascont))
print("Total de palavras em amazon: " + str(totalpalavrasamazon))
print("Total de palavras em edicao: " + str(totalpalavrasedicao))

print(palavrascont["quatro"])



classificacao = 1


if classificacao == 1:

    listafrase = remove_pontos(frase4)

    totalpalavras = conta_palavras(listafrase , palavrascont)

    totalpalavrascont = sum(totalpalavras.values())

elif classificacao == 2:

    listafrase = remove_pontos(frase4)

    totalpalavras = conta_palavras(listafrase , palavrasamazon)

    totalpalavrasamazon = sum(totalpalavras.values())

elif classificacao == 3:

    listafrase = remove_pontos(frase4)

    totalpalavras = conta_palavras(listafrase , palavrasedicao)

    totalpalavrasedicao = sum(totalpalavras.values())



print("Total de palavras em conteudo: " + str(totalpalavrascont))
print("Total de palavras em amazon: " + str(totalpalavrasamazon))
print("Total de palavras em edicao: " + str(totalpalavrasedicao))







    