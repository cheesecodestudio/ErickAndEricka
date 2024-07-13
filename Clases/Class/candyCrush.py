from Colors import colors
from Candy import Candy
from Especial import Especial
# Una matriz es una lista de listas

matriz = [[1,2,3],[1,2,3],[1,2,3]]

Confites = {
	"azul": Candy(colors.fg.blue),
	"verde": Candy(colors.fg.green),
	"rojo": Candy(colors.fg.red),
	"amarillo": Candy(colors.fg.yellow),
	"especial": Especial(colors.fg.purple)
}

# matriz 3x3 forma #1
candyMatriz = [
	[Confites["azul"], Confites["verde"], Confites["rojo"]],
	[Confites["amarillo"], Confites["especial"], Confites["azul"]],
	[Confites["verde"], Confites["amarillo"], Confites["azul"]]
]

# matriz 3x3 forma #2
candyMatriz2 = [
	[Candy(colors.fg.blue), Candy(colors.fg.green), Candy(colors.fg.blue)],
	[Candy(colors.fg.red), Candy(colors.fg.green), Especial(colors.fg.purple)],
	[Candy(colors.fg.yellow), Candy(colors.fg.red), Candy(colors.fg.yellow)]
]

matrizTexto = ""
for fila in candyMatriz:
	for confite in fila:
		matrizTexto += f"{confite.Color}{confite.Forma} "
	matrizTexto += "\n"

print(matrizTexto)
print(colors.reset)
