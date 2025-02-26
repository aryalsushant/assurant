# src/utils.py
import pandas as pd

def extract_claim_info(claim_id):
    # Adjusted path to go up one directory level to access claims.csv
    claims_df = pd.read_csv('../claims/claims.csv')
    claim = claims_df[claims_df['claim_id'] == claim_id]
    
    if not claim.empty:
        return claim.to_dict(orient='records')[0]  # Return the first matching claim as a dictionary
    return "Claim not found."

def get_image_filename(claim_id):
    # The image filename is simply the claim ID with a .jpg extension
    return f"{claim_id}.jpg"