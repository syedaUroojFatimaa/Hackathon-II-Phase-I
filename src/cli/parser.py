"""CLI parser - Input validation and parsing functions"""


def validate_id(id_str: str) -> int | None:
    """Validate and parse a todo ID from user input.

    Args:
        id_str: The string to parse as an ID

    Returns:
        The parsed integer ID, or None if invalid
    """
    try:
        id_val = int(id_str)
        if id_val > 0:
            return id_val
        return None
    except ValueError:
        return None


def get_user_input(prompt: str) -> str:
    """Get user input with a prompt.

    Args:
        prompt: The prompt to display

    Returns:
        The user's input (stripped of whitespace)
    """
    return input(prompt).strip()
