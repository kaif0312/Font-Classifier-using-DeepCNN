import os
from PIL import Image, ImageDraw, ImageFont

# Define text
text = "Hello World!"

# Define font directory
font_directory = "fonts"

# Define output directory
output_directory = "output_images"

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List all font files in the directory
font_files = [f for f in os.listdir(font_directory) if f.endswith('.ttf')]

# Define font sizes
font_sizes = [20, 24, 28, 32, 36]

# Create images with text using different fonts and sizes
for font_file in font_files:
    font_name = os.path.splitext(font_file)[0]
    for font_size in font_sizes:
        # Load font
        font_path = os.path.join(font_directory, font_file)
        font = ImageFont.truetype(font_path, font_size)
        
        # Create image
        image = Image.new("RGB", (1920, 720), "white")
        draw = ImageDraw.Draw(image)
        
        # Get size of text
        text_width, text_height = font.getsize(text)
        
        # Position text in the center
        x = (image.width - text_width) / 2
        y = (image.height - text_height) / 2
        
        # Draw text
        draw.text((x, y), text, fill="black", font=font)
        
        # Save image to the output directory
        output_path = os.path.join(output_directory, f"hello_{font_name}_{font_size}.png")
        image.save(output_path)

print("Images created successfully and saved to the output folder!")
