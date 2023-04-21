from PIL import Image

def encode(image_name, text, sigma, lmb):
    image = Image.open('Lenna.png')
    px = image.load()
    x = sigma
    y = sigma
    for char in text:
        bits = "{0:b}".format(ord(char))
        for bit in bits:
            r, g, b = px[x, y]
            if bit == "0":
                px[x, y] = (r, g, b + int(lmb * (0.299 * r + 0.587 * g + 0.114 * b)))
            else:
                px[x, y] = (r, g, b - int(lmb * (0.299 * r + 0.587 * g + 0.114 * b)))

            y += 1
            if y >= image.size[1]:
                x += 1
                y = 0

    image.save('out.png')
    image.show()

def decode(image_name, text_len, sigma, lmb):
    char_bit_count = len("{0:b}".format(ord('a')))
    image = Image.open(image_name)
    px = image.load()

    x = sigma
    y = sigma
    text = ""
    bits = ""
    for index in range(0, text_len * char_bit_count):
        r, g, b = px[x, y]
        sum = 0
        for i in range(1, sigma + 1):
            r1, g1, b1 = px[x, y + i]
            r2, g2, b2 = px[x, y - i]
            r3, g3, b3 = px[x + i, y]
            r4, g4, b4 = px[x - i, y]
            sum += b1 + b2 + b3 + b4
        crit_b = sum / (4 * sigma)
        bits += "0" if b > crit_b else "1"

        y += 1
        if y >= image.size[1]:
            x += 1
            y = 0

        if len(bits) >= char_bit_count:
            text += chr(int(bits, 2))
            bits = ""      

    print(text)

text = "message"
print(text)
print("\n")
encode("Lenna.png", text, 2, 0.1)
decode("out.png", len(text), 2, 0.1)