import os
def tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scoreJogador,scoreComputador):
	os.system("clear")
	print("\t\t\tScores: Player:",scoreJogador,"  Computador",scoreComputador)
	print("\n\t\t  1   2   3   4   5   6   7")
	print("\t\t ___________________________")
	print("\t\t║",coluna1[0],"║",coluna2[0],"║",coluna3[0],"║",coluna4[0],"║",coluna5[0],"║",coluna6[0],"║",coluna7[0],"║")
	print("\t\t ___________________________")
	print("\t\t║",coluna1[1],"║",coluna2[1],"║",coluna3[1],"║",coluna4[1],"║",coluna5[1],"║",coluna6[1],"║",coluna7[1],"║")
	print("\t\t ___________________________")
	print("\t\t║",coluna1[2],"║",coluna2[2],"║",coluna3[2],"║",coluna4[2],"║",coluna5[2],"║",coluna6[2],"║",coluna7[2],"║")
	print("\t\t ___________________________")
	print("\t\t║",coluna1[3],"║",coluna2[3],"║",coluna3[3],"║",coluna4[3],"║",coluna5[3],"║",coluna6[3],"║",coluna7[3],"║")
	print("\t\t ___________________________")
	print("\t\t║",coluna1[4],"║",coluna2[4],"║",coluna3[4],"║",coluna4[4],"║",coluna5[4],"║",coluna6[4],"║",coluna7[4],"║")
	print("\t\t ___________________________")
	print("\t\t║",coluna1[5],"║",coluna2[5],"║",coluna3[5],"║",coluna4[5],"║",coluna5[5],"║",coluna6[5],"║",coluna7[5],"║")
	print("\t\t ___________________________")

	print("\n\n\t\t Sair = 99")

def completo(col1,col2,col3,col4,col5,col6,col7):  #Verifica se completou o tabuleiro se encontrar o espaço retorna True
	i = 0
	retorno = True
	while i < 6:
		if (col1[i] == " " or col2[i] == " " or col3[i] == " " or col4[i] == " " or col5[i] == " " or col6[i] == " " or col7[i] == " "):
			retorno = True
			i = 6
		else:
			retorno = False
		i += 1
	return retorno

def posiciona(coluna):  #Posiciona a jogada no local certo para não substituir o já existente e tbm
						# retorna se ela tiver completa com valor -1
	if (coluna[0] != " " and coluna[1] != " " and coluna[2] != " " and coluna[3] != " " and coluna[4] != " " and coluna[5] != " "):
		return -1
	else:
		if(coluna[5] == " "):
			return 5
		else:
			if (coluna[4] == " "):
				return 4
			else:
				if (coluna[3] == " "):
					return 3
				else:
					if (coluna[2] == " "):
						return 2
					else:
						if (coluna[1] == " "):
							return 1
						else:
							if (coluna[0] == " "):
								return 0

def regulaPosicao(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,jogada,simUser,scorejogador,scoreComputador):
	preenchida = 0
	if(jogada == 1):
		posicao = posiciona(coluna1)
		if (posicao == -1):
			tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scorejogador,scoreComputador)
			preenchida = -1
		else:
			coluna1[posicao]= simUser
			preenchida = 0
	elif(jogada == 2):
		posicao = posiciona(coluna2)
		if (posicao == -1):
			tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scorejogador,scoreComputador)
			preenchida = -1
		else:
			coluna2[posicao]=simUser
			preenchida = 0
	elif(jogada == 3):
		posicao = posiciona(coluna3)
		if (posicao == -1):
			tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scorejogador,scoreComputador)
			preenchida = -1
		else:
			coluna3[posicao] = simUser
			preenchida = 0
	elif(jogada == 4):
		posicao = posiciona(coluna4)
		if (posicao == -1):
			tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scorejogador,scoreComputador)
			preenchida = -1
		else:
			coluna4[posicao] = simUser
			preenchida = 0
	elif(jogada == 5):
		posicao = posiciona(coluna5)
		if (posicao == -1):
			tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scorejogador,scoreComputador)
			preenchida = -1
		else:
			coluna5[posicao] = simUser
			preenchida = 0
	elif(jogada == 6):
		posicao = posiciona(coluna6)
		if (posicao == -1):
			tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scorejogador,scoreComputador)
			preenchida = -1
		else:
			coluna6[posicao] = simUser
			preenchida = 0
	else:
		posicao = posiciona(coluna7)
		if (posicao == -1):
			tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scorejogador,scoreComputador)
			preenchida = -1
		else:
			coluna7[posicao] = simUser
			preenchida = 0
	return preenchida



def limpaTela(): #############
	import platform  #########  ESSA FUNÇÃO LER O SISTEMA OPERACIONAL
	comando = " "    #########	E RETORNA O COMANDO PARA LIMPAR A TELA
	so = platform.system()

	if (so == "Linux"):
		comando = "clear"
	else:
		comando = "cls"
	return comando


def verificaPontuacao(col1,col2,col3,col4,col5,col6,col7,simbolo):
	pontos = 00
	novaLista = []
	novaLista.append(col1)
	novaLista.append(col2)
	novaLista.append(col3)
	novaLista.append(col4)
	novaLista.append(col5)
	novaLista.append(col6)
	novaLista.append(col7)
	credito = 0
	#print("novaLista", novaLista)
	for i in range(7):                      ###
		for j in range(6):					##
			if (novaLista[i][j] == simbolo):##  VERTICAL
				credito +=1					##
				if (credito == 3):			##
					pontos += 200    		##
			else:
				credito = 0

	i = 0
	while i < 6:
		for j in range(7):
			if (novaLista[j][i] == simbolo):
				credito += 1
				if (credito == 3):
					pontos += 200
			else:
				credito = 0
		i+= 1
	nulo = "-"
	diagonal1 = [novaLista[0][2],novaLista[1][3],novaLista[2][4],novaLista[3][5],nulo,nulo] #roxo
	diagonal2 = [novaLista[0][1],novaLista[1][2],novaLista[2][3],novaLista[3][4],novaLista[4][5],nulo] #verde escuro
	diagonal3 = [novaLista[0][0],novaLista[1][1],novaLista[2][2],novaLista[3][3],novaLista[4][4],novaLista[5][5]] #amarelo
	diagonal4 = [novaLista[1][0],novaLista[2][1],novaLista[3][2],novaLista[4][3],novaLista[5][4],novaLista[6][5]] # vermelho
	diagonal5 = [novaLista[2][0],novaLista[3][1],novaLista[4][2],novaLista[5][3],novaLista[6][4],nulo] #azul claro
	diagonal6 = [novaLista[3][0],novaLista[4][1],novaLista[5][2],novaLista[6][3],nulo,nulo] #cinza
	diagonal7 = [novaLista[3][5],novaLista[4][4],novaLista[5][3],novaLista[6][2],nulo,nulo] #vinho
	diagonal8 = [novaLista[2][5],novaLista[3][4],novaLista[4][3],novaLista[5][2],novaLista[6][1],nulo] #laranja
	diagonal9 = [novaLista[1][5],novaLista[2][4],novaLista[3][3],novaLista[4][2],novaLista[5][1],novaLista[6][0]] #rosa
	diagonal10 = [novaLista[0][5],novaLista[1][4],novaLista[2][3],novaLista[3][2],novaLista[4][1],novaLista[5][0]] #ciano
	diagonal11 = [novaLista[0][4],novaLista[1][3],novaLista[2][2],novaLista[3][1],novaLista[4][0],nulo] # verde craro
	diagonal12 = [novaLista[0][3],novaLista[1][2],novaLista[2][1],novaLista[3][0],nulo,nulo] #preta
	diagonal13 = [novaLista[0][3],novaLista[1][4],novaLista[2][5]]
	diagonal14 = [novaLista[0][2],novaLista[1][1],novaLista[2][0]]
	diagonal15 = [novaLista[4][0],novaLista[5][1],novaLista[6][2]]
	diagonal16 = [novaLista[6][3],novaLista[5][4],novaLista[4][5]]

	credito = 0
	for i in range(6):

		if (diagonal1[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0

	for i in range(6):
		if (diagonal2[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal3[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0

	for i in range(6):
		if (diagonal4[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal5[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal6[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal7[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal8[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal9[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal10[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal11[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(6):
		if (diagonal12[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(3):
		if (diagonal13[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(3):
		if (diagonal14[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(3):
		if (diagonal15[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	for i in range(3):
		if (diagonal16[i] == simbolo):
			credito += 1
			if (credito >=3):
				pontos += 200
		else:
			credito = 0
	return pontos

def verificaGanhou(col1,col2,col3,col4,col5,col6,col7,simbolo):

	win = True
	novaLista = []
	novaLista.append(col1)
	novaLista.append(col2)
	novaLista.append(col3)
	novaLista.append(col4)
	novaLista.append(col5)
	novaLista.append(col6)
	novaLista.append(col7)
	credito = 0
	for i in range(7):
		credito = 0                      ###
		for j in range(6):					##
			if (novaLista[i][j] == simbolo):##  VERTICAL
				credito +=1
				if (credito == 4):

					win = False			    ##
			elif(novaLista[i][j] != simbolo):
				credito = 0

	i = 0

	while (i < 6):
		credito = 0
		for j in range(7):					###
			if (novaLista[j][i] == simbolo):###
				credito += 1				###	HORIZONTAL
				if (credito >= 4):			###
					win = False

			else:
				credito = 0
		i += 1
	nulo = "-"
	diagonal1 = [novaLista[0][2],novaLista[1][3],novaLista[2][4],novaLista[3][5],nulo,nulo] #roxo
	diagonal2 = [novaLista[0][1],novaLista[1][2],novaLista[2][3],novaLista[3][4],novaLista[4][5],nulo] #verde escuro
	diagonal3 = [novaLista[0][0],novaLista[1][1],novaLista[2][2],novaLista[3][3],novaLista[4][4],novaLista[5][5]] #amarelo
	diagonal4 = [novaLista[1][0],novaLista[2][1],novaLista[3][2],novaLista[4][3],novaLista[5][4],novaLista[6][5]] # vermelho
	diagonal5 = [novaLista[2][0],novaLista[3][1],novaLista[4][2],novaLista[5][3],novaLista[6][4],nulo] #azul claro
	diagonal6 = [novaLista[3][0],novaLista[4][1],novaLista[5][2],novaLista[6][3],nulo,nulo] #cinza
	diagonal7 = [novaLista[3][5],novaLista[4][4],novaLista[5][3],novaLista[6][2],nulo,nulo] #vinho
	diagonal8 = [novaLista[2][5],novaLista[3][4],novaLista[4][3],novaLista[5][2],novaLista[6][1],nulo] #laranja
	diagonal9 = [novaLista[1][5],novaLista[2][4],novaLista[3][3],novaLista[4][2],novaLista[5][1],novaLista[6][0]] #rosa
	diagonal10 = [novaLista[0][5],novaLista[1][4],novaLista[2][3],novaLista[3][2],novaLista[4][1],novaLista[5][0]] #ciano
	diagonal11 = [novaLista[0][4],novaLista[1][3],novaLista[2][2],novaLista[3][1],novaLista[4][0],nulo] # verde craro
	diagonal12 = [novaLista[0][3],novaLista[1][2],novaLista[2][1],novaLista[3][0],nulo,nulo] #preta

	credito = 0
	for i in range(6):

		if (diagonal1[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0

	for i in range(6):
		if (diagonal2[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal3[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0

	for i in range(6):
		if (diagonal4[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal5[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal6[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal7[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal8[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal9[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal10[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal11[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0
	for i in range(6):
		if (diagonal12[i] == simbolo):
			credito += 1
			if (credito >=4):
				win = False
		else:
			credito = 0

	i = 0
	while (i > 6):
		credito = 0
		for j in range(7):
			if (novaLista[j][i] == simbolo):
				credito += 1
				if (credito >= 4):
					win = False
			else:
				credito = 0
		i += 1

	return win
