# Emre'nin Python Pratikleri - Sadece Sorular (Kodlarını sen yaz)

# 1. Görev:
# Aşağıdaki 3 sayının toplamını bir değişkene ata ve sonucu yazdır
a = 23
b = 7
c = 13.5

# Kodunu buraya yaz:

d = a + b + c
print("1️⃣ Toplam:",d)


# 2. Görev:
# Adını ve soyadını ayrı değişkenlerde tut. Bunları birleştir ve hepsini büyük harfli olarak ekrana yazdır.

name = "emre"
surname = "ozden"

# Kodunu buraya yaz:

fullName = name + " " + surname
print(fullName.upper())

# 3. Görev:
# Aşağıdaki kelimenin ilk ve son harfini ekrana yazdır

word = "yusufemre"

# Kodunu buraya yaz:

a = word[0]+word[-1]
print(a)

# 4. Görev:
# Aşağıdaki cümleyi boşluklardan ayır ve kaç kelimeden oluştuğunu ekrana yazdır

text = "bu bir python dersi"

# Kodunu buraya yaz:

print(text.split(" "))
a = text.count(" ") + 1
print("kelime sayısı:", a)

# 5. Görev:
# Aşağıdaki kelimenin ortadaki karakterini yazdır (tek ise 1 harf, çiftse 2 harf)

text = "ankara"

# Kodunu buraya yaz:

