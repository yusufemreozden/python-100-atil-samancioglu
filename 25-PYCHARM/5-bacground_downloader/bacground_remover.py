from rembg import remove

input_path = "sincap.jpg"

output_path = "sincap.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)