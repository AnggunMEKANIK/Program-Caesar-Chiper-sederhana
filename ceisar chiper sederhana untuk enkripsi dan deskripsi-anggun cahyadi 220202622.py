# Fungsi untuk enkripsi menggunakan Caesar Cipher
def encrypt(text, shift):
    result = ""
    
    # Looping setiap karakter dalam teks
    for char in text:
        # Enkripsi huruf kapital
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Enkripsi huruf kecil
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Jika bukan huruf (spasi, angka, simbol), tidak berubah
            result += char
    
    return result

# Fungsi untuk dekripsi menggunakan Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Contoh penggunaan
plain_text = "test saja!"
shift_value = 3

encrypted_text = encrypt(plain_text, shift_value)
print(f"Teks terenkripsi: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift_value)
print(f"Teks terdekripsi: {decrypted_text}")
