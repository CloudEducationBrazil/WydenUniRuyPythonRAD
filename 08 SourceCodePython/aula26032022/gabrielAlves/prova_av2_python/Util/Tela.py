import os

class Tela:

	def __init__(self):
		pass

	def home(self):
		print("===================================================")
		print("|                                                 |")
		print("|               MATRÍCULA UNIRUY 22.2             |")
		print("|                                                 |")
		print("===================================================")


	def menu(self):
		print("====================== MENU =======================")
		print("|                                                 |")
		print("|         *  digite o número da opção *           |")
		print("|                                                 |")
		print("| 1 - Sala de Matrícula                           |")
		print("| 2 - Sobre                                       |")
		print("| 3 - Sair                                        |")
		print("|                                                 |")
		print("===================================================")

	def alunos(self):
		self.limpar()
		print("=============== SALA DE MATRÍCULA =================")
		print("|                                                 |")
		print("|         *  digite o número da opção *           |")
		print("|                                                 |")
		print("| 1 - Matricular aluno                            |")
		print("| 2 - Listar alunos matriculados                  |")
		print("| 3 - Atualizar cadastro do aluno                 |")
		print("| 4 - Excluir aluno                               |")
		print("| 5 - Voltar                                      |")
		print("|                                                 |")
		print("===================================================")

	def listarAlunos(self):
		self.limpar()
		print("========== LISTA DE ALUNOS MATRICULADOS ===========")
		print("|                                                 |")
		print("===================================================")

	def cadastroAluno(self):
		self.limpar()
		print("============= MATRÍCULA DE ALUNO ==================")
		print("|                                                 |")
		print("===================================================")

	def atualizarAluno(self):
		self.limpar()
		print("=============== ATUALIZAR ALUNO ===================")
		print("|                                                 |")
		print("===================================================")

	def excluirAluno(self):
		self.limpar()
		print("================= EXCLUIR ALUNO ===================")
		print("|                                                 |")
		print("===================================================")		

	def sobre(self):
		self.limpar()
		print("====================== SOBRE ======================")
		print("|                                                 |")
		print("| Projeto desenvolvido para a AV2 da disciplina   |")
		print("| paradigmas de linguagem de programação.         |")
		print("|                                                 |")
		print("| Discente: Gabriel Alves Nunes Dos Santos        |")
		print("| RA: 201951143108                                |")
		print("|                                                 |")	                                                
		print("| Docente: Heleno Cardoso Filho                   |")
		print("|                                                 |")
		print("===================================================")

	def linha(self):
		print("---------------------------------------------------")

	def sair(self):
		self.limpar()
		print("Tchau!")

	def limpar(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def opcaoInvalida(self):
		print("Opção inválida, tente novamente...")

	def nomeInvalido(self):
		print("Digite um nome válido...")
	
	def raInvalido(self):
		print("Digite somente números para que o RA seja válido...")

	def idInvalido(self):
		print("Digite somente números para que o ID seja válido...")

	def erroCadastrarAluno(self):
		print("Algo deu errado ao tentar cadastar o aluno, tente novamente mais tarde...")

	def sucessoCadastrarAluno(self):
		print("Aluno cadastrado com sucesso!")

	def erroAtualizarAluno(self):
		print("Algo deu errado ao tentar atualizar o aluno, tente novamente mais tarde...")		
	
	def sucessoAtualizarAluno(self):
		print("Aluno atualizado com sucesso!")
	
	def erroExcluirAluno(self):
		print("Erro ao tentar excluir o aluno, tente novamente mais tarde.")

	def sucessoExcluirAluno(self):
		print("Aluno excluído com sucesso!")

	def idAlunoInexistente(self):
		print("Atenção! O ID digitado não é válido!")