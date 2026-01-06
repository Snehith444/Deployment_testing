from typing import Any, Optional

def build_response(
    *,
    success: bool,
    message: str,
    data: Optional[Any] = None
):
    return {
        "success": success,
        "message": message,
        "data": data
    }
