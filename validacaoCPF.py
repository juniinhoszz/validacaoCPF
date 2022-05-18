#--Validador de CPF--#

import numbers


#FUNÇÃO PARA A VALIDAÇÃO DO CPF#
def cpf_validacao(numbers):
    cpf = [int(numeros) for numeros in numbers if numeros.isdigit()]

    
    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

print("")
print('''---VALIDADOR DE CPF---''')
print("")



cpf = input('Digite o CPF: ')
if cpf_validacao(cpf):
        print('CPF válido.')
else:
        print('CPF inválido.')


