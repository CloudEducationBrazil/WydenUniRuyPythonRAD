import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento / qtde_produtos

# configurar as informações do seu e-mail
email.To = "macielgiudice@gmail.com; macielgiudice@gmail.com"
email.Subject = "E-mail automático do Python"
email.HTMLBody = f"""
<p>Olá Klaus, aqui é o código Python</p>
<p>O seu trabalho foi entregue {trabalho}</p>
<p>Seu resultado estará disponivel no portal</p>
<p>Abs,</p>
<p>Código Python</p>
"""
# mensagem acima apenas de exemplo

# anexo = "C://Users/klaus/Downloads/trabalho.xlsx"
# email.Attachments.Add(anexo)

email.Send()
print("Email Enviado")