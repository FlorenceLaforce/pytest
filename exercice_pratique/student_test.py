# tests/test_student.py
import math
import pytest
from student import Student


# ---------- CrÃ©ation / nom ----------
def test_name_is_stripped_and_stored():
    s = Student("  Sara  ")
    assert s.name == "Sara"

@pytest.mark.parametrize("bad", ["", "   ", None, 123])
def test_name_invalid_raises_value_error(bad):
    with pytest.raises(ValueError):
        Student(bad)


# ---------- Ajout de notes ----------
def test_add_note_valid_values_and_grades_copy():
    s = Student("Ali")
    s.add_note(75)
    s.add_note(60)
    # grades renvoie une COPIE (liste)
    g = s.grades
    assert g == [75, 60]
    g.append(0)               # on essaie de modifier la copie
    assert s.grades == [75, 60]  # l'interne n'a pas changÃ©

@pytest.mark.parametrize("note", [-1, 101])
def test_add_note_out_of_bounds_raises(note):
    s = Student("Ali")
    with pytest.raises(ValueError):
        s.add_note(note)

def test_add_note_wrong_type_raises():
    s = Student("Ali")
    with pytest.raises(TypeError):
        s.add_note(12.5)  # pas un int


# ---------- Moyenne / meilleure note ----------
def test_average_ok():
    s = Student("Lea")
    for n in (50, 70, 90):
        s.add_note(n)
    assert (s.average()== (50 + 70 + 90) / 3)

def test_average_no_grades_raises():
    s = Student("Lea")
    with pytest.raises(ValueError):
        s.average()

def test_best_ok():
    s = Student("Bob")
    for n in (10, 40, 99, 35):
        s.add_note(n)
    assert s.best() == 99

def test_best_no_grades_raises():
    s = Student("Bob")
    with pytest.raises(ValueError):
        s.best()


@pytest.mark.parametrize(
    "notes, attendu",
    [
        ((60, 60, 60), "admis"),   # moyenne >= 60 et min >= 40
        ((90, 30), "echec"),       # note < 40
        ((59, 80, 70), "admis"),   # moyenne < 60
        ((), "echec"),             # aucune note
    ],
    ids=["adm", "min_too_low", "avg_too_low", "no_grades"]
)
def test_status(notes, attendu):
    s = Student("Nora")
    for n in notes:
        s.add_note(n)
    assert s.status() == attendu