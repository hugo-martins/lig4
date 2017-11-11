import os, time,random,bibliReguladora
espaco = " "
for i in range(5):
	os.system("clear")
	time.sleep(0.4)
	                                                 
	print ("\t\t\t88           88    ,ad8888ba,               ,d8   " )
	print ("\t\t\t88                d8\"'    `\"8b            ,d888   " )
	print ("\t\t\t88           88  d8'                    ,d8\" 88   " )
	print ("\t\t\t88           88  88                   ,d8\"   88   " )
	print ("\t\t\t88           88  88      88888      ,d8\"     88   " )
	print ("\t\t\t88           88  Y8,        88      8888888888888 " )
	print ("\t\t\t88           88   Y8a.    .a88               88   " )
	print ("\t\t\t88888888888  88    `\"Y88888P\"                88   " )                           
                                                   
	time.sleep(0.4)

sair = True
while (sair):
	print("\n\n 1 - Iniciar o Jogo")
	print(" 2 - Como Jogar")
	print(" 3 - Sair")
	opcao = input("\nO Que Deseja Fazer? -->\t")

	if (opcao == "3"):
		os.system(bibliReguladora.limpaTela())
		print("   ___    _              _                       _           ")
		print("  / _ \  | |__    _ __  (_)   __ _    __ _    __| |   ___    ")
		print(" | | | | | '_ \  | '__| | |  / _` |  / _` |  / _` |  / _ \   ")
		print(" | |_| | | |_) | | |    | | | (_| | | (_| | | (_| | | (_) |  ")
		print("  \___/  |_.__/  |_|    |_|  \__, |  \__,_|  \__,_|  \___/   ")
		print("                             |___/                           ")
		print("	                      _                                ")
		print(" _ __     ___    _ __        | |   ___     __ _    __ _   _ __ ")
		print("| '_ \   / _ \  | '__|    _  | |  / _ \   / _` |  / _` | | '__|")
		print("| |_) | | (_) | | |      | |_| | | (_) | | (_| | | (_| | | |   ")
		print("| .__/   \___/  |_|       \___/   \___/   \__, |  \__,_| |_|   ")
		print("|_|                                       |___/                ")

		time.sleep(2)
		sair = False
	elif(opcao == "2"):
		os.system(bibliReguladora.limpaTela())
		arq = open('regras.txt', 'r') #
		texto = arq.read()			  # Abre o arquivo txt com as regras
		print(texto)				  #
		arq.close()

	elif(opcao == "1"):
		coluna1 = []
		coluna2 = []
		coluna3 = []
		coluna4 = []
		coluna5 = []
		coluna6 = []
		coluna7 = []
		for i in range(6):
			coluna1.append(" ")
			coluna2.append(" ")
			coluna3.append(" ")
			coluna4.append(" ")
			coluna5.append(" ")
			coluna6.append(" ")
			coluna7.append(" ")

		#print(coluna1)
		scoreComputador = 00
		scoreJogador = 00
		rodando = True
		simUser = " "
		escolha = True
		simComputador = " "
		os.system(bibliReguladora.limpaTela())
		simbolo = ""
		while(escolha):
			simbolo = input("Com qual Simbolo deseja Jogar?\n1 -> □\n2 -> ■\n\nDigite o número correspondente ao número -->  ")
			if (simbolo == "2"):
				simUser = "■"
				simComputador = "□"
				escolha = False
			elif(simbolo == "1"):
				simUser = "□"
				simComputador = "■"
				escolha = False
			else:
				os.system(bibliReguladora.limpaTela())
				print ("Opção inválida\nDigite novamente!")
		testePergunta = -1 ### Testa se a coluna já está preenchida
		testePerguntaComp = 0
		venceu = True
		while (rodando and venceu):

			while (testePergunta == -1):
				bibliReguladora.tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scoreJogador,scoreComputador)
				jogador = int(input("Escolha o número da coluna:\t"))
				if(jogador == 99):
					testePergunta = 0
					rodando = False
					if (scoreJogador > scoreComputador):
						print ("Parabéns Você ganhou por pontuação de ",scoreJogador," Contra ",scoreComputador)
					elif(scoreComputador > scoreJogador):
						print("Computador venceu por pontuação de ",scoreComputador," Contra ",scoreJogador)
					else:
							print("Empate técnico")

				elif(jogador < 1 or jogador > 7 ):
					print("Coluna não Existe\nJoque Novamente")
				else:
					testePergunta = bibliReguladora.regulaPosicao(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,jogador,simUser,scoreJogador,scoreComputador)
					if (testePergunta== -1):
						print("Coluna já está preenchida\nQual a nova Jogada?:\t")
					else:
						testePerguntaComp = -1
					scoreJogador = bibliReguladora.verificaPontuacao(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,simUser)
					venceu = bibliReguladora.verificaGanhou(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,simUser)

					if(venceu == False):
						bibliReguladora.tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scoreJogador,scoreComputador)
						for k in range(8):
							tabulacao = "\t\t\t"
							os.system(bibliReguladora.limpaTela())
							print(tabulacao,"|\     /|(  ___  )(  ____ \(  ____ \ ") 
							print(tabulacao,"| )   ( || (   ) || (    \/| (    \/ ") 
							print(tabulacao,"| |   | || |   | || |      | (__     ") 
							print(tabulacao,"( (   ) )| |   | || |      |  __)    ") 
							print(tabulacao," \ \_/ / | |   | || |      | (       ") 
							print(tabulacao,"  \___/  | (___) || (____/\| (____/\ \n") 
							print(tabulacao,"|\     /|(  ____ \( (    /|(  ____ \(  ____ \|\     /|")
							print(tabulacao,"| )   ( || (    \/|  \  ( || (    \/| (    \/| )   ( |")
							print(tabulacao,"| |   | || (__    |   \ | || |      | (__    | |   | |")
							print(tabulacao,"( (   ) )|  __)   | (\ \) || |      |  __)   | |   | |")
							print(tabulacao," \ \_/ / | (      | | \   || |      | (      | |   | |")
							print(tabulacao,"  \   /  | (____/\| )  \  || (____/\| (____/\| (___) |")
							print(tabulacao,"   \_/   (_______/|/    )_)(_______/(_______/(_______)")
							time.sleep(0.5)							
							
						
						venceu = False

					else:
				
						while (testePerguntaComp == -1 ):
							bibliReguladora.tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scoreJogador,scoreComputador)
							computador = random.randrange(7)
							print("Computador Pensando...")
							pensando = random.randrange(2)
							time.sleep(pensando)

							testePerguntaComp = bibliReguladora.regulaPosicao(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,computador,simComputador,scoreJogador,scoreComputador)
							scoreComputador = bibliReguladora.verificaPontuacao(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,simComputador)
							venceu = bibliReguladora.verificaGanhou(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,simComputador)
							testePergunta = -1
							if(venceu == False):
								os.system(bibliReguladora.limpaTela())
								bibliReguladora.tabela(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,scoreJogador,scoreComputador)
								arq = open('perdeu.txt', 'r') #
								texto = arq.read()			  # Abre o arquivo txt com cara feia
								print(texto)				  #
								arq.close()
								print("Você Perdeu")
								testePerguntaComp = 0
								testePergunta = 0


							rodando = bibliReguladora.completo(coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7)
							if (rodando == False ):
								testePergunta = 0
								if (scoreJogador > scoreComputador):
									print ("Parabéns Você ganhou por pontuação de ",scoreJogador," Contra ",scoreComputador)
								elif(scoreComputador > scoreJogador):
									print("Computador venceu por pontuação de ",scoreComputador," Contra ",scoreJogador)
								else:
									print("Empate técnico")

	else:
		os.system(bibliReguladora.limpaTela())
		print("Opção inválida\nDigite novamente sua Opção!\n")
