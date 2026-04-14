# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Desenvolver uma API REST simples com FastAPI para praticar rotas, operacoes CRUD, validacao de dados e organizacao de respostas JSON. Ao final, a aplicacao deve expor endpoints claros e testaveis para cadastrar, listar, atualizar e remover recursos.

## 📝 Tasks

### 🛠️ Criar uma API REST basica

#### Description
Construa uma aplicacao com FastAPI para gerenciar uma colecao simples de itens, como livros, tarefas ou produtos. A API deve rodar localmente, aceitar requisicoes HTTP e retornar respostas em JSON para operacoes basicas de criacao, consulta, atualizacao e remocao.

#### Requirements
Completed program should:

- Criar uma aplicacao FastAPI executavel localmente.
- Implementar pelo menos um endpoint `GET` para listar todos os itens.
- Implementar pelo menos um endpoint `GET` para buscar um item pelo identificador.
- Implementar um endpoint `POST` para adicionar um novo item.
- Implementar um endpoint `PUT` ou `PATCH` para atualizar um item existente.
- Implementar um endpoint `DELETE` para remover um item.
- Retornar dados em formato JSON em todas as respostas.

### 🛠️ Validar dados e documentar o comportamento da API

#### Description
Melhore a API utilizando modelos de dados com FastAPI para validar entradas e manter o comportamento consistente. Teste os endpoints com a documentacao automatica da ferramenta e trate cenarios em que um recurso nao exista.

#### Requirements
Completed program should:

- Usar modelos de dados para validar os campos recebidos nas requisicoes.
- Retornar codigo de status apropriado para sucesso, criacao e recurso nao encontrado.
- Exibir mensagens claras de erro quando um item nao for encontrado.
- Permitir testar a API pela interface automatica de documentacao do FastAPI.
- Organizar os dados de forma simples, como uma lista em memoria ou estrutura equivalente.
