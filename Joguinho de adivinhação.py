print("********************************")
 print('Bem vindo ao jogo de forca')
 print("**********************************")

palavra_secreta = "python"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]

enforcou = False
acertou = False



while (not acertou and not enforcou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print(letras_acertadas)
