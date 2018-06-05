from PIL import Image

im = Image.open("元画像")
image = im.convert("RGB")
fl = Image.open("埋め込みたい文字の画像")
flag = fl.convert("RGB")


for x in range([x-size]):
    for y in range([y-size]):
        r,g,b = image.getpixel((x, y))
		# 下位1bitを操作
        r = r&0b11111110 | int(flag.getpixel((x, y))[0] > 128)<<1
        image.putpixel((x, y), (r,g,b))

image.save("完成画像")
