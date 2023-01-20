# Portuguese Clinical NER - Disorder

Este projeto tem como objetivo desenvolver uma aplicação de reconhecimento de entidades nomeadas em textos clínicos em português. Para isso, foi utilizado o modelo [BioBERTpt](https://github.com/HAILab-PUCPR/BioBERTpt), treinado com o corpus [SemClinBr](https://github.com/HAILab-PUCPR/SemClinBr).

## Como usar

### Pré-requisitos

-   Docker
-   Docker Compose

### Executando a aplicação

1.  Clone este repositório: `git clone https://github.com/[SEU_USUARIO]/ner-disorder.git`
2.  Construa e inicie a aplicação com o comando `docker-compose up --build`
3.  Acesse a aplicação em seu navegador em `http://localhost:8501`

### Executando testes

Para executar os testes unitários, execute o seguinte comando dentro do container:

`pytest` 

## Estrutura de pastas

.
├── app.py
├── config.json
├── Dockerfile
├── docker-compose.yml
├── helpers.py
├── model
│   ├── biobertpt-all
│   │   ├── config.json
│   │   ├── pytorch_model.bin
│   │   ├── special_tokens_map.json
│   │   ├── tokenizer_config.json
│   │   └── vocab.txt
├── README.md
├── requirements.txt
├── service.py
└── tests
    ├── test_helpers.py
    └── test_service.py` 
