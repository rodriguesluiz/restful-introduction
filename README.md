# restful-introduction

# API de Sorvetes

Este repositório é parte da aula "Elementos e Funcionamento do REST - Transferência de Estado Representacional", ministrada por Luiz Antonio Lima Rodrigues, candidato à vaga _Ciência da Computação- Sistemas de informação_, no contexto da Prova Didática do edital Nº 001/2024 - CPPS.

Este repositório contém uma API simples para manipulação de dados de sorvetes utilizando FastAPI e Pydantic. Seu objetivo é permitir a introdução de um exemplo prático de API RESTful, bem como possibilitar a discussão da implementação de uma API baseada em REST.

## Dependências

Para executar a API, é necessário usar um ambiente virtual com seguintes dependências instaladas:

- Python 3.7 ou superior
- FastAPI
- Uvicorn
- Pydantic

## Instruções para Execução

Para executar a API, abra o PowerShell na pasta do projeto e siga os passos abaixo:

1. Ative o ambiente virtual:
   ```bash
   .venv/Scripts/Activate.ps1

2. Inicialize o servidor:
   ```bash
   uvicorn api:app --reload

3. Acesse o servidor em seu navegador:
   ```bash
   http://127.0.0.1:8000

# Importando Bibliotecas
A API utiliza as seguintes bibliotecas:
- FastAPI para criação da API.
- Pydantic para modelagem de dados.

# Funcionalidades

## Hello World
O endpoint raiz da API exibe uma mensagem "Hello World".

- Endpoint: /
- Método: GET

## CRUD de Sorvetes
A API implementa as operações CRUD (Create, Read, Update, Delete) para dados de sorvetes.

- Modelagem dos dados de sorvetes com Pydantic.
- Dados simulados de sorvetes para fins de exemplo.

Recuperar todos os sorvetes
- Endpoint: /sorvetes/
- Método: GET
- Retorna todos os sorvetes cadastrados.

Criar um novo sorvete
- Endpoint: /sorvetes/
- Método: POST
- Adiciona um novo sorvete à lista de sorvetes cadastrados.

Atualizar um sorvete
- Endpoint: /sorvetes/{sorvete_id}/
- Método: PUT
- Atualiza as informações de um sorvete existente com base no ID fornecido.

Deletar um sorvete
- Endpoint: /sorvetes/{sorvete_id}/
- Método: DELETE
- Remove um sorvete da lista com base no ID fornecido.
