from PIL import Image, ImageDraw, ImageFont

# ------------------------
# Settings
# ------------------------
text = "GENESIS BCS CARE"
font_size = 150
font_path = "Poppins-Bold.ttf"  # or any TTF font you have
output_file = "genesis_bcs_care.png"

# ------------------------
# Create Image
# ------------------------
# Load font
try:
    font = ImageFont.truetype(font_path, font_size)
except:
    print("⚠️ Poppins font not found! Using default font.")
    font = ImageFont.load_default()

# Measure text size
dummy_img = Image.new('RGBA', (10, 10))
draw = ImageDraw.Draw(dummy_img)
text_width, text_height = draw.textsize(text, font=font)

# Create transparent image
img = Image.new('RGBA', (text_width + 50, text_height + 50), (255, 255, 255, 0))

# Draw text
draw = ImageDraw.Draw(img)
draw.text((25, 25), text, font=font, fill=(0, 0, 0, 255))  # Black color text

# Save PNG
img.save(output_file)

print(f"✅ Saved as {output_file}")
