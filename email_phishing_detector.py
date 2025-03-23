import re

phishing_keywords = [
    r"urgent", r"click here",
    r"free gift", r"congratulations", r"lottery", r"bank details",
    r"claim your prize", r"credit card", r"refund", r"limited time offer"
]

def detect_phishing(email_text):
    
    email_text = email_text.lower()

    
    for keyword in phishing_keywords:
        if re.search(keyword, email_text):
            return "Phishing Alert! Suspicious content detected."
    
    return "Safe....No phishing signs detected."

email = """
Dear user,

Congratulations! You have won a FREE GIFT. Click here to claim your prize. 
Please verify your account by providing your bank details.

Best regards,
Unknown Sender
"""

result = detect_phishing(email)
print(result)
