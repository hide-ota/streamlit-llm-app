import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7
)

st.title("映画・音楽の専門家に質問しよう")
st.write("このアプリでは、映画や音楽の専門家に質問することができます。")
st.write("ジャンルを選び、質問を入力してください。")

genre = st.radio("ジャンルを選んでください", ["映画", "音楽"])
question = st.text_input("質問を入力してください")

if st.button("実行"):
    if not question:
        st.error("質問を入力してください。")
    else:
        system_template = "あなたは、{genre}に詳しいAIです。ユーザーからの質問に回答してください。"
        human_template = "{question}"
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template(human_template),
        ])

        messages = prompt.format_prompt(genre=genre, question=question).to_messages()
        response = llm(messages)
        st.write("### 回答")
        st.write(response.content)
