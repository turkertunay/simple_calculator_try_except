
n_1 = input("birinci sayıyı girin: ")
n_2 = input("ikinci sayıyı girin: ")

islem = input("işlemi girin: ")

try:
    if islem == "+":
        sonuc = float(n_1) + float(n_2)
    if islem == "-":
        sonuc = float(n_1) - float(n_2)
    if islem == "*":
        sonuc = float(n_1) * float(n_2)
    if islem == "/":
        sonuc = float(n_1) / float(n_2)

    if islem not in ["+", "-", "*", "/"]:
        sonuc = ("girdiğiniz değer dört işlemden birisi değil.")

except(ValueError):
    sonuc = ("girdiğiniz değerlerden en az biri, bir sayı değil.")
except(ZeroDivisionError):
    sonuc = ("bir sayıyı sıfıra bölemeyiz.")

print(sonuc)

