import base64
with open("Capture6.PNG", "rb") as img:
    res = base64.b64encode(img.read())
    print(res)

sv = open("sv_img.png", "wb")
sv.write(res.decode('base64'))
sv.close()
