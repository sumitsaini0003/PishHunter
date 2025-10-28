import requests
import re
from urllib.parse import urlparse

# ---------------------------
# Simple keyword/phishing pattern check
# ---------------------------
def is_suspicious_url(url):
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'paypal', 'bank', 'account']
    shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 't.co']

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    keyword_score = sum(1 for word in suspicious_keywords if word in url.lower())
    shortened = any(short in domain for short in shorteners)

    return {
        'domain': domain,
        'keyword_score': keyword_score,
        'is_shortened': shortened
    }

# ---------------------------
# PhishTank URL Checker (Dummy Version)
# ---------------------------
def check_phishtank(url):
    # In real version, use API. For now, just return mock.
    print("Checking PhishTank... (mock)")
    return {'is_phishing': False, 'source': 'PhishTank'}

# ---------------------------
# MAIN FUNCTION
# ---------------------------
def analyze_url(url):
    print(f"Analyzing URL: {url}")

    result = {}
    
    # Step 1: Check via PhishTank
    result['phishtank'] = check_phishtank(url)

    # Step 2: Check for suspicious patterns
    pattern_result = is_suspicious_url(url)
    result['pattern'] = pattern_result

    # Step 3: Decide final status
    if result['phishtank']['is_phishing'] or result['pattern']['keyword_score'] >= 2:
        status = "❌ Likely Phishing"
    elif result['pattern']['is_shortened']:
        status = "⚠️ Shortened Link - Risky"
    else:
        status = "✅ Seems Safe (But Not Guaranteed)"

    print("\n=== Risk Analysis ===")
    print(f"Domain: {pattern_result['domain']}")
    print(f"Suspicious Keywords Found: {pattern_result['keyword_score']}")
    print(f"Shortened URL: {pattern_result['is_shortened']}")
    print(f"PhishTank Match: {result['phishtank']['is_phishing']}")
    print(f"➡ Final Status: {status}")

# ---------------------------
# RUN IT
# ---------------------------
if __name__ == "__main__":
    user_url = input("Enter the ad URL to analyze: ")
    analyze_url(user_url)
