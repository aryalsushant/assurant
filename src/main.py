   # src/main.py
import os
import openai
from dotenv import load_dotenv
from image_analysis import analyze_image
from claims_analysis import analyze_claim

load_dotenv()  # Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
       # User selects claim PDF
       claim_pdf = input("Select a claim PDF from claims folder: ")
       claim_path = os.path.join('claims', claim_pdf)

       # User selects an image of the damage
       image_path = input("Select an image of the damage: ")

       # Analyze claim and image
       anomaly_rating = analyze_claim(claim_path)
       image_rating = analyze_image(image_path)

       # Calculate overall rating
       overall_rating = int(anomaly_rating) + image_rating

       # Output results
       print(f"Anomaly Rating: {anomaly_rating}")
       print(f"Image Manipulation Rating: {image_rating}/5")
       print(f"Overall Fraud Chances Rating: {overall_rating}/10")

       # Continue conversation with AI agent
       while True:
           user_input = input("Ask the AI agent a question (or type 'exit' to quit): ")
           if user_input.lower() == 'exit':
               break
           response = openai.ChatCompletion.create(
               model="gpt-3.5-turbo",
               messages=[{"role": "user", "content": user_input}]
           )
           print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
       main()