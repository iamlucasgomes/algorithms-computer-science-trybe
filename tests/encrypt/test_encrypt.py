from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    assert encrypt_message("trybe", 2) == "eby_rt"
    assert encrypt_message("trybe", 3) == "yrt_eb"
    assert encrypt_message("trybe", 5) == "ebyrt"

    with raises(TypeError):
        encrypt_message("abc", "1")

    with raises(TypeError):
        encrypt_message(4, 1)
