# > ESTRUTURAS CONDICIONAIS

idade = 18

if idade >= 18:
    print("Maior de idade")

else: 
    print("Menor de idade")    

"""
Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha média
superior ou igual a 7, e "Reprovado(a)", caso a média seja inferior a 7.
"""

media = float(input("Informe a média do estudante: "))

if media >= 7:
    print("Aprovado(a)")

elif media  >= 5:
    print("Recuperação")
else:
    print("Reprovado(a)")


media = 10
presenca = 100
if media >= 7 and presenca >= 70:
    print("Aprovado(a)")

else: print ("Reprovado(a)")    