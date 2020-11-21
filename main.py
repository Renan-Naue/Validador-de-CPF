import re

def isCpfValid(cpf):
    
    
    if not isinstance:
        return False

    cpf = re.sub("[^0-9]",'',cpf)


    if cpf =='00000000000' or cpf=="11111111111" or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777':
        return False


    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1


    verifyingDigit = 11 - sum % 11


    if verifyingDigit > 9:
        firtsVerifyingDigit = 0
    else:
            firtsVerifyingDigit = verifyingDigit


    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight


        weight = weight - 1
    verifyingDigit = 11 - sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0

    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firtsVerifyingDigit, secondVerifyingDigit):
        return True

   
    return False


cpf = input('Informe seus cpf:')


isCpfValid(cpf)


print(isCpfValid(cpf))





