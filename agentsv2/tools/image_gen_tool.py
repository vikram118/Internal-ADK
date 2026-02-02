from google import genai
from PIL import Image
import uuid

client = genai.Client()

def generate_image(prompt: str) -> str:
    """
    Generates an image from a text prompt and saves it to disk.
    Returns the file path.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt],
    )

    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            filename = f"generated_{uuid.uuid4().hex}.png"
            image.save(filename)
            return filename

    return "NO_IMAGE_GENERATED"
