from Util.Tela import Tela

class Entrada:

	def __init__(self):
		self.tela = Tela()

	def ler(self, texto):
		return input(texto)

	def lerInt(self, texto):

		try:
			return int(input(texto))
		except Exception as e:
			pass

	def lerIntSemTry(self, texto):
		return int(input(texto))

	def lerOpcaoMenu(self):
		return self.lerInt("Digite o número da opção: ")

	def precioneParaVoltarMenu(self):
		return self.ler("Precione enter para voltar ao menu...")

	def lerNome(self):
		return self.ler("Digite o nome do aluno: ")
	
	def lerRa(self):
		return self.lerIntSemTry("Digite o RA do aluno: ")

	def lerId(self, sufix):
		return self.lerInt("Digite o ID do aluno {}: ".format(sufix))


	def lerNomeAluno(self):
		while True:
			nome = ''

			try:
				nome = self.lerNome()

				if nome == '':
					self.tela.nomeInvalido()
				else:
					return nome

			except Exception as e:
				self.tela.nomeInvalido()
				

	def lerRaAluno(self):
		while True:
			ra = ''

			try:
				ra = self.lerRa()
				return ra
			except Exception as e:
				self.tela.raInvalido()

	def lerIdAluno(self, sufix):
		while True:
			idAluno = ''

			try:
				idAluno = self.lerId(sufix)
				return idAluno
			except Exception as e:
				self.tela.idInvalido() 