from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    assert encrypt_message("abc", 1) == "a_cb"
    assert encrypt_message("abc", 2) == "c_ba"
    assert encrypt_message("abc", 3) == "cba"

    with raises(TypeError) as error:
        encrypt_message("abc", "")
    assert str(error) == "tipo inválido para key"

    with raises(TypeError) as error:
        encrypt_message(1, 1)
    assert str(error) == "tipo inválido para message"
