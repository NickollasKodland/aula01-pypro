meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "FARMAR": "Obter um número elevado de um determinado recurso",
            "BISCOITAR": "Postar algo apenas para chamar a atenção"
            }

palavra = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if palavra in meme_dict.keys():
    print(meme_dict[palavra])
else:
    print("Não conheço essa palavra")
