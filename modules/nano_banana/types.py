from typing import List, Optional, TypedDict


class ReferenceImage(TypedDict):
    url: str
    description: Optional[str]


class BananaRequest(TypedDict):
    prompt: str
    reference_images: Optional[List[ReferenceImage]]
    aspect_ratio: Optional[str]
    style: Optional[str]
    seed: Optional[int]


class BananaResult(TypedDict):
    image_url: str
    model: str
    request_id: Optional[str]
