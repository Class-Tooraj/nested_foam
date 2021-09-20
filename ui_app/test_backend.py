###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT STANDARD PACKAGE
import time

from os.path import getsize as the_size

# IMPORT LOCAL --> IMPORT ALL BACKEND MODULE FOR TEST
from backend import *

# TESTS
TIME_NS = lambda : time.perf_counter_ns()

# STATIC TEST KEY MAKER
def test_key_maker() -> int:
    custom_char = 'abcdefghijklmnopqrstuvwxyz'
    skip_char = "*/.\\?'\";:.,~!@#$%^&*()_-[]{=}+><"
    print("KEY DEFAULT MAKE")
    t_0 = TIME_NS()
    _key_1_default = key_maker()
    t_1 = TIME_NS()
    print(f"LENGTH:{len(_key_1_default)}\tTIME [{t_1 - t_0} ns]\tKEY:{_key_1_default}", end = "\n\n")
    print(f"KEY CUSTOM CHAR MAKE & CUSTOM LENGTH\tCHARS:[{custom_char}]")
    t_0 = TIME_NS()
    _key_2_custom_char = key_maker(64, chars= custom_char)
    t_1 = TIME_NS()
    print(f"LENGTH:{len(_key_2_custom_char)}\tTIME [{t_1 - t_0} ns]\tKEY:{_key_2_custom_char}", end = "\n\n")
    print(f"KEY SKIP CHAR MAKE & CUSTOM LENGTH\tSKIP CHARS:[{skip_char}]")
    t_0 = TIME_NS()
    _key_3_skiped_char = key_maker(64, skip= skip_char)
    t_1 = TIME_NS()
    print(f"LENGTH:{len(_key_3_skiped_char)}\tTIME [{t_1 - t_0} ns]\tKEY{_key_3_skiped_char}", end = "\n\n")

    del custom_char, skip_char, t_0, t_1, _key_1_default, _key_2_custom_char, _key_3_skiped_char
    return 0

# STATIC TEST CRYPTO
def test_crypto() -> int:
    test_text = ['TEST CRYPTO STRING', '__ 73$7 Cryp70 $Tr!n9 __', '1234567890', '0123456789', '   ', '_ _']
    key = 'THE~KEY'
    for idx, txt in enumerate(test_text):
        print(f"ENCRYPT TEXT INDEX [{idx}]")
        t_0 = TIME_NS()
        ex = crypto(txt, key)
        enc = ''.join(ex)
        t_1 = TIME_NS()
        print(f'ENCRYPTED index[{idx}]: TIME:[{t_1 - t_0} ns]\t[{enc}]', end = "\n\n")
        print(f"DECRYPT TEXT INDEX [{idx}]")
        t_0 = TIME_NS()
        ex = crypto(enc, key)
        dec = ''.join(ex)
        t_1 = TIME_NS()
        print(f'DECRYPTED INDEX [{idx}]: TIME:[{t_1 - t_0} ns]\t[{dec}]')
        print(f'SOURCE [{txt}] | DECRYPTED [{dec}] \t [{True if txt == dec else False}]', end = "\n\n")
    print('... END TEST CRYPTO ...')

    del test_text, key, t_0, t_1, idx, txt, enc, dec
    return 0

# STATIC TEST TEXT CIPHER
def test_text_cipher() -> int:
    test_text = ['TestString _ 0/ TEST Str!ng', 'TestString _ 1/ TEST $trin9', '1234567890', '0123456789']
    for idx, txt in enumerate(test_text):
        print(f"ENCODE TEXT INDEX [{idx}]")
        t_0 = TIME_NS()
        enc = text_cipher('mb64', 'encode', txt, 'ABCD', 'rmb64')
        t_1 = TIME_NS()
        print(f'ENCODED index[{idx}]: TIME:[{t_1 - t_0} ns]\t[{enc}]', end = "\n\n")
        print(f"DECODE TEXT INDEX [{idx}]")
        t_0 = TIME_NS()
        dec = text_cipher('mb64', 'encode', enc, 'ABCD', 'rmb64')
        t_1 = TIME_NS()
        print(f'DECODED INDEX [{idx}]: TIME:[{t_1 - t_0} ns]\t[{dec}]')
        print(f'SOURCE [{txt}] | DECRYPTED [{dec}] \t [{True if txt == dec else False}]', end = "\n\n")
    print('... END TEST TEXT CIPHER ...')

    del test_text, idx, txt, t_0, t_1, enc, dec
    return 0


# STATIC TEST FILE CIPHER
def test_file_cipher() -> int:
    def enc():
        test_file = [('./test/text.txt', 't'), ('./test/img.jpg', 'b'), ('./test/vid.mp4', 'b')]
        result_file = ['./test/enc/ci_text.txt', './test/enc/ci_img.txt', './test/enc/ci_vid.txt']
        for tf, rf in zip(test_file, result_file):
            print(f"ENCODE File: [{tf[0]}]\tType: [{tf[1]}]\tSize: [{the_size(tf[0])}]")
            t_0 = TIME_NS()
            ex = file_cipher('mb64', 'encode', tf, rf, 'ABCD', 'rmb64')
            t_1 = TIME_NS()
            print(f"...ENCODED...\tTime: [{t_1 - t_0} ns]\tPATH:[{ex}]", end = "\n\n")
            yield ex

    def dec():
        test_file = [('./test/enc/ci_text.txt', 't'), ('./test/enc/ci_img.txt', 'b'), ('./test/enc/ci_vid.txt', 'b')]
        result_file = ['./test/dec/de_text.txt', './test/dec/de_img.jpg', './test/dec/de_vid.mp4']
        for tf, rf in zip(test_file, result_file):
            print(f"DECODE File: [{tf[0]}]\tType: [{tf[1]}]\tSize: [{the_size(tf[0])}]")
            t_0 = TIME_NS()
            ex = file_cipher('mb64', 'decode', tf, rf, 'ABCD', 'rmb64')
            t_1 = TIME_NS()
            print(f"...DECODED...\tTime: [{t_1 - t_0} ns]\tPATH:[{ex}]", end = "\n\n")
            yield ex

    t_enc = enc()
    t_dec = dec()

    en_txt = next(t_enc)
    en_img = next(t_enc)
    en_vid = next(t_enc)
    de_txt = next(t_dec)
    de_img = next(t_dec)
    de_vid = next(t_dec)

    del t_enc, t_dec, en_txt, en_img, en_vid, de_txt, de_img, de_vid
    return 0

def test_main() -> int:
    def st_key() -> None:
        print("STATIC TEST KEY MAKER [START]")
        test_key_maker()
        print("STATIC TEST KEY MAKER [END]")

    def st_crypto() -> None:
        print("STATIC TEST CRYPTO [START]")
        test_crypto()
        print("STATIC TEST CRYPTO [END]")

    def st_text() -> None:
        print("STATIC TEST TEXT CIPHER [START]")
        test_text_cipher()
        print("STATIC TEST TEXT CIPHER [END]")

    def st_file() -> None:
        print("STATIC TEST FILE CIPHER [START]")
        test_file_cipher()
        print("STATIC TEST FILE CIPHER [END]")

    print("<SELECT STATIC TEST>\n\t1: TEST KEY MAKE\n\t2: TEST CRYPTO\n\t3: TEST TEXT CIPHER\n\t4: TEST FILE CIPHER\n\t0: EXIT")

    _inp = str(input("TEST >/ "))

    if _inp == '0':
        return 0

    elif _inp == '1':
        print(f"<MODE '{_inp}'>")
        st_key()
        print("<TEST IS DONE>")

    elif _inp == '2':
        print(f"<MODE '{_inp}'>")
        st_crypto()
        print("<TEST IS DONE>")

    elif _inp == '3':
        print(f"<MODE '{_inp}'>")
        st_text()
        print("<TEST IS DONE>")

    elif _inp == '4':
        print(f"<MODE '{_inp}'>")
        st_file()
        print("<TEST IS DONE>")

if __name__=='__main__':
    raise SystemExit(test_main())
