n1 = float(input('Qual foi a primeira nota: '))
n2 = float(input('Qual foi a segunda nota: '))
média = (n1 + n2) / 2
print('A sua média é {}'.format(média))
if média <= 5.0:
    print('Você foi reprovado!!')
elif média > 6.9:
    print('Você foi aprovado!!')
else:
    print('Você está de recuperação!')