import segno
s = "Hallo Every"
resp = segno.make_qr(s)
resp.save(
    "qr.png",
    scale = 10,
    light = "lightwhite"
)