import streamlit as st
import openai
def gpt3(stext):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=stext,
      temperature=0.7,
      max_tokens=2000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    content = response.choices[0]["text"]
    return content

def generate(char1, char2, nsfw):
    openai.api_key = st.secrets["apikey"]
    print(str(nsfw))
    if str(nsfw) == "True":
        response = gpt3("Write a nsfw fanfiction novel with " + char1 + " and  " + char2)
    else:
        response = gpt3("Write a fanfiction novel with " + char1 + " and  " + char2)

    return response

st.title("Fanfiction writer")
text = st.text_area("Enter character 1: ", value='', height=10, max_chars=None, key=None)
text2 = st.text_area("Enter character 2: ", value='', height=10, max_chars=None, key=None)
agree = st.checkbox('NSFW?')

if st.button('Generate fanfiction'):
    if text == '' or text2 == '':
        st.write("Enter characters bitch")
    else:
        res = generate(text, text2, agree)
        st.markdown(res)
else:
    pass


