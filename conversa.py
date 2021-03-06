# -*- coding: utf-8 -*-
"""Conversa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eg_HtfL4wSY9mX17qg-Upf4B0jL5Vk38
"""

from datetime import datetime, timezone, timedelta

diference = timedelta(hours=-3)

dt = datetime.now()
fuso_horario = timezone(diference)

dt_br = dt.astimezone(fuso_horario)
dt_br_str = dt_br.strftime('%d/%m/%Y %H:%M')

print(dt.hour - 3)

greetings = ["olá", "oi", "Olá", "Oi", "Ola", "ola"]

sim = ["Sim", "sim", "si", "Si", "S", "s"]
nao = ["Não", "nao", "Nao", "não", "no", "No", "N", "n"]
start = input()

if (start in greetings and dt.hour - 3 < 12):
  print("Olá, bom dia!")

  name_ask = input("Meu nome é Charlie, qual o seu nome? \n")
  your_name = name_ask.split()
  name = your_name[-1]

  hau = input(f"Ótimo {name}! Mas me diga, está tudo bem com você? \n")

  if (hau in sim):
    print("que bom!:)") 

  elif (hau in nao):
    sure = input("Quer conversar sobre? \n")
    
    if (sure in nao):
      print("Tudo bem, mas se precisar estou aqui!\n")

    if (sure in sim):
      tell = input("Então me conte o que te incomoda\n")

      print("É complicado")

elif (dt.hour - 3 > 12 and dt.hour - 3 < 18):
  print("Olá, boa tarde!")

  name_ask = input("Meu nome é Charlie, qual o seu nome? \n")
  your_name = name_ask.split()
  name = your_name[-1]

  hau = input(f"Ótimo {name}! Mas me diga, está tudo bem com você? \n")

  if (hau in sim):
    print("que bom!:)") 

  elif (hau in nao):
    sure = input("Quer conversar sobre? \n")
    
    if (sure in nao):
      print("Tudo bem, mas se precisar estou aqui!\n")

    if (sure in sim):
      tell = input("Então me conte o que te incomoda\n")

      print("É complicado")

elif (dt.hour - 3 > 18):
  print("Olá, boa noite!")

  name_ask = input("Meu nome é Charlie, qual o seu nome? \n")
  your_name = name_ask.split()
  name = your_name[-1]

  hau = input(f"Ótimo {name}! Mas me diga, está tudo bem com você? \n")

  if (hau in sim):
    print("que bom!:)") 

  elif (hau in nao):
    sure = input("Quer conversar sobre? \n")
    
    if (sure in nao):
      print("Tudo bem, mas se precisar estou aqui!\n")

    if (sure in sim):
      tell = input("Então me conte o que te incomoda\n")

      print("É complicado")

else:  
  print("Bye")