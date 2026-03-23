ant = 1
atual = 1
prox = ant + atual
soma = 0
soma += prox
print(ant, atual, end = ' ')
while soma < 580:
  print(prox, end = ' ')
  ant = atual
  atual = prox
  prox = ant + atual
  soma += prox
