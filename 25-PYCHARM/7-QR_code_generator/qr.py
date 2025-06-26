import pyqrcode

url:str = input("Lütfen QR koda çevirmek istediğiniz URL'nizi giriniz: ")

qr_code = pyqrcode.create(url)

qr_code.svg("qr.svg",scale=5)