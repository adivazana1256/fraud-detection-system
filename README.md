# Fraud Detection System

## Overview
This project simulates a fraud detection system for financial transactions.

The goal is to identify suspicious transactions using a rule-based risk scoring approach.

## Problem
Financial systems process many transactions every day.  
Some of them may be suspicious due to unusual behavior such as:
- high transaction amounts
- unusual transaction hours
- foreign countries
- too many transactions in a short time

## Approach

### 1. Data Simulation
Generated 1000 synthetic transactions with:
- user_id
- amount
- hour
- country
- transactions_last_10min

### 2. Risk Scoring
Each transaction receives a risk score based on suspicious features:
- high amount
- frequent recent transactions
- foreign country
- unusual hour

### 3. Fraud Classification
Transactions with risk score above a defined threshold are classified as fraud.

### 4. Analysis
The project analyzes:
- total fraud vs non-fraud transactions
- average transaction amount
- fraud by country
- fraud by hour

### 5. Visualization
The project includes charts for:
- fraud vs non-fraud
- fraud by country
- fraud by hour

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib

## Key Insight
This project demonstrates how rule-based systems can detect suspicious behavior and how risk scoring can improve decision-making compared to a simple binary rule.

## Future Improvements
- add machine learning model
- track user normal behavior over time
- improve fraud detection logic using historical patterns