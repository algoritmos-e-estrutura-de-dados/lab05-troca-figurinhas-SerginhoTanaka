def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    if len(figurinhas_do_joao) >= len(figurinhas_da_maria):
        maior = figurinhas_do_joao
        menor = figurinhas_da_maria
    else:
        menor = figurinhas_do_joao
        maior = figurinhas_da_maria

    maior_copy = maior.copy()
    menor_copy = menor.copy()
    for i in range(len(menor)):
        for j in range(len(maior)):

            if maior[j] == menor[i]:
                for k in range(len(maior_copy)):

                    if int(menor_copy[k]) == int(maior[j]):
                        menor_copy.pop(k)
                        if len(maior_copy) == 0:
                            return 0
                        else:
                            return len(menor_copy)
                        
            elif maior[j] is not menor[i]:
                return len(menor_copy)
                


if __name__ == '__main__':

    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_do_joao = input().split(' ')


    print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao))
