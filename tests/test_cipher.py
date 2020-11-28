from hypothesis import given, example, assume, event
from math import isnan
import string
import hypothesis.strategies as st
from cipher import encrypt, decrypt

#@given(st.text())
@given(st.text(string.ascii_letters))
@example("hello world")
def test_decrypt_deciphers_encrypt_fixed_key(s):
    assert decrypt(encrypt(s, 20), 20) == s

@given(st.integers())
def test_key_works(i):
    assert decrypt(encrypt('test', i), i) == 'test'

#@given(s=st.text(), i=st.integers())
@given(s=st.text(string.ascii_letters), i=st.integers())
def test_decrypt_deciphers_encrypt_variable_key(s, i):
    assert decrypt(encrypt(s, i), i) == s

#####################################
## Exemplos extras da documentação ##
#####################################

@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
        pass

@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
        event("i mod 3 = %d" % (i % 3,))

@given(floats())
def test_negation_is_self_inverse_for_non_nan(x):
        assume(False)
        assert x == -(-x)
