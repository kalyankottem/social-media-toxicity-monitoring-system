import streamlit as st
import pandas as pd
import re
from collections import Counter
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Toxicity Monitoring Dashboard",
    layout="wide"
)

st.title("🛡 Social Media Toxicity & Abuse Monitoring Dashboard")

# -----------------------------
# SAMPLE SOCIAL MEDIA COMMENTS
# -----------------------------
comments = [
    "You are stupid and useless",
    "Amazing platform, I love it",
    "Worst app ever, trash service",
    "Great experience overall",
    "This update is horrible and stupid",
    "Fantastic support from team",
    "Idiot developers ruined the app",
    "Smooth and clean interface",
    "Awful and disgusting service",
    "Very happy with this product"
]

df = pd.DataFrame({
    "Comment": comments
})

# -----------------------------
# TOXIC WORD DICTIONARY
# -----------------------------
toxic_words = {
    "stupid": 2,
    "useless": 2,
    "idiot": 3,
    "trash": 2,
    "horrible": 2,
    "awful": 2,
    "disgusting": 3,
    "hate": 2,
    "worst": 2
}

# -----------------------------
# TOXICITY ANALYSIS FUNCTIONS
# -----------------------------
def analyze_toxicity(text):
    
    words = re.findall(r'\b\w+\b', text.lower())
    
    score = 0
    abusive_terms = []
    
    for word in words:
        if word in toxic_words:
            score += toxic_words[word]
            abusive_terms.append(word)
    
    label = "Toxic" if score > 0 else "Non-Toxic"
    
    return pd.Series([label, score, abusive_terms])

# -----------------------------
# PROCESS COMMENTS
# -----------------------------
df[["Toxicity", "Severity Score", "Abusive Terms"]] = df["Comment"].apply(
    analyze_toxicity
)

# -----------------------------
# DASHBOARD METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Comments", len(df))
col2.metric("Toxic Comments", (df["Toxicity"] == "Toxic").sum())
col3.metric("Average Toxicity Score", round(df["Severity Score"].mean(), 2))

# -----------------------------
# TOXICITY DISTRIBUTION
# -----------------------------
toxicity_counts = df["Toxicity"].value_counts()

fig1 = px.pie(
    values=toxicity_counts.values,
    names=toxicity_counts.index,
    title="Toxic vs Non-Toxic Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# SEVERITY SCORE DISTRIBUTION
# -----------------------------
fig2 = px.histogram(
    df,
    x="Severity Score",
    nbins=10,
    title="Toxicity Severity Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# ABUSIVE TERM FREQUENCY
# -----------------------------
all_terms = []

for terms in df["Abusive Terms"]:
    all_terms.extend(terms)

term_counts = Counter(all_terms)

if term_counts:
    
    term_df = pd.DataFrame(
        term_counts.items(),
        columns=["Abusive Term", "Frequency"]
    ).sort_values(
        by="Frequency",
        ascending=False
    )

    fig3 = px.bar(
        term_df,
        x="Abusive Term",
        y="Frequency",
        title="Most Frequent Abusive Terms"
    )

    st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# TOXIC COMMENTS TABLE
# -----------------------------
st.subheader("⚠ Flagged Toxic Comments")

st.dataframe(
    df[df["Toxicity"] == "Toxic"]
)

# -----------------------------
# FULL DATA TABLE
# -----------------------------
st.subheader("📄 Full Toxicity Analysis")

st.dataframe(df)
