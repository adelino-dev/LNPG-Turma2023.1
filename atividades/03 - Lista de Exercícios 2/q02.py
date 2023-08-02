cod = input("Digite o código de usuário:")

if cod != '1234':
  print("Usuário inválido!")

else:
  senha = input("Senha:")

  if senha == '9999':
    print("Acesso permitido")

  else:
    print("senha incorreta")
