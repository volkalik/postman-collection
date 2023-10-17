from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_size=20, image_size=(400, 200), output_path="output.png"):
    # Create a new image with a white background
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.load_default()  # You can also provide the path to a specific font file

    # Calculate text position to center it in the image
    text_width, text_height = draw.textsize(text, font)
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill="black")

    # Save the image
    image.save(output_path)
    print(f"Image saved to '{output_path}'")

# Example usage
text_to_image("Hello, World!", font_size=30, image_size=(400, 200), output_path="/Users/oleksandr.volk/Documents/Myprojects/First_project/output.png")
