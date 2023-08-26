from PIL import Image, ImageDraw

def get_circular_image(pil_image):
    width, height = pil_image.size

    # Create a mask for circular crop
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)

    # Apply mask to image
    circular_cropped = Image.new("RGBA", (width, height))
    circular_cropped.paste(pil_image, mask=mask)
    return circular_cropped
