import streamlit as st
import openai
def gpt3(stext):
    response = openai.Completion.create(
      engine="text-curie-001",
      prompt=stext,
      temperature=0.7,
      max_tokens=512,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    content = response.choices[0]["text"]
    return content

def generate(char1, char2, nsfw):
    openai.api_key = "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"
    print(str(nsfw))
    if str(nsfw) == "True":
        response = gpt3("Write a nsfw fanfiction for " + char1 + " and  " + char2)
    else:
        response = gpt3("Write a fanfiction for " + char1 + " and  " + char2)

    return response

st.title("Fanfiction writer")
text = st.text_area("Enter character 1: ", value='', height=50, max_chars=None, key=None)
text2 = st.text_area("Enter character 2: ", value='', height=50, max_chars=None, key=None)
agree = st.checkbox('NSFW?')

if st.button('Generate fanfiction'):
    if text == '' or text2 == '':
        st.write("Enter characters bitch")
    else:
        res = generate(text, text2, agree)
        st.markdown(res)
else:
    pass

