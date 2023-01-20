import json
import os
from datetime import datetime

import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer


class ClinicalNERService:
    def __init__(self):
        # Carregando configurações
        with open("config.json", "r") as f:
            config = json.load(f)
        self.model_name = config["model_name"]
        self.num_labels = config["num_labels"]
        self.dropout_prob = config["dropout_prob"]
        self.id2label = config["id2label"]
        self.tokenizer_config = config["tokenizer_config"]

        # Inicializando o modelo e o tokenizador
        self.model = AutoModelForTokenClassification.from_pretrained(
            self.model_name
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name, **self.tokenizer_config
        )
        self.model.eval()

        # Carregando dados de pacientes
        self.pacients_data = {}

    def predict(self, input_data):
        try:
            # Preparando entrada
            input_ids = self.tokenizer.encode(
                input_data["texto_prontuario"], return_tensors="pt"
            )
            attention_mask = input_ids.ne(self.tokenizer.pad_token_id)
            # Executando previsão com o modelo
            with torch.no_grad():
                logits = self.model(input_ids, attention_mask=attention_mask)[
                    0
                ]
            labels = logits.argmax(2).tolist()[0]
            disorder_list = [self.id2label[str(i)] for i in labels if i != 0]
            return disorder_list
        except Exception as e:
            print("Erro ao executar previsão:", e)
            return None
