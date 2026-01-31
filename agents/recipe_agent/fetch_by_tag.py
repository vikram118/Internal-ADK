import requests

def fetch_assets_by_tags(tags: list[str], limit: int = 5) -> list[dict]:
    """Fetch reference media assets by tags.
    
    Args:
        tags: List of lowercase, single-word food/cooking related tags
        limit: Maximum number of assets to return (default: 5)
        
    Returns:
        List of asset dictionaries matching all provided tags
    """
    params = {
        "tags": ",".join(tags)
    }

    resp = requests.get(
        "https://media.cookclub.ai/api/assets",
        params=params,
        timeout=5
    )
    resp.raise_for_status()

    assets = resp.json().get("assets", [])

    # TEMP: client-side AND filtering
    filtered = [
        a for a in assets
        if set(tags).issubset(set(a.get("tags", [])))
    ]

    return filtered[:limit]