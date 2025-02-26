   # src/claims_analysis.py
import openai
from utils import extract_claim_info

def analyze_claim(claim_pdf):
       # Extract claim information from the PDF
       claim_info = extract_claim_info(claim_pdf)

       # Use AI agent to analyze the claim
       response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=[{"role": "user", "content": f"Analyze this claim: {claim_info}"}]
       )
       
       # Extract anomaly score from the response
       anomaly_score = response['choices'][0]['message']['content']
       return anomaly_score