import matplotlib.pyplot as plt

retaSaida = []
entrada = []
saida = []
cost = []
x = []

epocas = 12000
alpha = 0.001

#--------------------- File Systeam ------------------------`
file = open("entrada_1.txt")

for line in file:
	x.append([1,float(line.split(",")[0])])
	entrada.append(float(line.split(",")[0]))
	saida.append(float(line.split(",")[1].replace("\n","")))
file.close()

#------------------Funcao Calculo teta gradiente----------------
#Teta inicial
teta = [5,3]
tamanhoEntrada = len(entrada)

def calculo_gradiente():
	tetaAuxiliar = teta
	for j in range(0,2):
		somatorio = 0
		for i in range(0,tamanhoEntrada):
			somatorio += (teta[1]*entrada[i]+teta[0]-saida[i])*x[i][j]
		tetaAuxiliar[j] -= (alpha/tamanhoEntrada)*somatorio
	return tetaAuxiliar

for i in range(0,epocas):
	teta = calculo_gradiente()

print(teta)

for i in range(0,tamanhoEntrada):
	retaSaida.append(teta[1]*entrada[i]+teta[0])

plt.plot(entrada,saida,"o")
plt.plot(entrada,retaSaida)
plt.show()