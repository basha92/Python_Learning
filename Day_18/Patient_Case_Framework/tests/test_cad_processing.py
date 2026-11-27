import pytest

#testing processing
@pytest.mark.cad
def test_tibia_processing(valid_tibia):
    assert valid_tibia.process() == "Tibial part processed"

@pytest.mark.cad
def test_femur_processing(valid_femur):
    assert valid_femur.process() == "Femoral part processed"

@pytest.mark.cad
def test_insert_processing(valid_insert):
    assert valid_insert.process() == "Insert part processed"

#testing validation - negative.
