import streamlit as st
from service import ClinicalNERService
from utils.helpers import Helpers

helpers = Helpers()
clinical_ner_service = ClinicalNERService()

st.set_page_config(
    page_title="Clinical NER App", page_icon=":hospital:", layout="wide"
)
st.title("Clinical Named Entities Recognition")


patient_id = st.text_input("Insira o ID do paciente:")
texto_prontuario = st.text_area("Insira o texto do prontuário:")


if st.button("Reconhecer entidades"):
    disorder_list = clinical_ner_service.predict(
        {"texto_prontuario": texto_prontuario}
    )
    cancer_detected, patient_data = helpers.detect_cancer({}, disorder_list)
    if cancer_detected:
        st.success("Câncer detectado!")
    else:
        st.warning("Câncer não detectado.")
    helpers.save_patient_data(patient_data, patient_id)

if st.button("Ver dados do paciente"):
    patient_data = helpers.load_patient_data(patient_id)
    st.write("Dados do paciente:", patient_data)
