### This App will be able to take the URL of Youtube/Website and get the data and give you summary.

import validators, streamlit as st
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain

## Let's create streamlit app
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

## Get the Groq API Key and url(YT or website)to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Enter the GROQ API Key", value="", type="password")


generic_url = st.text_input("URL", label_visibility="collapsed")


## Gemma model using Groq API
llm = ChatGroq(groq_api_key=groq_api_key, model="Gemma-7b-It")


## Prompt Template
prompt_template = """ 
Provide a summary of the following content in 300 words:
Content: {text}
"""
## Prompt
prompt = PromptTemplate(
    input_variables=['text'],
    template= prompt_template
)


## Let's create a button - Summarize
if st.button("Summarize"):
    ## Let's validate the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be something YT URL or Website URL")
    else:
        try:
            with st.spinner("Waiting.."):
                ## Load YT or Website URL
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(urls=[generic_url], ssl_verify=False, 
                                                   headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                
                docs = loader.load()

                ## Chain for Summarization
                chain = load_summarize_chain(llm=llm, chain_type="stuff", prompt=prompt)
                output_sumamry = chain.run(docs)

                st.success(output_sumamry)
        
        except Exception as e:
            st.exception(f"Exception:{e}")
            

