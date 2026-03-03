import streamlit as st
from transformers import pipeline
import plotly.graph_objects as go
import re

# setting up page for Legal Translator
st.set_page_config(page_title="Mwananchi Legal Translator", layout="wide")

# We use @st.cache_resource so the large ML model only loads once
@st.cache_resource
def load_model():
    # Loading a pre-trained Zero-Shot classification model from Hugging Face
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

classifier = load_model()

def count_syllables(word):
    """Simple heuristic to count syllables for highlighting."""
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if len(word) == 0: return 0
    if word[0] in vowels: count += 1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i - 1] not in vowels:
            count += 1
    if word.endswith("e"): count -= 1
    if count == 0: count += 1
    return count

def highlight_jargon(text):
    """Finds complex words (>3 syllables) and highlights them in red."""
    words = text.split()
    highlighted_text = []
    jargon_count = 0
    
    for word in words:
        clean_word = re.sub(r'[^\w\s]', '', word) # removing punctuation
        if count_syllables(clean_word) >= 3:
            # wrapping complex words highlight them
            highlighted_text.append(f"<mark style='background-color: #ffcccc; color: red;'><b>{word}</b></mark>")
            jargon_count += 1
        else:
            highlighted_text.append(word)
            
    return " ".join(highlighted_text), jargon_count

def create_gauge_chart(score):
    """Creates a Plotly chart for the accessibility score."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Jargon Probability", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 33], 'color': "lightgreen"},
                {'range': [33, 66], 'color': "gold"},
                {'range': [66, 100], 'color': "salmon"}],
        }
    ))
    return fig

# creating dashboard
st.title("⚖️ The Mwananchi Legal Readability Scorer")
st.markdown("Enter an Article from the Constitution or a proposed Bill to test its linguistic accessibility.")

# text box for input
user_text = st.text_area("Paste Legal Text Here:", height=150, 
                         value="The Consolidated Fund shall be appropriated by an Act of Parliament for the remuneration and equalisation of devolved county mechanisms.")

if st.button("Analyze Accessibility"):
    with st.spinner("Running Deep Learning NLP Analysis..."):
        
        # run the Hugging Face Zero-Shot Model and confirm if plain or complex english
        labels = ["accessible plain English", "complex legal jargon"]
        result = classifier(user_text, candidate_labels=labels)
        
        # probability score of complex jargon
        jargon_index = result['labels'].index("complex legal jargon")
        jargon_score = result['scores'][jargon_index]
        
        highlighted_html, jargon_count = highlight_jargon(user_text)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Deep Learning Assessment")
            st.plotly_chart(create_gauge_chart(jargon_score), use_container_width=True)
            
            if jargon_score > 0.6:
                st.error("🚨 **High Complexity:** This text is highly inaccessible to the average citizen.")
            else:
                st.success("✅ **Accessible:** This text is written in plain, understandable language.")
                
        with col2:
            st.subheader("Lexical Breakdown")
            st.markdown(f"**Potential Jargon Words Detected:** {jargon_count}")
            st.markdown("The words highlighted below have 3 or more syllables and may cause cognitive overload for a layperson:")
            
            st.markdown(f"<div style='padding:15px; border:1px solid #ddd; border-radius:5px;'>{highlighted_html}</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("*Built for DSA 8501: Text & Unstructured Data Analytics*")
