# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 09:48:54 2026

@author: Oreoluwa
"""

from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

from services.groq_llm import simplify_text
from services.image_gen import generate_image
from services.tts import text_to_speech
from utils.text_utils import split_sentences

st.set_page_config(layout="wide")

# =========================================================
# SESSION STATE INITIALIZATION (COST PROTECTION)
# =========================================================

if "sentences" not in st.session_state:
    st.session_state.sentences = []

if "index" not in st.session_state:
    st.session_state.index = 0

if "image_url" not in st.session_state:
    st.session_state.image_url = None

if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None

if "last_sentence" not in st.session_state:
    st.session_state.last_sentence = ""

# =========================================================
# UI
# =========================================================

st.title("📘 AI Powered Learning Assistant for Dyslexic Students")


user_text = st.text_area(
    "Enter learning text or a situation",
    height=200
)

# =========================================================
# TEXT SIMPLIFICATION
# =========================================================

if st.button("Generate Learning View"):
    with st.spinner("Simplifying text..."):
        simplified = simplify_text(user_text)
        sentences = split_sentences(simplified)

    st.session_state.sentences = sentences
    st.session_state.index = 0

    # Reset cached multimodal outputs
    st.session_state.image_url = None
    st.session_state.audio_bytes = None
    st.session_state.last_sentence = ""

# =========================================================
# MAIN CONTENT
# =========================================================

if st.session_state.sentences:
    idx = st.session_state.index
    sentence = st.session_state.sentences[idx]

    # =====================================================
    # GENERATE IMAGE + AUDIO ONCE PER SENTENCE
    # =====================================================

    if sentence != st.session_state.last_sentence:
        with st.spinner("Generating learning content..."):
            st.session_state.image_url = generate_image(sentence)
            st.session_state.audio_bytes = text_to_speech(sentence)
            st.session_state.last_sentence = sentence

    col1, col2 = st.columns([1, 1])

    # ---------------- LEFT: TEXT + AUDIO -----------------
    with col1:
        st.markdown(
            f"<div style='font-size:22px; line-height:1.6'>{sentence}</div>",
            unsafe_allow_html=True
        )

        # Auto-play when content loads
        if st.session_state.audio_bytes:
            st.audio(
                st.session_state.audio_bytes,
                format="audio/mp3",
                autoplay=True
            )

        # Manual replay (NO image regeneration)
        if st.button("🔊 Read Aloud"):
            st.audio(
                st.session_state.audio_bytes,
                format="audio/mp3",
                autoplay=True
            )

    # ---------------- RIGHT: IMAGE -----------------
    with col2:
        if st.session_state.image_url:
            st.image(st.session_state.image_url)

    # =====================================================
    # NAVIGATION
    # =====================================================

    nav1, nav2 = st.columns(2)

    if nav1.button("⬅ Previous") and idx > 0:
        st.session_state.index -= 1

    if nav2.button("Next ➡") and idx < len(st.session_state.sentences) - 1:
        st.session_state.index += 1
