# Portuguese Clinical NER - Disorder

Este repositório contém o código-fonte para uma aplicação de reconhecimento de entidades nomeadas (NER) clínicas. A aplicação foi desenvolvida utilizando o framework Streamlit e o modelo pré-treinado "pucpr/clinicalnerpt-disorder" para a tarefa de NER.

### Instalação

Para executar esta aplicação, é necessário ter o Docker e o Docker Compose instalados.

1.  Clone este repositório
2.  Na raiz do projeto execute o comando abaixo para criar as imagens e iniciar os contêineres:

Copy code

`make up` 

A aplicação estará disponível em [http://localhost:8501](http://localhost:8501/)

### Utilização

A aplicação possui duas funcionalidades principais: reconhecimento de entidades nomeadas e visualização de dados do paciente.

1.  Para realizar o reconhecimento de entidades nomeadas, é necessário inserir o ID do paciente e o texto do prontuário. Ao clicar no botão "Reconhecer entidades", a aplicação irá realizar a previsão utilizando o modelo pré-treinado e informar se foi detectado câncer. Os dados do paciente serão salvos em um arquivo json, caso o câncer não tenha sido detectado.
2.  Para visualizar os dados do paciente, é necessário inserir o ID do paciente e clicar no botão "Ver dados do paciente". A aplicação irá carregar os dados do paciente a partir do arquivo json correspondente e exibir na tela.

### Testes

Para executar os testes, utilize o comando abaixo:


`make test` 

Este comando irá executar os testes.

### Lint

Para verificar o código-fonte quanto às boas práticas de estilo e organização, utilize o comando abaixo:


`make lint`