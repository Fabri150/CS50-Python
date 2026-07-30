import sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    extensions = (".jpg", ".jpeg", ".png")
    if not sys.argv[1].endswith(extensions) or not sys.argv[2].endswith(extensions):
        sys.exit("Invalid Input")
    if sys.argv[1].rsplit(".", 1)[1] != sys.argv[2].rsplit(".", 1)[1]:
        sys.exit("Input and output have different extensions")
    try:
        with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt:
                img = ImageOps.fit(img, shirt.size)
                print(img.size, shirt.size)
                img.paste(shirt, shirt)
                img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")