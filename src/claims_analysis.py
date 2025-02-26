# src/claims_analysis.py
import openai
from utils import extract_claim_info

def analyze_claim(claim_id):
    # Extract claim information from the claims.csv
    claim_info = extract_claim_info(claim_id)

    if claim_info == "Claim not found.":
        return claim_info

    # Use AI agent to analyze the claim
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Analyze this claim: {claim_info}"}]
    )
    
    # Extract anomaly score from the response
    anomaly_score = response['choices'][0]['message']['content']
    return anomaly_score

def get_image_filename(claim_id):
    # The image filename is simply the claim ID with a .jpg extension
    return f"{claim_id}.jpg"