import calculator

def test_mysum():
    assert calculator.mysum(1, 2) == 3

    assert calculator.mysum(100, 1000) == 1100
    assert calculator.mysum(10, 100) != 0

    # python -m pytest test_calculator.py
    # 테스트 명령어