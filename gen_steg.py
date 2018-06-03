from PIL import Image

im = Image.open("元画像")
image = im.convert("RGB")
fl = Image.open("埋め込みたい文字の画像")
flag = fl.convert("RGB")


for x in range(480):
    for x in range(640):
        r,g,b = image.getpixel((x, y))
		# 下位1bitを操作
        r = r&11111110 | int(flag.getpixel((x, y))[0] > 128)<<1
        #r = r&11111101 | int(flag.getpixel((x, y))[0] > 128)<<1
        #r = r&11111011 | int(flag.getpixel((x, y))[0] > 128)<<1
        image.putpixel((x, y), (r,g,b))

image.save("完成画像")
