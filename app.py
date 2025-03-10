import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
##  Function to get response from LLAma 2 model
def getLLamaresponse(input_text,no_words,blog_style):
     ##llama model
     llm=CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                       model_type='llama',
                       config={'max_new_tokens':256,
                               'temperature':0.01})
     ##prompt template
     template="""
    Write a blog for {blog_style} job profile for a topic {input_text}
    within{no_words} words.

              """
     prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                             template=template)
     ##generate the response from the LLama 2 model
     response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
     print(response)
     return response

    





st.set_page_config(page_title="Blogs Generator",
                   page_icon='📜',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Blogs Generator 📜")
input_text=st.text_input("Enter the Blog Topic")
## creating coloums for additonal 2 fields
col1,col2=st.columns([5,5])
with col1:
    no_words = st.text_input('no of words')
with col2:
    blog_style = st.selectbox('writing this blog for',('Researchers','Data Scientist','Common people'),index=0)
submit=st.button("Generate")
##final response
if submit:
      st.write(getLLamaresponse(input_text,no_words,blog_style)) 