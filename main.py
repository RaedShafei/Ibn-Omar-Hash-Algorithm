# coding=utf-8


import math
import decimal
from decimal import *
import cmath
import time


# Ciphering functions



def rShift(s1, d):
    rs = s1[0:len(s1) - d]
    rss = s1[len(s1) - d:]
    return rss + rs


def lShift(s1, d):
    ls = s1[0:d]
    lss = s1[d:]
    return lss + ls


def reverse(seq, start, stop):
    seq = list(seq)
    size = stop + start
    for i in range(start, (size + 1) // 2):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]

    return ''.join(seq)




print("Designed and Developed By: Raed Omar Shafei")

# input
i = raw_input("enter: ")
ti = time.time()
isize = len(i)



# ASCII to Binary
i = map(bin, bytearray(i))
i = ''.join(i)
i = i.replace('0b', '')

# Salts
A = '1100010001111001001110110001010001100101001011000101100110010011101100010111111001010010'
B = '11001000111110010011101100100100011001010001110010011101100011001011001010010'
C = '11000101101110010011111100011011111001010001110010100001100100101011001010010'
D = '1100100001111001001110110010001001100100111011001000101110010011111100100011011001010010'
E = '1100011001111001001110110001110011100101001011001000001110010011101100011010111001010010'
F = '1100100001011001001110110001100011100100111011000110100110010011101100010101011001010010'
G = '110001010111100100111011000101110110010011101100011000011001010010'
H = '110001101101100100111011000111000110010100001100011101011001010010'

# Padding1
b = i + A + i + B + i + C + i + D + i + E + i + F + i + G + i + H + i
block = b + b + '1'



# Padding2
bSize = len(block)
paddingValue = (2048 % bSize)
pv = (bSize % 2048)


if bSize < 2048:
    padL = ''
    padL = padL.ljust(paddingValue, '0')
    blocks = block + padL
elif bSize > 2048:
    pv = ((bSize // 2048) + 1) * 2048 - bSize
    padG = ''
    padG = padG.ljust(pv, '0')
    blocks = block + padG
else:
    blocks = block

# Ciphering
blocksR = rShift(blocks, 604)
andR = int(blocks) & int(blocksR)
xoR = int(blocks) ^ int(blocksR)
bR = andR | xoR
bR = rShift(str(bR), 604)
bR = int(bR)
bR = '{0:b}'.format(bR)

blocksL = lShift(blocks, 309)
andL = int(blocks) & int(blocksL)
xoL = int(blocks) ^ int(blocksL)
bL = andL | xoL
bL = lShift(str(bL), 309)
bL = int(bL)
bL = '{0:b}'.format(bL)

# Binary to Decimal
bLDec = 0
bRDec = 0
for dL in bL:
    bLDec = bLDec * 2 + int(dL)

for dR in bR:
    bRDec = bRDec * 2 + int(dR)

iDecimal = 0
for dig in blocks:
    iDecimal = iDecimal * 2 + int(dig)

# Creating factors
factorL = 0
for d in str(bLDec):
    factorL += int(d)

factorR = 0
for d in str(bRDec):
    factorR += int(d)


bLDecF = factorR * bLDec

bRDecF = factorL * bRDec



# Ciphering
bLDecSTR = str(bLDecF)
bRDecSTR = str(bRDecF)

bLDec = ((bLDecF - int(lShift(bRDecSTR, 1270))) + (bLDecF - int(rShift(bRDecSTR, 309))) + (
        bLDecF - int(reverse(bRDecSTR, -31, 286)))) ** 3

bRDec = ((bRDecF - int(lShift(bLDecSTR, 1469))) + (bRDecF - int(rShift(bLDecSTR, 309))) + (
        bRDecF - int(reverse(bLDecSTR, 46, 199)))) ** 5

bLDec = int(bLDec)
bRDec = int(bRDec)

if bLDec < 0:
    bLDec = bLDec * -1

if bRDec < 0:
    bRDec = bRDec * -1


iLen = len(i)

# Finding the logarithmic values of both blocks
Yl = math.log(bLDec, iLen)
Yr = math.log(bRDec, iLen)

if Yr < 0:
    Yr = Yr * -1

if Yl < 0:
    Yl = Yl * -1




# K constants
primesR = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
           223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
           349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
           479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
           619]
primesL = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
           223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
           349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
           479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
           619]

for e in primesR:
    e = e * Yl
    e = e / iLen
    e = int(math.ceil(e))
    bRDec = (e * bRDec) + e

for e in primesL:
    e = e * Yr
    e = e / iLen
    e = int(math.ceil(e))
    bLDec = (e * bLDec) + e


Y = Yl * Yr

Y = int(math.floor(Y))


bDec = (bRDec + bLDec) / Y
bDec = lShift(str(bDec), Y)

bDec = int(bDec)

# Decimal to Binary
bBin = bin(bDec).replace('0b', '')


bBSize = len(bBin)

if bBSize > 1024:
    pvRb = ((bBSize // 1024) + 1) * 1024 - bBSize
    padGRb = ''
    padGRb = padGRb.ljust(pvRb, '0')
    bBin = bBin + padGRb


bBin = str(bBin)



bBin = reverse(bBin, -306, -604)
bBin = lShift(bBin, 1024)
bBin = reverse(bBin, -910, -295)


bBin = str(bBin)

elementSize = 1024

bB = list()

for i in range(0, len(bBin), elementSize):
    bB.append(bBin[i:i + elementSize])


finalBlock = bB[0]

finalBlock = str(finalBlock)
finalBlock = finalBlock.replace('L', '')








final = hex(int(finalBlock, 2))
tf = time.time()
processTime = tf - ti

print(final)
print(processTime)
print(iLen)