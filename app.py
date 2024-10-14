"""
Copyright @Abu Huzaifah Bidin
Streamlit app untuk Penghasil Pantun 
menggunakan finetune model dari GPT-4o

"""

#muat turun library
import openai
import streamlit as st
from dotenv import load_dotenv
import os
import re
from PIL import Image

# muat turun environment variable sebab kita gunapakai benda tu untuk simpan API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# mari setup streamlit dahulu
st.title("Penghasil Pantun Melayu")

# Add scaled image
image = Image.open("melayu.png")  # Replace with your image path
image = image.resize((int(image.width * 0.5), int(image.height * 0.5)))
st.image(image, caption='Pantun Generator')  # Set the width to scale the image
st.write("Ini adalah prototaip awal penghasil pantun Melayu. Di hasilkan melalui kumpulan 3000 pantun yang dikumpul oleh Abu Huzaifah yang kacak. Pantun ini akhirnya melalui proses finetuning dengan menggunakan model GPT-4o yang telah mengopakkan duit Abu Huzaifah yang kacak!")

# prompt untuk user
prompt = st.text_input("Sila masukkan baris pertama pantun:")

# letakkan nilai awal untuk session state
if 'regeneration_count' not in st.session_state:
    st.session_state.regeneration_count = 0
if 'generated_pantun' not in st.session_state:
    st.session_state.generated_pantun = None

# fungsi menghasilkan pantun dari model yang telah difinetune
def generate_pantun(prompt, model="ft:gpt-4o-2024-08-06:personal:pantun-gen:AI6u8GDU", temperature=1, max_tokens=150):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Pantunbot is a pantun generator able to continue a pantun given a pantun line. A pantun typically consists of four lines where the end of the first line rhymes with the end of the third line, and the end of the second line rhymes with the end of the fourth line. The lines should have a rhythmic flow and convey a meaningful message."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    pantun = response['choices'][0]['message']['content'].strip()
    # susun baik2 response yang sudah diterima
    lines = re.split(r'(?<=[.,;!?])\s+', pantun)
    lines = [re.sub(r'[.;,!?]$', '', line.strip()) for line in lines] 
    if len(lines) < 3:
        raise ValueError("The generated response did not contain enough lines to form a complete pantun.")
    return [prompt] + lines[:3]
# penghasilan pantun
if prompt:
    if st.button('Hasilkan Pantun') or (st.session_state.generated_pantun is None):
        with st.spinner('Pantun sedang dikarang...'):
            try:
                st.session_state.generated_pantun = generate_pantun(prompt)
                st.session_state.regeneration_count = 1
                st.success("Ini hasil pantun yang sedara pinta:")
            except Exception as e:
                st.error(f"Adeh silap pulak: {str(e)}")
    elif st.button('Hasilkan semula pantun') and st.session_state.regeneration_count < 10:
        with st.spinner('Pantun sedang dikarang semula..'):
            try:
                st.session_state.generated_pantun = generate_pantun(prompt)
                st.session_state.regeneration_count += 1
                st.success("Ini pantun yang dikarang semula atas permintaan sedara:")
            except Exception as e:
                st.error(f"Adeh silap pulak: {str(e)}")
    # susun pantun baris demi baris
    if st.session_state.generated_pantun:
        st.write(st.session_state.generated_pantun[0].capitalize() + ',')  # User's prompt
        st.write(st.session_state.generated_pantun[1].capitalize() + ',')  # First generated line
        st.write(st.session_state.generated_pantun[2].capitalize() + ',')  # Second generated line
        st.write(st.session_state.generated_pantun[3].capitalize() + ',')  # Third generated line

    # reset semula pantun selepas 10 kali sesi 
    if st.session_state.regeneration_count >= 10:
        st.session_state.generated_pantun = None
        st.session_state.regeneration_count = 0