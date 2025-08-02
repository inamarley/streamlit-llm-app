from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

import streamlit as st
st.title("chapter6: 提出課題")

st.write("##### 動作モード1: 旦那さんのお弁当作りの専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、旦那さんのお弁当の提案を行います。")
st.write("##### 動作モード2: おつまみ作りの専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、おつまみの提案を行います。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["旦那さんのお弁当作り", "おつまみ作り"]
)

st.divider()

input_message = st.text_input(label="提案のためのテキストを入力してください。")

if st.button("実行"):
    if input_message:
        with st.spinner("提案を生成中..."):
            if selected_item == "旦那さんのお弁当作り":
                system_message = SystemMessage(content="あなたは旦那さんのお弁当作りの専門家です。栄養バランスが良く、見た目も美味しそうで、忙しい朝でも作りやすいお弁当のレシピを提案してください。")
                human_message = HumanMessage(content=input_message)
                
                messages = [system_message, human_message]
                response = llm.invoke(messages)
                
                st.write("**旦那さんのお弁当の提案:**")
                st.write(response.content)
                
            elif selected_item == "おつまみ作り":
                system_message = SystemMessage(content="あなたはおつまみ作りの専門家です。お酒に合う美味しいおつまみのレシピを提案してください。簡単に作れて、お酒がすすむようなものを心がけてください。")
                human_message = HumanMessage(content=input_message)
                
                messages = [system_message, human_message]
                response = llm.invoke(messages)
                
                st.write("**おつまみの提案:**")
                st.write(response.content)
    else:
        st.warning("提案のためのテキストを入力してください。")
