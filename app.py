import streamlit as st
from st_audiorec import st_audiorec
from datetime import datetime

st.set_page_config(
    page_title="録音(st-audiorec)",
    page_icon="🎤",
)

st.title("🎤 録音")

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
    
    filename = f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    
    st.download_button(
        label="ダウンロード",
        data=wav_audio_data,
        file_name=filename,
        mime="audio/wav"
    )