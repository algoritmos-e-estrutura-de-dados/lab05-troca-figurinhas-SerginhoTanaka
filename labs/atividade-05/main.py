def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    aux = 0
    for i in range(len(figurinhas_da_maria)-1):
        for j in range(len(figurinhas_do_joao)-1):

            if len(figurinhas_da_maria) >= len(figurinhas_do_joao):
                if figurinhas_da_maria[i] == figurinhas_do_joao[j]:
                    valor = figurinhas_da_maria[i]
                    figurinhas_da_maria.remove(valor)
                    print(valor)
                    return len(figurinhas_da_maria)-1
            if len(figurinhas_do_joao) > len(figurinhas_da_maria):
                if figurinhas_do_joao[j] == figurinhas_da_maria[i]:
                    valor = figurinhas_do_joao[j]
                    figurinhas_do_joao[j].remove(valor)

                if figurinhas_da_maria[i] != figurinhas_do_joao[j]:
                    aux = aux + 1


if __name__ == '__main__':
    """""
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_do_joao = input().split(' ')
    """

    figurinhas_da_maria = [1, 3, 5, 7]
    figurinhas_do_joao = [2, 3, 5]

    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao)
