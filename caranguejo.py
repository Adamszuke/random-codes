
sim = "s"
nao = "n"
talvez = "t"

resultado = "Você não é um caranguejo"

print("Sim/s, Não/n, Talvez/t")

pergunta1 = input("Você é um caranguejo? ")

if (pergunta1 == nao):

  print(resultado) 

elif (pergunta1 == sim):
  print("Você é um caranguejo")

elif (pergunta1 == talvez):

  pergunta2 = int(input("Com quantas patas você anda? "))
  
  if (pergunta2 == 8):
    pergunta3 = input("Sério? ")

    if (pergunta3 == nao or pergunta3 == sim):
       
      pergunta4 = input("Você pode ler e escrever? ")

      if (pergunta4 == sim):
        print(resultado)
        
      elif(pergunta4 == nao):
        print("Mentira você está lendo isso")
        print(resultado)
  else: 
    print(resultado)

sim = "s"
nao = "n"
