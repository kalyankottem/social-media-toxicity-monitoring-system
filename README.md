# Social Media Toxicity and Abuse Monitoring System

## Description
This project is an NLP-based moderation dashboard designed to detect toxic, abusive, and offensive language in social media comments and posts. It helps online platforms automate moderation by identifying harmful content, measuring toxicity severity, and visualizing abuse patterns interactively.

---

## Problem Statement
Online platforms are increasingly affected by toxic, abusive, and offensive language, negatively impacting user experience and community standards. Manual moderation is not scalable for large volumes of user-generated content.

This project provides an automated toxicity monitoring and moderation dashboard.

---

## Objective
- Analyze comments and posts for toxic language  
- Classify content as Toxic or Non-Toxic  
- Identify frequently used abusive terms  
- Measure toxicity severity across datasets  
- Visualize toxicity insights interactively  

---

## Features
### Toxicity Classification
Classifies comments into:
- Toxic  
- Non-Toxic  

### Toxicity Severity Scoring
Assigns weighted severity scores based on abusive terms detected.

### Abusive Term Frequency Analysis
Tracks the most commonly used toxic/abusive words.

### Interactive Dashboard Visualizations
Displays:
- Toxic vs Non-Toxic Distribution  
- Toxicity Severity Histogram  
- Abusive Term Frequency Chart  
- Flagged Toxic Comment Table  

---

## Methodology
1. Load social media comments/posts  
2. Preprocess text  
3. Match toxic words against abuse lexicon  
4. Compute toxicity severity score  
5. Classify content based on toxicity presence  
6. Aggregate abusive term frequencies  
7. Visualize moderation insights in dashboard  

---

## Technologies Used
- Python  
- Streamlit  
- Pandas  
- Plotly  

---

## Output
The dashboard provides:
- Total Comments Count  
- Toxic Comments Count  
- Average Toxicity Score  
- Toxicity Distribution Pie Chart  
- Severity Distribution Histogram  
- Abusive Term Frequency Bar Chart  
- Toxic Comment Monitoring Table  

---

## Applications
- Social Media Moderation  
- Community Management  
- Toxic Behavior Monitoring  
- Online Platform Safety  
- Content Moderation Automation  

---

## Future Improvements
- Replace rule-based detection with ML/Transformer toxicity models  
- Add real-time moderation API integration  
- Support CSV Upload / Live Streams  
- Detect contextual / sarcastic toxicity  
- Deploy to cloud for production moderation  

---

## Run Locally
```bash
python -m streamlit run social_media_toxicity_dashboard.py
```
