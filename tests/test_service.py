from service import ClinicalNERService


def test_predict_input_text():
    # Testando se o modelo está tratando corretamente a entrada de texto
    service = ClinicalNERService()
    input_data = {
        "texto_prontuario": "O paciente apresentou dores de cabeça e náuseas."
    }
    output = service.predict(input_data)
    assert (
        "O" not in output
    ), f"A classe 'O' não deveria estar presente na saída {output}."


def test_predict_input_data():
    # Testando se o modelo está lidando corretamente com a falta de dados de entrada
    service = ClinicalNERService()
    input_data = {"texto_prontuario": None}
    output = service.predict(input_data)
    assert output is None, f"Esperado None, mas obtido {output}."
