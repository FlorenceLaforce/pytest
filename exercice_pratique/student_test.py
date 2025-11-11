import pytest
from student import Student

def test_name_is_striped():
    s = Student(" Sara ")
    assert s.name == "Sara"

@pytest.mark.parametrize("bad",["", " ", None, 123])
def test_invalid_name(bad):
    with pytest.raises(ValueError):
        Student(bad)

def test_note_valide():
    s = Student("Sara")
    s.add_note(75)
    s.add_note(60)
    g = s.grades
    assert g == [75,60]