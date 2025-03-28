import re

def analyze_password(password):
    # Criteria
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*]', password))

    # Check strength
    if all([length_ok, has_upper, has_lower, has_digit, has_special]):
        return "Strong password!"
    else:
        feedback = "Weak password. Suggestions: "
        if not length_ok:
            feedback += "Use 8+ characters. "
        if not has_upper:
            feedback += "Add uppercase letters. "
        if not has_lower:
            feedback += "Add lowercase letters. "
        if not has_digit:
            feedback += "Add numbers. "
        if not has_special:
            feedback += "Add special characters (!@#). "
        return feedback

# Test it
password = input("Enter a password to analyze: ")
result = analyze_password(password)
print(result)