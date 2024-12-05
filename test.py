from PIL import Image

def test(f):
    img = Image.open(f).convert("RGBA")
    img = img.point(lambda p: p // 2 )
    img.save(f)

test("images/Thief1_.png")
test("images/sliding_.png")