import pytest
import student 

def test_default():
    assert "THIS is A sentence THAT must WORK" in student.caseSwitcher("This is a sentence that must work")

def test_second_sentence():
    assert "THIS must ALSO work" in student.caseSwitcher("This must also work")

