import sys

from langchain.tools import tool
import cv2
import numpy as np

@tool('bounding_box_tool', return_direct=False)
def bounding_box_tool(image_path: str) -> str:
    """This tool creates a bounding box around titles or headers in an image."""
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            return 'Error: Image not found.'

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use a simple threshold to find text areas
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        # Find contours of the text areas
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around contours
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save the output image
        output_path = 'output_with_bounding_boxes.png'
        cv2.imwrite(output_path, image)

        return f'Bounding boxes created and saved to {output_path}.'
    except:
        return 'Error: ' + str(sys.exc_info())