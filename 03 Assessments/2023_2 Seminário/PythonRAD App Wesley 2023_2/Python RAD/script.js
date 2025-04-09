function criarUsuario() {
  // Obter os dados do formulário
  const nome = document.querySelector('input[name="nome"]').value;
  const email = document.querySelector('input[name="email"]').value;
  const senha = document.querySelector('input[name="senha"]').value;

  // Criar um objeto com os dados do usuário
  const usuario = {
    nome,
    email,
    senha
  };

  // Fazer uma requisição POST para a API
  fetch('/usuario', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(usuario)
  })
  .then(response => {
    // Verificar o status da requisição
    if (response.status === 201) {
      // A requisição foi bem-sucedida
      console.log('Usuário criado com sucesso!');
    } else {
      // A requisição falhou
      console.log('Erro ao criar usuário!');
    }
  })
  .catch(error => {
    console.error('Erro na requisição:', error);
  });
}
