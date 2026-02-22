import re

class ChatFilter:
    def __init__(self):
        self.patterns = {
            'mentions': r'@\w+',  # Matches @mentions
            'telegram_links': r't.me/[\w]+',  # Matches Telegram links
            'phone_numbers': r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}',  # Matches phone numbers
            'card_numbers': r'\b(?:\d[ -]*?){13,16}\b',  # Matches credit card numbers
            'payment_keywords': r'\b(payment|invoice|checkout|pay|bill)\b'  # Matches payment-related keywords
        }

    def filter_message(self, message):
        filtered = {}
        for key, pattern in self.patterns.items():
            found = re.findall(pattern, message)
            if found:
                filtered[key] = found
        return filtered
