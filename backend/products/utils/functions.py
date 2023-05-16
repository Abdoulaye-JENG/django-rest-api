import string
import secrets


def generate_random_string(
    length: int = 7, lowercase=True, uppercase=True, numbers=True
):
    """Generate Random secure string

    Args:
        length (int, optional): String length. Defaults to 7.

    Returns:
        str: Generated String
    """
    if not (lowercase or uppercase):
        raise ValueError(
            "Generated String must have Lowercase or Uppercase characters."
        )
    if not (uppercase or numbers) and lowercase:
        seq = string.ascii_lowercase
    elif not (lowercase or numbers) and uppercase:
        seq = string.ascii_uppercase
    elif (lowercase and uppercase) and not numbers:
        seq = string.ascii_uppercase + string.ascii_lowercase
    elif (lowercase and numbers) and not uppercase:
        seq = string.ascii_lowercase + string.digits
    elif (uppercase and numbers) and not lowercase:
        seq = string.ascii_uppercase + string.digits
    else:
        seq = string.ascii_uppercase + string.ascii_lowercase + string.digits

    result_string = "".join(secrets.choice(seq) for _ in range(length))
    return result_string
