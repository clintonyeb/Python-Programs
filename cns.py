# coding: utf-8
ord('t')
get_ipython().run_line_magic('pinfo', 'ord')
chr(116)
ord(t)
ord('t')
ord(
'a')
def posOrd(ch)
def posOrd(ch):
    return (ord(ch) - ord('a') + 1)
posOrd('a')
posOrd('b')
posOrd('t')
def aord(ch):
    return (ord(ch) - ord('a') + 1)
def achr(d):
    return (chr(d) - chr(97) + 1)
achr(1)
chr(97)
def achr(d):
    ch = d + 97
    return (chr(d))
def achr(d):
    ch = d + 97
    return (chr(ch))
achr(1)
def achr(d):
    ch = d + 97 - 1
    return (chr(ch))
def achr(d):
    ch = d + 97 - 1
    return (chr(ch))
achr(1)
achr('t')
aord('t')
aord('z')
achr(14)
achr(40)
def enc(mess, key):
    res = ''
    for ch in mess:
        e = (ch + key) % 26
        res += e
        
def enc(mess, key):
    res = ''
    for ch in mess:
        e = (ch + key) % 26
        res += e
    return res    
def aord(ch):
    return (ord(ch) - ord('a'))
def enc(mess, key):
    res = ''
    for ch in mess:
        d = aord(ch)
        e = (d + key) % 26
        res += achr(e)
    return res
def achr(d):
    ch = d + 97
    return (chr(ch))
enc('hello
enc('hello', 15)
def dec(mess, key):
    res = ''
    for ch in mess:
        o = aord(ch)
        d = (o - 26) % 26
        res += achr(d)
    return res
enc('wtaad', 15)
def dec(mess, key):
    res = ''
    for ch in mess:
        o = aord(ch)
        d = (o - key) % 26
        res += achr(d)
    return res
enc('wtaad', 15)
dec('wtaad', 15)
mess = 'UVACLYFZLJBYL'.lower()
mess
for i in range(15):
    d = dec(mess, i)
    print(d)
    
mess = '"GCUA VQ DTGCM“'.lower()
mess
for i in range(15):
    d = dec(mess, i)
    print(d)
    
mess = 'GCUA VQ DTGCM'.lower()
def bfa(mess, lim)"
def bfa(mess, lim):
    for i in range(15):
        d = dec(mess, i)
        print(d)
        
bfa(mess, 10)
def dec(mess, key):
    res = ''
    for ch in mess:
        if ch == ' ':
            res += ch
            continue
        o = aord(ch)
        d = (o - key) % 26
        res += achr(d)
    return res
bfa(mess, 10)
def freq('mess'):
a = {}
a
a['c'] = 3
a['c']
a['d']
'c' in a
'd' in a
def freq(mess):
    res = {}
    for ch in mess:
        if ch in res:
            res[ch] += 1
        else:
            res[ch] = 1
    return res
l = 'ifwewishtoreplaceletters'
freq(l)
aord('i')
enc('e', 4)
