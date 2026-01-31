from typing import Optional
from google import genai
from modules.nano_banana.types import BananaRequest, BananaResult

# Initialize once
_client = genai.Client()


def generate_image(request: BananaRequest) -> BananaResult:
    """
    Generate an image using Google Nano Banana.

    This function is deterministic given the same inputs.
    """

    # Build prompt text
    prompt_parts = [request["prompt"]]

    # Attach reference images if present
    if request.get("reference_images"):
        for ref in request["reference_images"]:
            prompt_parts.append(
                f"Reference image: {ref['url']}"
                + (f" ({ref['description']})" if ref.get("description") else "")
            )

    prompt_text = "\n".join(prompt_parts)

    # Call Nano Banana
    response = _client.models.generate_images(
        model="imagen-3.0-generate-002",  # Nano Banana
        prompt=prompt_text,
        config={
            "aspectRatio": request.get("aspect_ratio", "1:1"),
            "seed": request.get("seed"),
        },
    )

    # Basic safety check
    if not response.images:
        raise RuntimeError("Nano Banana returned no images")

    image = response.images[0]

    return {
        "image_url": image.uri,
        "model": "nano-banana",
        "request_id": getattr(response, "request_id", None),
    }
