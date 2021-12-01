from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

# IMPORT STANDARD PACKAGE
import os
import random

from typing import Iterable, Iterator

# IMPORT CIPHER PACKAGE
import nested_cipher.b64 as nsb64


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #


# KEY MAKER
def key_maker(length: int = None, chars: str = None, skip: Iterable[str] = None, pattern: dict = None) -> str:
    """[Key Maker Function]

    Args:
        length (int, optional): [Make Key Length]. Defaults to '32'.
        chars (str, optional): [Characters For Key Make]. Defaults to 'Ascii 32:126'.
        skip (Iterable[str], optional): [Skip Characters]. Defaults to None.
        pattern (dict, optional): [Set 'Start' and 'End' Pattern. Dict with 3 keys ('start', 'end', 'splitter').
            Supports 4 Special Charackter {'\\d': 'Digit', '\\A': 'Upper Alpha', '\\a': 'Lower Alpha', '\\s': 'Symbol'}]

    Returns:
        str: [Created Key]
    """
    def _make(length: int = None, chars: str = None, skip: Iterable[str] = None) -> str:
        chars = "".join([chr(i) for i in range(32, 127)]) if chars is None else chars
        length = 32 if length is None else length

        if skip:
            skip = set(skip)
            chars = set(chars).difference(skip)
            chars = ''.join(chars)

        _idx = (random.choice(chars) for _ in range(0, length))

        return ''.join(iter(_idx))

    _key = _make(length, chars, skip)
    if pattern is None:
        return _key

    _mp = {
        '\\d': '0123456789',
        '\\A': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '\\a': 'abcdefghijklmnopqrstuvwxyz',
        '\\s': "()+'\\-_\"?/<>~!@#$%^&*.,[]{}|`:;=",
    }
    _mk_pat = lambda x: random.choice(x)

    start, end = pattern['start'], pattern['end']
    if start is not None:
        _split_start = start.split(pattern['splitter'])
        _st = ''
        for it in _split_start:
            if it in _mp.keys():
                _st += _mk_pat(_mp[it])
            else:
                _st += it
        _key = f"{_st}{_key[len(_st):]}"
        del _split_start, _st

    if end is not None:
        _split_end = end.split(pattern['splitter'])
        _ed = ''
        for it in _split_end:
            if it in _mp.keys():
                _ed += _mk_pat(_mp[it])
            else:
                _ed += it
        _key = f"{_key[: -len(_ed)]}{_ed}"
        del _split_end, _ed
    return _key


# STRING CRYPTO
def crypto(text: str, key: str) -> Iterable:
    """[Crypto XOR String]

    Args:
        text (str): [Text for Encrypt Or Decrypt]
        key (str): [Key Crypto]

    Returns:
        Iterable: [Encrypt string or Decrypt string]
    """

    xor = lambda a, b: ord(a) ^ b

    # Create Iterable Key Length Same to Input Text
    def str_key(key: str, end: int) -> Iterator:
        """[Inner Function Key Iter]

        Args:
            key (str): [Key Crypt]
            end (int): [Need How Many]

        Yields:
            Iterator: [unicode id key]
        """
        _len_key = len(key)
        _idx = 0

        for _ in range(0, end):

            if _idx == _len_key:
                _idx = 1
                key = ''.join(reversed(key))
                yield ord(key[0])
            
            else:
                yield ord(key[_idx])
                _idx += 1

    key = str_key(key, len(text))

    for char in text:
        # Generate New Char
        yield chr(xor(char, next(key)))


# CIPHER Text
def text_cipher(method: str, mode: str, text: str, key: str = None, cipher_key_method: str = None) -> str:
    """[Text Cipher]

    Args:
        method (str): [nested cipher method name for cipher input value]
        mode (str): [mode 'encode' or 'decode']
        text (str): [input value for cipher]
        key (str, optional): [key for 'encrypt' or 'decrypt' input value]. Defaults to None mean no crypting.
        cipher_key_method (str, optional): [cipher key before crypting input value]. Defaults to None mean no cipher key.

    Raises:
        NameError: [Mode Name Error if not 'encode' or 'decode']
        NameError: [Cipher Method Name Error if not nested_cipher method name]
        NameError: [Cipher Key Method Name Error if not nested_cipher method name]

    Returns:
        str: [encoded text or decoded text]
    """
    all_ci_method = ('b64','ab64','mb64','eb64','lb64','rb64','rab64','rmb64','reb64','rlb64')
    if mode not in ('encode', 'decode'):
        raise NameError("Mode Must 'encode' or 'decode'")

    if method not in all_ci_method:
        raise NameError("Method Name Not Exists")

    if cipher_key_method is not None and cipher_key_method not in all_ci_method:
        raise NameError("Method Name Not Exists")

    _nested_active = f'nsb64.{method}_{mode}'
    _ex = eval(_nested_active)

    if key not in ('', ' ', None):
        if cipher_key_method is not None:
            key = text_cipher(cipher_key_method, 'encode', key)

        if mode == 'encode':
            text = ''.join(crypto(text, key))
            return _ex(text.encode('utf-8')).decode('ascii')

        elif mode == 'decode':
            text = _ex(text.encode('ascii')).decode('utf-8')
            return ''.join(crypto(text, key))
    else:
        if mode == 'encode':
            return _ex(text.encode('utf-8')).decode('ascii')
        elif mode == 'decode':
            return _ex(text.encode('ascii')).decode('utf-8')


# CIPHER FILE
def file_cipher(method: str, mode: str, file_path_and_type: tuple[str, str], result_file: str, key: str = None, cipher_key_method: str = None) -> str:
    """[File Cipher]

    Args:method (str): [nested cipher method name for cipher input value]
        mode (str): [mode 'encode' or 'decode']
        file_path_and_type (tuple[str, str]): [Path File For Cipher and Type Source File]
            Example [Binarray] File : Encode ('./dir/file.mp4', 'b') - Decode ('./dir/file.ci', 'b')
            Example [Text] File : Encode ('./dir/file.txt', 't') - Decode ('./dir/file.ci', 't')
        result_file (str): [Path Result File]
        key (str, optional): [key for 'encrypt' or 'decrypt' input value]. Defaults to None mean no crypting.
        cipher_key_method (str, optional): [cipher key before crypting input value]. Defaults to None mean no cipher key.

    Raises:
        NameError: [Mode Name Error if not 'encode' or 'decode']
        NameError: [Cipher Method Name Error if not nested_cipher method name]
        NameError: [Cipher Key Method Name Error if not nested_cipher method name]
        NameError: [Type File Name Error for text file 't', for binarray file 'b']
        FileNotFoundError: [If File Not Found Error Not Found File]
        TypeError: [If result file Path Not a File Error]
        err: [Any Error For Read or Write 'Text' File]
        err: [Any Error For Read or Write 'Binarray' File Mode 'Encode']
        err: [Any Error For Read or Write 'Binarray' File Mode 'Decode']

    Returns:
        str: [Result File Path]
    """
    all_ci_method = ('b64','ab64','mb64','eb64','lb64','rb64','rab64','rmb64','reb64','rlb64')
    if mode not in ('encode', 'decode'):
        raise NameError("Mode Must 'encode' or 'decode'")

    if method not in all_ci_method:
        raise NameError("Method Name Not Exists")

    if cipher_key_method is not None and cipher_key_method not in all_ci_method:
        raise NameError("Method Name Not Exists")

    if file_path_and_type[1] not in ('t', 'b'):
        raise NameError("File Type Must Be Binarray 'b' or Text 't'")

    _path = os.path.realpath(file_path_and_type[0])
    if not os.path.isfile(_path):
        raise FileNotFoundError("File Not Found")

    result_file = os.path.realpath(result_file)
    if os.path.isdir(result_file):
        raise TypeError('The Path Must Be File Path Not a Directory Path')

    is_text = True if file_path_and_type[1] == 't' else False
    if mode == 'encode':
        _mr = 'r' if file_path_and_type[1] == 't' else 'rb'
        _mw = 'w'
    elif mode == 'decode':
        _mr = 'r'
        _mw = 'w' if file_path_and_type[1] == 't' else 'wb'

    if is_text:
        try:
            with open(_path, _mr) as f, open(result_file, _mw) as of:
                _ex = text_cipher(method, mode, f.read(), key, cipher_key_method)
                of.write(_ex)
            f.close()
            of.close()
            del _ex

            return result_file

        except BaseException as err:
            raise err
    else:
        _dir = os.path.dirname(result_file)
        _tmp = os.path.join(_dir, '_tmp.tmp')

        if mode == 'encode':
            try:
                # Make Binarray File to String File
                with open(_path, 'rb') as f, open(_tmp, 'w') as tf:
                    _bin_to_string = nsb64.b64_encode(f.read())
                    tf.write(_bin_to_string.decode('ascii'))
                f.close()
                tf.close()
                del _bin_to_string

                # Make Execute Order
                with open(_tmp, 'r') as f, open(result_file, 'w') as of:
                    _ex = text_cipher(method, 'encode', f.read(), key, cipher_key_method)
                    of.write(_ex)
                f.close()
                of.close()

                return result_file

            except BaseException as err:
                raise err
            finally:
                if os.path.exists(_tmp):
                    os.remove(_tmp)

        elif mode == 'decode':
            try:
                # Cipher Foam To Raw Base64
                with open(_path, 'r') as f, open(_tmp, 'w') as tf:
                    _cipher_to_b64 = text_cipher(method, 'decode', f.read(), key, cipher_key_method)
                    tf.write(_cipher_to_b64)
                f.close()
                tf.close()
                del _cipher_to_b64

                # Raw Base64 To Source File
                with open(_tmp, 'r') as f, open(result_file, 'wb') as of:
                    _b64_to_source = nsb64.b64_decode(f.read())
                    of.write(_b64_to_source)
                f.close()
                of.close()
                del _b64_to_source

                return result_file

            except BaseException as err:
                raise err
            finally:
                if os.path.exists(_tmp):
                    os.remove(_tmp)


__dir__ = ('key_maker', 'crypto', 'text_cipher', 'file_cipher')
