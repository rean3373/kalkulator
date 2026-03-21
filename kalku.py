from decimal import Decimal

def format_angka(angka):
    angka = Decimal(str(angka))
    hasil = format(angka, 'f').rstrip('0').rstrip('.')
    return hasil.replace('.', ',')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

print("Kalkulator Sederhana")
print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")

choice = input("Masukkan pilihan (1/2/3/4/5): ")

try:
    num1 = float(input("Masukkan bilangan pertama: "))
    num2 = float(input("Masukkan bilangan kedua: "))

    if choice == '1':
        hasil = add(num1, num2)
        print(f"{format_angka(num1)} + {format_angka(num2)} = {format_angka(hasil)}")

    elif choice == '2':
        hasil = subtract(num1, num2)
        print(f"{format_angka(num1)} - {format_angka(num2)} = {format_angka(hasil)}")

    elif choice == '3':
        hasil = multiply(num1, num2)
        print(f"{format_angka(num1)} * {format_angka(num2)} = {format_angka(hasil)}")

    elif choice == '4':
        if num2 == 0:
            print("Tidak bisa dibagi dengan nol.")
        else:
            hasil = divide(num1, num2)
            print(f"{format_angka(num1)} / {format_angka(num2)} = {format_angka(hasil)}")

    elif choice == '5':
        hasil = exponent(num1, num2)
        print(f"{format_angka(num1)} ^ {format_angka(num2)} = {format_angka(hasil)}")

    else:
        print("Pilihan tidak valid.")

except ValueError:
    print("Input tidak valid! Harap masukkan angka.")
