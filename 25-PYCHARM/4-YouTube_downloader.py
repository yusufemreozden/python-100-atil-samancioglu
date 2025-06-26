import pytube 

print(pytube.__version__)

url:str = input("\nLütfen indirmek istediğiniz YouTube içeriğinin URL'sini giriniz: ")

# path = "/Users/yusufemreozden/Desktop"

pytube.YouTube(url).streams.get_lowest_resolution().download(output_path=path)

# https://www.youtube.com/watch?v=wbFE0Hs2N4k