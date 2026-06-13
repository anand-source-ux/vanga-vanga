import streamlit as st
import requests
from datetime import datetime

# -----------------------
# CONFIG
# -----------------------
API_KEY = "pub_3c52ff1f0d5841cc978fe39d8a8f6972"
BASE_URL = "https://newsdata.io/api/1/news"

st.set_page_config(
    page_title="News Explorer",
    page_icon="📰",
    layout="wide"
)

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("📰 News Explorer")

countries = {
    "India": "in",
    "United States": "us",
    "United Kingdom": "gb",
    "Australia": "au",
    "Canada": "ca",
    "Germany": "de",
    "France": "fr",
    "Japan": "jp"
}

country = st.sidebar.selectbox(
    "Select Country",
    list(countries.keys())
)

keyword = st.sidebar.text_input(
    "Search Keyword",
    placeholder="AI, Cricket, Tesla..."
)

article_count = st.sidebar.slider(
    "Number of Articles",
    min_value=5,
    max_value=50,
    value=10
)

# -----------------------
# TITLE
# -----------------------
st.title("🌍 Advanced News Explorer")
st.markdown(
    "Get the latest headlines from around the world."
)

# -----------------------
# FETCH NEWS
# -----------------------
params = {
    "apikey": API_KEY,
    "country": countries[country],
    "language": "en"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:

    data = response.json()

    articles = data.get("results", [])

    # Keyword Filter
    if keyword:
        articles = [
            article for article in articles
            if keyword.lower() in (
                (article.get("title") or "") +
                (article.get("description") or "")
            ).lower()
        ]

    articles = articles[:article_count]

    st.success(f"Found {len(articles)} articles")

    if not articles:
        st.warning("No matching articles found.")

    for article in articles:

        with st.container():

            col1, col2 = st.columns([1, 2])

            with col1:
                if article.get("image_url"):
                    st.image(
                        article["image_url"],
                        use_container_width=True
                    )

            with col2:

                st.subheader(
                    article.get("title", "No Title")
                )

                source = arti