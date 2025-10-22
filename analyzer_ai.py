import pandas as pd
import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# Fix Windows console for emojis
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load data
data = pd.read_csv("data.csv")

# Basic analysis
total_sales = data["sales"].sum()
average_sales = data["sales"].mean()
max_sales = data["sales"].max()
min_sales = data["sales"].min()

print("📊 SALES REPORT")
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Highest Sale: {max_sales}")
print(f"Lowest Sale: {min_sales}")
print("\n🤖 Generating AI insights... Please wait...\n")

# Prepare data summary for AI
summary = f"""
We have sales data with:
- Total Sales: {total_sales}
- Average Sales: {average_sales}
- Highest Sale: {max_sales}
- Lowest Sale: {min_sales}

Please analyze performance and provide key insights in 3-5 sentences.
"""

# Use a model that exists in your account
try:
    model = genai.GenerativeModel("models/gemini-pro-latest")
    response = model.generate_content(summary)
    print("🧠 AI INSIGHT:\n")
    print(response.text)

except Exception as e:
    print("❌ Error while generating AI insight:")
    print(str(e))
