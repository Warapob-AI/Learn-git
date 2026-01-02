import pytest
from fastapi.testclient import TestClient
from server import app  

client = TestClient(app)
# ---------------------------------------------------------
# กลุ่มที่ 1: ทดสอบกรณี Success (Status 200)
# ---------------------------------------------------------
@pytest.mark.parametrize("num1, num2, expected_result", [
    (10.5, 20, 30.5),   # Float + Int
    (1, 2, 3.0),        # Int + Int
    (5.5, 4.5, 10.0),   # Float + Float
])
def test_add_plus_success(num1, num2, expected_result):
    payload = {
        "num1": num1,
        "num2": num2
    }
    response = client.post("/add-plus", json=payload)

    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


# ---------------------------------------------------------
# กลุ่มที่ 2: ทดสอบกรณีข้อมูลผิดประเภท (Status 422)
# ---------------------------------------------------------
@pytest.mark.parametrize("num1, num2", [
    ("ไม่ใช่ตัวเลข", 20),  # num1 ผิด
    (10, "ข้อความ"),      # num2 ผิด
    ("กขค", "ABC"),       # ผิดทั้งคู่
])
def test_add_plus_invalid_type(num1, num2):
    payload = {
        "num1": num1,
        "num2": num2
    }
    response = client.post("/add-plus", json=payload)
    
    assert response.status_code == 422
    
# ---------------------------------------------------------
# กลุ่มที่ 1: ทดสอบกรณี Success (Status 200)
# ---------------------------------------------------------
@pytest.mark.parametrize("num1, num2, expected_result", [
    (5, 2, 3),
    (5.0, 2.0, 3.0),
    (5.0, 2, 3.0),
    (5, 2.0, 3.0)
])
def test_add_negative_success(num1, num2, expected_result):
    payload = {
        "num1": num1,
        "num2": num2
    }
    response = client.post("/add-negative", json=payload)

    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


# ---------------------------------------------------------
# กลุ่มที่ 2: ทดสอบกรณีข้อมูลผิดประเภท (Status 422)
# ---------------------------------------------------------
@pytest.mark.parametrize("num1, num2", [
    ("ไม่ใช่ตัวเลข", 20),  # num1 ผิด
    (10, "ข้อความ"),      # num2 ผิด
    ("กขค", "ABC"),       # ผิดทั้งคู่
])
def test_add_negative_invalid_type(num1, num2):
    payload = {
        "num1": num1,
        "num2": num2
    }
    response = client.post("/add-negative", json=payload)
    
    assert response.status_code == 422