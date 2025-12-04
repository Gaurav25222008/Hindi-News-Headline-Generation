import streamlit as st
# Run the Streamlit app and create a public URL
from pyngrok import ngrok

!streamlit run deploy.py &

# Create a public URL using ngrok
public_url = ngrok.connect(port='8501')
print(f"Streamlit app is live at: {public_url}")