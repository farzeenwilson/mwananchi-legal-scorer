# The Language of Law vs. The Common Mwananchi

Assessing and Addressing the Accessibility Gap in Kenya’s Constitution

## Project Overview
Following the 2024 Finance Bill protests in Kenya, it became clear that a significant gap exists between legal frameworks and citizen understanding. This project uses Natural Language Processing (NLP) to quantify the "Accessibility Gap" in the Constitution of Kenya (2010).

Our research proves that while the "Bill of Rights" is written for the people, the "Public Finance" chapters are linguistically dense, requiring post-graduate level literacy to interpret. This repository contains both the Exploratory Data Analysis (EDA) and a deployed Deep Learning Dashboard to help citizens decode complex legal jargon.

## The Solution: Mwananchi Legal Readability Scorer
The deployed application allows users to:
- Analyze: Paste any legal clause (Constitution, Finance Bill, or Acts of Parliament).
- Score: Get an instant "Jargon Probability" score using a Facebook BART Zero-Shot Classification model.
- Decode: Automatically highlight multisyllabic jargon that contributes to cognitive overload.

## Tech Stack
- Language: Python 3.12
- Analysis: Pandas, Regex, NLTK (Readability Metrics)
- Machine Learning: Hugging Face Transformers (bart-large-mnli)
- Visualization: Plotly, Seaborn, WordCloud
- Deployment: Streamlit Community Cloud

## Repository Structure
app.py: The main Streamlit application script.

requirements.txt: List of Python dependencies for cloud deployment.

The_Language_of_Law.ipynb: The complete data science notebook containing the Chapter ranking, Readability scoring, and EDA.

The_Constitution_of_Kenya_2010.pdf: The source dataset.

## Key Findings from EDA
Chapter 12 (Public Finance) ranks in the top quartile of difficulty, often requiring 16+ years of formal education to comprehend.

Chapter 4 (The Bill of Rights) is the most accessible, designed with simpler sentence structures and higher sentiment clarity.

There is a direct correlation between Average Sentence Length and the lack of civic understanding among the "Common Mwananchi."
