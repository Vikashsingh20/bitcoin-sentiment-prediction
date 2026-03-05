import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load model once (faster)
@st.cache_resource
def load_model():
    return joblib.load("btc_sentiment_model.pkl")

model = load_model()

st.title("📈 Bitcoin Market Direction Predictor")
st.write("Enter today's tweets to predict tomorrow's BTC direction.")

# User input
tweets_input = st.text_area(
    "Enter tweets (one per line):",
    height=200
)

if st.button("Predict Tomorrow"):

    if tweets_input.strip() == "":
        st.warning("Please enter at least one tweet.")
    else:
        tweets_today = tweets_input.split("\n")

        # Sentiment calculation
        analyzer = SentimentIntensityAnalyzer()
        sentiments = []

        for text in tweets_today:
            score = analyzer.polarity_scores(str(text))['compound']
            sentiments.append(score)

        avg_sentiment = np.mean(sentiments)

        # Download latest BTC data
        btc = yf.download("BTC-USD", period="10d")
        btc.reset_index(inplace=True)

        # Feature engineering
        btc['return_1d'] = btc['Close'].pct_change()
        btc['volatility'] = (btc['High'] - btc['Low']) / btc['Open']
        btc['volume_change'] = btc['Volume'].pct_change()
        btc['log_volume'] = np.log1p(btc['Volume'])

        btc = btc.dropna()
        latest = btc.iloc[-1]

        # Create feature row
        X_live = pd.DataFrame([{
            'avg_sentiment': avg_sentiment,
            'return_1d': latest['return_1d'],
            'volatility': latest['volatility'],
            'volume_change': latest['volume_change'],
            'log_volume': latest['log_volume']
        }])

        X_live = X_live.astype(float)

        # Prediction
        prediction = model.predict(X_live)[0]
        probability = model.predict_proba(X_live)[0][1]

        if prediction == 1:
            st.success(f"📈 Market Likely UP Tomorrow")
        else:
            st.error(f"📉 Market Likely DOWN Tomorrow")

        st.write(f"Confidence: {probability:.2%}")