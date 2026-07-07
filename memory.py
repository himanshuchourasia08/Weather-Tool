from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key='********')

history=InMemoryChatMessageHistory()

print("Type 'exit', to quit. \n")
while True:
    query=input(" Your: ")
    if query.lower()=="exit":
        break

    history.add_message(HumanMessage(query))

    response=llm.invoke(history.messages)

    history.add_message(AIMessage(content=response.content))

    print("Ai Messages",response.content)

for i,msg in enumerate(history.messages,start=1):
    print(f"{i}.{msg.type.upper()}: {msg.content}")
