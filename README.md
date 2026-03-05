# 📈 Bitcoin Market Direction Prediction using Sentiment Analysis

## 📌 Project Overview

This project predicts the **next-day direction of Bitcoin price (UP or DOWN)** using **Twitter sentiment analysis and machine learning**.

The system combines:

- Public sentiment from Bitcoin-related tweets
- Historical Bitcoin market data
- Market volatility and trading volume

These features are used to train a **machine learning model** that predicts whether the **Bitcoin market will go up or down tomorrow**.

---

## 🚀 Features

- 📊 Sentiment analysis on Bitcoin tweets
- 📈 Bitcoin market data using Yahoo Finance
- 🤖 Machine learning models for prediction
- 📉 Feature engineering on market indicators
- 🌐 Interactive **Streamlit web application**
- ⚡ Real-time prediction using live BTC data

---

## 🧠 Models Used

The following models were tested during experimentation:

| Model | Accuracy |
|------|------|
| Random Forest | 0.43 |
| Logistic Regression | 0.43 |
| XGBoost | **0.49 (Best Model)** |

The final deployed model is **XGBoost**.

---

## 📊 Features Used for Prediction

The model uses the following features:

- `avg_sentiment` → Average tweet sentiment score
- `return_1d` → Previous day price return
- `volatility` → Price volatility
- `volume_change` → Trading volume change
- `log_volume` → Log transformed trading volume

---

## 📂 Dataset

### Tweet Dataset

Source: **Bitcoin Twitter dataset**

Columns used:

- `date`
- `text`

Sentiment scores are calculated using **VADER Sentiment Analyzer**.

---

### Bitcoin Market Data

Market data is fetched using **Yahoo Finance API** via `yfinance`.

Columns used:

- Open
- Close
- High
- Low
- Volume

---

## ⚙️ Feature Engineering

Additional features created:

- Daily average tweet sentiment
- Next day return
- Market volatility
- Volume change
- Log volume transformation

Target variable:
