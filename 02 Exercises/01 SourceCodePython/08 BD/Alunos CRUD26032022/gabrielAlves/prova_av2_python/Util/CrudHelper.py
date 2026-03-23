class CrudHelper:

	def __init__(self):
		pass

	def colocarEntreParenteses(self, s):
		return "({})".format(s)

	def separarValoresPorVirgula(self, v):
		return ", ".join(v);

	def colacarEntreAspas(self, v):
		for i in range(len(v)):
			v[i] = "'{}'".format(v[i])
		return v

	def formatarCamposSQL(self, v):
		v = self.separarValoresPorVirgula(v)
		v = self.colocarEntreParenteses(v)
		return v

	def formatarColunasSQL(self, v):
		v = self.separarValoresPorVirgula(v)
		return v

	def formatarValoresSQL(self, v):
		v = self.colacarEntreAspas(v)
		v = self.separarValoresPorVirgula(v)
		v = self.colocarEntreParenteses(v)
		return v

	def fomatarSetencaUpdate(self, f, v):
		return "{} = {}".format(f, v)

	def formatarCamposEValoresSQL(self, f, v):
		campos = []
		v = self.colacarEntreAspas(v)

		for i in range(len(f)):
			campos.append(self.fomatarSetencaUpdate(f[i], v[i]))

		return self.separarValoresPorVirgula(campos)


	def fomatarCommandosSQL(self, v):
		return " ".join(v)