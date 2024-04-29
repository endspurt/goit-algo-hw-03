import re

def normalize_phone(phone_number):
    # Remove all characters except digits and '+'
    sanitized = re.sub(r"[^\d+]", "", phone_number.strip())

    # Check if the number starts with '+' and has sufficient digits
    if sanitized.startswith('+'):
        # Already in international format
        if len(sanitized) == 13 and sanitized[1:].isdigit():
            return sanitized
    else:
        # Check for national number without international code
        if sanitized.startswith('380') and len(sanitized) == 12:
            return '+' + sanitized
        elif len(sanitized) >= 9:
            # Assume it's a Ukrainian number missing the international code
            return '+38' + sanitized

    # If the number format is not as expected, return the original input
    return phone_number  # this can be adjusted based on how strict you want to be with formatting

# Example usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalisierte Telefonnummern für SMS-Versand:", sanitized_numbers)
