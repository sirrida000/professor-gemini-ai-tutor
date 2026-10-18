from google import genai
import streamlit as st

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
model = "gemini-3.5-flash"
userrole = "user"

pre_prompt = "Teach me the following concept: "
response = ""

st.title("My Gemini Chat App")
st.divider()
prompt = st.text_input("What do you want to learn?")
genaibutton = st.button("Teach me")
st.caption("ProfessorGEMINI will work when you press the button.")
st.divider()

if genaibutton:
    with st.spinner("I am preparing your lecture"):
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[{"role": userrole, "parts": [{"text": pre_prompt + prompt}]}],
        )
    st.snow()
    st.write(response.text)
