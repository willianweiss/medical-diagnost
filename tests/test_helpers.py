from utils.helpers import Helpers
import os

helpers = Helpers()


def test_save_patient_data():
    patient_data = {"name": "John Doe", "age": 30}
    patient_id = "123"
    helpers.save_patient_data(patient_data, patient_id)
    assert os.path.exists(f"patients_data/{patient_id}.json") == True


def test_load_patient_data():
    patient_data = {"name": "John Doe", "age": 30}
    patient_id = "123"
    helpers.save_patient_data(patient_data, patient_id)
    loaded_patient_data = helpers.load_patient_data(patient_id)
    assert loaded_patient_data == patient_data


def test_update_patient_data():
    patient_data = {"name": "John Doe", "age": 30}
    patient_id = "123"
    helpers.save_patient_data(patient_data, patient_id)
    patient_data["age"] = 31
    helpers.update_patient_data(patient_data, patient_id)
    loaded_patient_data = helpers.load_patient_data(patient_id)
    assert loaded_patient_data == patient_data


def test_detect_cancer():
    patient_data = {}
    disorder_list = ["I-Disorder"]
    cancer_detected, updated_patient_data = helpers.detect_cancer(
        patient_data, disorder_list
    )
    assert cancer_detected == True
    assert "cancer_detected" in updated_patient_data
    assert "cancer_detection_date" in updated_patient_data
    disorder_list = ["O"]
    cancer_detected, updated_patient_data = helpers.detect_cancer(
        patient_data, disorder_list
    )
    assert cancer_detected == False
    assert "cancer_detected" in updated_patient_data
