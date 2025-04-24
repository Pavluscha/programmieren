#!/usr/bin/env python3

class prg:
    pass

prg.verbose = False

def Q1(b):
    return b ^ ((b << 17) | (b >> 15)) & ((1 << 32) - 1)

def rotate_left_32bit(value, shift):
    shift %= 32  # Ensure shift is within 0–31
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def Q(b):
    return b ^ rotate_left_32bit(b, 17)

def R(b):
    x = [5]*32
    x[0] = 0
    last_index = 0
    for i in range(1,32):
        next_index = (last_index+17)%32
        next_b_bit =  ((1 << next_index ) & b) >> next_index
        x[next_index] = next_b_bit ^ x[last_index]
        last_index = next_index

    bin_str = ''
    for i in range(0,32):
        bin_str = str(x[i])+bin_str

    print(bin_str)
    bin_val = int(bin_str, 2)
    print(hex(bin_val))

    inv_bin_val = ~bin_val & 0xFFFFFFFF
    print(f"{inv_bin_val:032b}")
    print(hex(inv_bin_val))

def H(nachricht):
    if prg.verbose:
        print(f"nachricht={nachricht}")
    S = int(0x524f464c)
    count = 0
    if prg.verbose:
        print(f"S_{count}={hex(S)}")
    nachricht = nachricht.encode("utf-8")
    hex_wert = nachricht.hex()

    while hex_wert:
        if len(hex_wert) < 8:   
            P = hex_wert.ljust(8, 'F')
            hex_wert = "" 

        else:
            P = hex_wert[:8]
            hex_wert = hex_wert[8:]

        count += 1
        if prg.verbose:
            print(f"buffer={P}")
        P = int(P, 16)
        S = Q(S ^ P)
        if prg.verbose:
            print(f"S_{count}={hex(S)}")

    if prg.verbose:
        print(f"return {hex(Q(S))}")

    return hex(Q(S))

test_vektoren= {
    "": "ded7e2d2",
    "A": "5d725f7f",
    "AB": "5f3b5f7f",
    "ABC": "5f39137f",
    "ABCD": "5f391128",
    "ABCDE": "2f69af58",
}

S = int(0x524f464c)

print(f"S0 = {hex(S)}")
print(f"Q(S0) = {hex(Q(S))}")

R(Q(S))

P = int(0x7afd368c)
S1 = int(0x524f464c)
S2 = int(0xadb0b9b3)

print(hex(Q(S1 ^ P)))
print(hex( Q( Q(S1 ^ P) ) ))
print(hex(Q(S2 ^ P)))
print(hex( Q( Q(S2 ^ P) ) ))


#print(f"R(Q(S0)) = {hex(R(Q(S)))}")

#print(f"Q(Q(S0)) = {hex(Q(Q(S)))}")
#print(f"Q(Q(Q(S0))) = {hex(Q(Q(Q(S))))}")
#
#print(f"QR(Q(S0)) = {hex(Qr(Q(S)))}")
#
#for input, erwarteter_Hash in test_vektoren.items():
#    if(H(input) == "0x" + erwarteter_Hash):
#        print(f"H(\"{input}\") = {H(input)}")
#    else:
#        print("Error")
#
#prg.verbose = True
#
#K = "x"*16
#
#H(K+"abcd")
#
#H(K+"abcdef")
#
#H(K+"abcdefghijk")



