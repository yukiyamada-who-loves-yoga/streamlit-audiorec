import streamlit as st
from st_audiorec import st_audiorec
from datetime import datetime

st.set_page_config(
    page_title="録音(st-audiorec)",
    page_icon="🎤",
)

st.title("🎤 録音")
st.write("ライブラリ：https://pypi.org/project/streamlit-audiorec/")
st.write("GitHub：https://github.com/yukiyamada-who-loves-yoga/streamlit-audiorec")

wav_audio_data = st_audiorec()

# 以下は、手動で音声ダウンロードする場合の参考コード
# if wav_audio_data is not None:
#     st.audio(wav_audio_data, format='audio/wav')
        
#     st.download_button(
#         label="ダウンロード",
#         data=wav_audio_data,
#         file_name=f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav",
#         mime="audio/wav"
#     )