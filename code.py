def meuIn(num, valores):
    for i in valores:
        if(i == num):
            return True
        if(i > num):
            return False
    return False

def verificaValores(valores):

    if(not meuIn(1, valores)):
        return 1

    return -1

num = int(input())
entrada = input().split()

valores = [int(valor) for valor in entrada]
valores.sort()

print(verificaValores(valores))
	 	 		  	  			 	  	 	 		 	  	 	