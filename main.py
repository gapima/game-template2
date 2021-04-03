import random

def jogar():
    banner = """
    *****************************
     **** Simulador de Dado ****
    *****************************
    """

    print(banner)







    print("Você gostaria de jogar o dado?")
    print("(1)Sim  (2)Não")
    escolha = int(input("Digite sua escolha: "))



    while(escolha):
        numero_aleatorio = random.randrange(1, 7)
        if (escolha == 1):
            print("Rolando o dado...")
            print("Resultado: {}". format(numero_aleatorio))

            print("Deseja jogar novamente?")
            print("(1)Sim  (2)Não")
            repete_jogo = int(input("Digite: "))

            if (repete_jogo == 1):
                continue
            elif (repete_jogo == 2):
                print("Fechando o jogo.")
                break
            else:
                print("digito invalido, insirá um digito valido.")
                continue


        elif (escolha == 2):
            print("Fechando o jogo.")
            break

        else:
            print("Valor inserido é inválido, insira um valor válido!")
            jogar()

if(__name__,"__main__"):
    jogar()
