# 🍇 API Vitivinicultura Embrapa - Tech Challenge FIAP

Esta API foi desenvolvida como parte do **Tech Challenge da FIAP**. Seu objetivo é disponibilizar publicamente os dados de vitivinicultura do Brasil, a partir do site da **Embrapa**, permitindo análises e integração com futuros modelos de Machine Learning.


## 🧑‍💻 Desenvolvido por

- `Gabriel Fernandes - RM362747`
- `Jean Franco do Nascimento - RM364515`
- `Kauê Braz - RM362598`
- `Kaue Santana - RM363168`
- `Thomas Nícolas - RM362762`


## 🚀 Link da API em Produção

Acesse a documentação via Swagger:  
👉 [https://embrapa-fiap.onrender.com/docs](https://embrapa-fiap.onrender.com/docs)

## 🧩 Arquitetura e Fluxo

![Diagrama de Arquitetura](dfd.png)

## 🔐 Autenticação

A autenticação é feita via **JWT**.  
Inclua no cabeçalho da requisição:

```http
Authorization: Bearer <seu_token_aqui>
```

## 🧪 Testando a API

Você pode utilizar o Swagger UI, **Postman** ou **Insomnia** para testar a API.  
Não se esqueça de gerar e usar o token JWT antes de acessar os dados.

## 📚 Documentação

### Endpoints

- [Autenticação](#autenticação)
- [Usuários](#usuários)
- [Produção](#produção)
- [Processamento](#processamento)
- [Comercialização](#comercialização)
- [Importação](#importação)
- [Exportação](#exportação)

---

### Autenticação

`POST` /auth/createToken

Gera tokens de acesso e refresh

#### Corpo da Requisição

| campo | tipo | obrigatório | descrição
|:---:|:---:|:---:|:---:|
| `username`|string |✅| Nome de usuário.
| `password`|string |✅| Senha de usuário.

```js
{
  "username": "usuario_exemplo",
  "password": "senha_secreta"
}
```

#### Exemplo de resposta
```js
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Tokens gerados com sucesso
| `401`  | Credenciais inválidas

---

`POST` /auth/create/refreshToken

Renova access token

#### Corpo da Requisição

| campo | tipo | obrigatório | descrição
|:---:|:---:|:---:|:---:|
| `refresh_token`|string |✅| Token de acesso.

```js
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### Exemplo de resposta
```js
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Novo access token gerado
| `401`  | Refresh token inválido ou expirado

---

### Usuários

`POST` /auth/createUser

Registra um novo usuário no sistema


#### Corpo da Requisição

| campo | tipo | obrigatório | descrição
|:---:|:---:|:---:|:---:|
| `username`|string |✅| Nome de usuário.
| `password`|string |✅| Senha de usuário.

```js
{
  "username": "usuario_exemplo",
  "password": "senha_secreta"
}
```

#### Exemplo de resposta
```js
{
  "username": "novo_usuariow",
  "message": "User created successfully"
}
```

#### Código de Status

| código | descrição
|---     | ---
| `201`  | Usuário criado com sucesso
| `400`  | Usuário já existe
| `500`  | Erro interno no servidor

---

`DELETE` /auth/user/{user_id}

Deleta um usuário existente (requer autenticação)

#### Exemplo de resposta
```js
{
  "message": "User deleted successfully"
}
```

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Usuário removido com sucesso
| `401`  | Não autorizado
| `404`  | Usuário não encontrado

### Produção

`GET` /producao/{year}

`GET` /producao

Retorna uma lista de registros de produção agrícola filtrados pelo ano solicitado ou intervalo de anos

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Dados de produção encontrados
| `400`  | Intervalo inválido ou Ano inválido
| `401`  | Não autorizado
| `500`  | Erro interno no servidor

---

### Processamento

`GET` /processamento/viniferas/{year}

`GET` /processamento/viniferas

Dados de processamento de uvas viníferas

`GET` /processamento/americanas/{year}

`GET` /processamento/americanas

Dados de processamento de uvas americanas

`GET` /processamento/uva/{year}

`GET` /processamento/uva

Dados de processamento de uvas de mesa

`GET` /processamento/semClass/{year}

`GET` /processamento/semClass

Dados sem classificação

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Dados encontrados
| `400`  | Ano inválido
| `500`  | Erro interno no servidor

---

### Comercialização


`GET` /comercializacao/{year}

`GET` /comercializacao

Retorna dados de comercialização

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Dados encontrados
| `400`  | Intervalo inválido ou Ano inválido
| `401`  | Não autorizado
| `500`  | Erro interno no servidor

---

### Importação

`GET` `/importacao/vinhosMesa/{year}`

`GET` `/importacao/vinhosMesa`

Dados de importação de vinhos de mesa

`GET` `/importacao/espumantes/{year}`

`GET` `/importacao/espumantes`

Dados de importação de espumantes

`GET` `/importacao/uvasFrescas/{year}`

`GET` `/importacao/uvasFrescas`

Dados de importação de uvas frescas

`GET` `/importacao/uvasPassas/{year}`

`GET` `/importacao/uvasPassas`

Dados de importação de uvas passas

`GET` `/importacao/sucoUva/{year}`

`GET` `/importacao/sucoUva`

Dados de importação de suco de uva

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Dados encontrados
| `400`  | Intervalo inválido ou Ano inválido
| `401`  | Não autorizado
| `500`  | Erro interno no servidor

---

### Exportação

`GET` `/exportacao/vinhosMesa/{year}`

`GET` `/exportacao/vinhosMesa`

Dados de exportação de vinhos de mesa por intervalo

`GET` `/exportacao/espumantes/{year}`

`GET` `/exportacao/espumantes`

Dados de exportação de espumantes por intervalo

`GET` `/exportacao/uvasFrescas/{year}`

`GET` `/exportacao/uvasFrescas`

Dados de exportação de uvas frescas por intervalo

`GET` `/exportacao/sucoUva/{year}`

`GET` `/exportacao/sucoUva`

Dados de exportação de suco de uva por intervalo

#### Código de Status

| código | descrição
|---     | ---
| `200`  | Dados encontrados
| `400`  | Intervalo inválido ou Ano inválido
| `401`  | Não autorizado
| `500`  | Erro interno no servidor

## 📄 Licença

Este projeto é apenas para fins educacionais e segue a licença MIT.
