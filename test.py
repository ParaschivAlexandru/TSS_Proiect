import pytest
from function_for_test import Function


clasa_test=Function()

#Testare Functionala ( cauza-efect )
@pytest.mark.parametrize("text, word, n, y, expecteds", [
("test", "cattt", -1, 'y', ["Enter new info","valid number","valid text"]),                     #1
("cat cat", "cat", 3, 'n', ["valid number","Exiting"]),                                         #2
("cat cat", "cat", 'd', 'n', ["valid number","Exiting"]),                                       #3
("cat cat", "", 'd', 'y', ["valid number","Enter new info","valid word"]),                      #4
("cat cat", "cattttttttttt", 3, 'n', ["valid number","valid text","Exiting"]),                  #5
("cat cat", "", 'd', 'ns', ["valid number","valid word","valid continue word"]),                #6
("cat Cat dog Dog", "cat", 3, 'n', ["NOT present in the text with 3","Exiting"]),               #7
("cat Cat dog Dog", "hat", 3, 'y', ["NOT present in the text","Enter new info"]),               #8
("cat Cat dog Dog", "cat", 2, 'n', ["present in the text with 2","Exiting"]),                   #9
("cat Cat dog Dog", "", -3, 'ns', ["valid number","valid word","valid continue word"]),         #10
("cat", "catt", 'd', 'ns', ["valid number","valid text","valid continue word"])                 #11
])
def test_function_cause_and_effect(text, word, n, expecteds, y, capsys):
    clasa_test.word_has_n_occurrences_in_text(text, word, n, y)
    cap = capsys.readouterr()
    out = cap.out
    assert all(sentence in out for sentence in expecteds)

#Testare Structurala
#a)Statement coverage
@pytest.mark.parametrize("text, word, n, y, expecteds", [
("test", "", -1, 'ds', ["valid continue word","valid number","valid word"]),
("cat cat", "catttttttt", 1, 'n', ["valid text","Exiting"]),
("cat Cat dog Dog", "cat", 3, 'n', ["NOT present in the text with 3","Exiting"]),
("cat Cat dog Dog", "hat", 3, 'y', ["NOT present in the text","Enter new info"]),
("cat Cat dog Dog", "cat", 2, 'n', ["present in the text with 2","Exiting"])
])
def test_statement_coverage(text, word, n, expecteds, y, capsys):
    clasa_test.word_has_n_occurrences_in_text(text, word, n, y)
    cap = capsys.readouterr()
    out = cap.out
    assert all(sentence in out for sentence in expecteds)

#b)Branch coverage
@pytest.mark.parametrize("text, word, n, y, expecteds", [
("test", "", -1, 'ds', ["valid continue word","valid number","valid word"]),
("cat cat", "catttttttt", 1, 'n', ["valid text","Exiting"]),
("cat Cat dog Dog", "cat", 3, 'n', ["NOT present in the text with 3","Exiting"]),
("cat Cat dog Dog", "hat", 3, 'y', ["NOT present in the text","Enter new info"]),
("cat Cat dog Dog", "cat", 2, 'n', ["present in the text with 2","Exiting"]),
("cat cat dog","cat",2,'y',["present in the text","Enter new info"])
])
def test_branch_coverage(text, word, n, expecteds, y, capsys):
    clasa_test.word_has_n_occurrences_in_text(text, word, n, y)
    cap = capsys.readouterr()
    out = cap.out
    assert all(sentence in out for sentence in expecteds)

#c)Condition coverage
@pytest.mark.parametrize("text, word, n, y, expecteds", [
("test", "", -1, 'ds', ["valid continue word","valid number","valid word"]),
("cat cat", "catttttttt", 1, 'n', ["valid text","Exiting"]),
("cat Cat dog Dog", "cat", 3, 'n', ["NOT present in the text with 3","Exiting"]),
("cat Cat dog Dog", "hat", 3, 'y', ["NOT present in the text","Enter new info"]),
("test", "", 'd', 'ds', ["valid continue word","valid number","valid word"]),
("test", "", 2, 'ds', ["valid continue word","valid number","valid word"]),
("cat Cat dog Dog", "cat", 2, 'n', ["present in the text with 2","Exiting"])
])
def test_condition_coverage(text, word, n, expecteds, y, capsys):
    clasa_test.word_has_n_occurrences_in_text(text, word, n, y)
    cap = capsys.readouterr()
    out = cap.out
    assert all(sentence in out for sentence in expecteds)

#c)Circuit coverage
@pytest.mark.parametrize("text, word, n, y, expecteds", [
("test", "", -1, 'ds', ["valid continue word","valid number","valid word"]),
("cat cat", "catttttttt", 1, 'n', ["valid text","Exiting"]),
("cat Cat dog Dog", "cat", 3, 'n', ["NOT present in the text with 3","Exiting"]),
("cat Cat dog Dog", "hat", 3, 'y', ["NOT present in the text","Enter new info"]),
("test", "", 'd', 'ds', ["valid continue word","valid number","valid word"]),
("test", "", 2, 'ds', ["valid continue word","valid number","valid word"]),
("cat Cat dog Dog", "cat", 2, 'n', ["present in the text with 2","Exiting"])
])
def test_circuit_coverage(text, word, n, expecteds, y, capsys):
    clasa_test.word_has_n_occurrences_in_text(text, word, n, y)
    cap = capsys.readouterr()
    out = cap.out
    assert all(sentence in out for sentence in expecteds)
