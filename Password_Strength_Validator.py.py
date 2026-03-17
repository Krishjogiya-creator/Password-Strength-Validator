# Project: Password Security Analyzer
# Author : Krish Jogiya
# Purpose:  To help users create more secure passswords for their online accounts.

def analyze_password(password):
    """
    Function to check a password against 4 security criteria.
    Returns a score out of 4 and a list of suggestions.
    """
    score = 0
    suggestions = []
    # Criteria 1: Length Check
    if len(password) >=8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters.")
    #Criteria 2: Number Check
    if any(char.isdigit() for char in password):
            score += 1
    else:
        suggestions.append("Include at least one digit (0-9).")
    #Criteria 3: Case Check (Uppercase)
    if any(char .isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    #Criteria 4: Special Character Check
    special_characters = "!@#$%^&()"
    if any(char in special_characters for char in password):
        score += 1
    else:
        suggestions.append("Add a special character (e.g.,@#$).")
    return score, suggestions
    
    # --- User Interface ---
print("========================================")
print("   PYTHON PASSWORD SECURITY ANALYZER    ")
print("========================================\n")
# --- 1. GET USER INPUT ---
# This line asks the user to type their password
user_pass = input("Please enter a password to test: ")

# --- 2. RUN THE ANALYZER ---
# This line "calls" your function and creates the 'score' variable score,
score, tips = analyze_password(user_pass)
# Display Results
print("\n--- Results ---")
if score == 4:
    print("STATUS: STRONG(EXCELLENT)")
elif score == 3:
    print("STATUS: GOOD(COULD BE BETTER)")
else:
    print("STATUS: WEAK(UNSAFE)")

# Show tips if the passsword isn't perfect
if tips:
    print("\nHow to improve:")
    for tip in tips:
        print(f" - {tip}")

print("\n========================================")
