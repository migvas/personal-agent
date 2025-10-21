from datetime import datetime, timezone


def get_current_date():
    """
    Return the current date and time in ISO 8601 format (UTC).

    Args:
        None

    Returns:
        str: The current UTC date and time in ISO 8601 format
    """
    return datetime.now(timezone.utc).isoformat() + "Z"
