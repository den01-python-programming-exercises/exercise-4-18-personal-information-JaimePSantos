import pytest
from src.personal_information import PersonalInformation

def test_exercise():
    scott = PersonalInformation("Scott","Morgan",12345)

    assert scott.get_first_name() == "Scott"
    assert scott.get_last_name() == "Morgan"
    assert scott.get_identification_number() == 12345
