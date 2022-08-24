from Util.ConnectDB import ConnectMySQL
from Util.CrudHelper import CrudHelper


class Crud:

    def __init__(self):
        self.conexao = ConnectMySQL()
        self.helper = CrudHelper()
        self.sql = []

    def limparSQL(self):
        self.sql = []

    def create(self, table):
        self.limparSQL()
        self.sql.append("INSERT INTO")
        self.sql.append(table)
        return self

    def select(self, f):
        self.limparSQL()
        self.sql.append("SELECT")
        self.sql.append(self.helper.formatarColunasSQL(f))
        return self

    def update(self, table):
        self.limparSQL()
        self.sql.append("UPDATE")
        self.sql.append(table)
        return self

    def delete(self):
        self.limparSQL()
        self.sql.append("DELETE")
        return self

    def set(self, f, v):
        self.sql.append("SET")
        self.sql.append(self.helper.formatarCamposEValoresSQL(f, v))
        return self

    def fields(self, f):
        self.sql.append(self.helper.formatarCamposSQL(f))
        return self

    def de(self, tabela):
        self.sql.append("FROM")
        self.sql.append(tabela)
        return self

    def values(self, v):
        self.sql.append("VALUES")
        self.sql.append(self.helper.formatarValoresSQL(v))
        return self

    def join(self, table):
        self.sql.append("JOIN")
        self.sql.append(table)
        return self

    def innerJoin(self, table):
        return self.join(table)

    def leftJoin(self, table):
        self.sql.append("LEFT JOIN")
        self.sql.append(table)
        return self

    def rightJoin(self, table):
        self.sql.append("RIGHT JOIN")
        self.sql.append(table)
        return self

    def on(self, field):
        self.sql.append(field)
        return self

    def igualA(self, field):
        self.sql.append("=")
        self.sql.append(field)
        return self

    def pareceCom(self, field):
        self.sql.append("LIKE")
        self.sql.append(field)
        return self

    def maiorQue(self, field):
        self.sql.append(">")
        self.sql.append(field)
        return self

    def menorQue(self, field):
        self.sql.append("<")
        self.sql.append(field)
        return self

    def maiorIgualQue(self, field):
        self.sql.append(">=")
        self.sql.append(field)

    def menorIgualQue(self, field):
        self.sql.append("<=")
        self.sql.append(field)
        return self

    def diferenteQue(self, field):
        self.sql.append("<>")
        self.sql.append(field)
        return self

    def e(self, field):
        self.sql.append("AND")
        self.sql.append(field)
        return self

    def ou(self):
        self.sql.append("OR")
        return self

    def ehNulo(self, field):
        self.sql.append(field)
        self.sql.append("IS NULL")
        return self

    def onde(self, field):
        self.sql.append("WHERE")
        self.sql.append(field)
        return self

    def campo(self, field):
        self.sql.append(field)
        return self

    def getSQL(self):
        return self.helper.fomatarCommandosSQL(self.sql)

    def isSelect(self):
        return self.sql[0] == "SELECT"

    def executar(self, commit=False):
        cursor = self.conexao.getCursor()
        response = cursor.execute(self.getSQL())

        if(not self.isSelect()):
            self.conexao.commit()
            return response

        return cursor.fetchall()
