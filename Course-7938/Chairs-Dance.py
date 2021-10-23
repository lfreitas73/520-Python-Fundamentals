import random
import time

Cadeiras = 9
nomes = ["João", "Marcos", "Silva", "Ana", "Vera", "Paulo", "Luciano", "Anselmo", "Ricardo", "Felipe"]
while Cadeiras > 0:
    id_remove = random.randint(0,Cadeiras)
    nomes.pop(id_remove)
    Cadeiras-=1
    print(nomes)
    time.sleep(1)


       

    


