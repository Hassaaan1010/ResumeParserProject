import re

def sanitize_name(name):
    # Remove non-alphabetic characters and trim whitespace
    if name:
        return re.sub(r"[^a-zA-Z\s]", "", name).strip()
    return ""

def sanitize_email(email):
    # Ensure the email is in a valid format
    if email and re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return email.strip()
    return ""

def sanitize_mobile_number(mobile_number):
    # Remove unwanted characters and keep valid phone numbers
    if mobile_number:
        sanitized = re.sub(r"[^\d+]", "", mobile_number)  # Remove non-numeric characters except '+'
        return sanitized if 7 <= len(sanitized) <= 15 else ""
    return ""


def sanitize_candidate_data(extracted_data):
    sanitized_data = {
        'first_name': sanitize_name(extracted_data.get('first_name')),
        'email': sanitize_email(extracted_data.get('email')),
        'mobile_number': sanitize_mobile_number(extracted_data.get('mobile_number')),
    }
    return sanitized_data