nota1 =  int(input('Informe a nota do 1° Bimestre (0-100): ')) 
nota2 =  int(input('Informe a nota do 2° Bimestre (0-100): '))
media = (nota1 + nota2) / 2
if media >= 60:
  print(f"Você foi aprovada com média {media}")
else:
  print(f"Você não foi aprovado, sua média é {media}")

