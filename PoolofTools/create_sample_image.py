import sys
from langchain.tools import tool
from PIL import Image, ImageDraw, ImageFont

@tool('create_sample_image', return_direct=False)
def create_sample_image(image_path: str, text: str) -> str:
    """This tool creates a sample image with a title/header."""
    try:
        # Create a blank image with white background
        image = Image.new('RGB', (400, 200), color='white')
        draw = ImageDraw.Draw(image)

        # Define a font and draw the text
        font = ImageFont.load_default()
        draw.text((10, 80), text, fill='black', font=font)

        # Save the image
        image.save(image_path)

        return f'Sample image created and saved to {image_path}'
    except:
        return 'Error: ' + str(sys.exc_info())