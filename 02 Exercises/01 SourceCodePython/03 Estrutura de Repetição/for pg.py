soma = 0
termo = 3

for exp in range(1, 9):
    print(termo ** exp, end = ' ')


soma = 0
termo = 3
a1 = 3
r = 3
# 3, 9, 27, 81, 243, 729, 2187, 6561
for i in range(8):
    termo = a1 * (r ** i) 
    print(termo, end = ' ')