from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage
import json
import os

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key='********************************************************')

username=input('Enter your username: ')
memory_save=f"{username}.json"

history=[]

if os.path.exists(memory_save):
    with open(memory_save,'r') as file:
        data=json.load(file)
        for memory in data:

            if memory['role']=="Human":
                history.append(HumanMessage(content=memory['content']))
            else:
                history.append(AIMessage(content=memory['content']))

        print(f" Welcome Back {username} How I Can Help You Today ")

print(" Type Here to Exit or Quit ")

while True:
    query=input (" You : ")
    if query.lower().strip()=="exit":
        break

    history.append(HumanMessage(content=query))
    print("===========================================================================================================================================================================================================")
    response=llm.invoke(history)

    history.append(AIMessage(content=response.content))
    print(" AI : ",response.content)

history.append(HumanMessage(content="user execute a exit then you will summarize the conversation between Human and AI to generate Summary"))
response1=llm.invoke(history)
history.append(AIMessage(content=response1.content))
print(" AI : ",response1.content)

data=[]
for msg in history:
    data.append({
        "role":msg.type,
        "content":msg.content
    })

with open(memory_save,'w') as file:
    json.dump(data,file,indent=5)
    print(" JSON FILE SAVED SUCCESSFULLY ")



