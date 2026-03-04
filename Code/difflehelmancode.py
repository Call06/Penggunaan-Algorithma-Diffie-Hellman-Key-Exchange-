# Program Pertukaran Kunci Diffie-Hellman Manual

def power_mod(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        exponent = exponent // 2
        
        base = (base * base) % modulus

    return result

print("======================================")
print(" Simulasi Diffie-Hellman Key Exchange ")
print("======================================\n")

# 1. Parameter Publik
p = 23   
g = 5    

print("Parameter Publik:")
print("p (prima)     =", p)
print("g (generator) =", g)
print("")

# 2. Input Kunci Privat
x = int(input("Masukkan kunci privat Alice (x): "))
y = int(input("Masukkan kunci privat Bob (y): "))
print("")

# 3. Hitung Kunci Publik
# A = g^x mod p
A = power_mod(g, x, p)

# B = g^y mod p
B = power_mod(g, y, p)

print("=== Proses Pertukaran ===")
print("Alice mengirim A =", A)
print("Bob mengirim B   =", B)
print("")

# 4. Hitung Shared Secret
# Alice menghitung S = B^x mod p
S_alice = power_mod(B, x, p)

# Bob menghitung S = A^y mod p
S_bob = power_mod(A, y, p)

print("=== Shared Secret ===")
print("Secret versi Alice =", S_alice)
print("Secret versi Bob   =", S_bob)
print("")

# 5. Verifikasi
if S_alice == S_bob:
    print("HASIL: Kunci rahasia berhasil dibuat dan sama.")
else:
    print("HASIL: Terjadi kesalahan, kunci tidak sama.")