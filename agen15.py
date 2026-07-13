import os
import requests
import json

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage,AIMessage

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key='*******************************')

history=[]

if os.path.exists('umesh.json'):
    with open('umesh.json','r') as f:
        data=json.load(f)
        for msg in data:
            if msg['role']=="human":
                history.append(HumanMessage(content=msg['content']))
            else:
                history.append(AIMessage(content=msg['content']))

print(" 1. History ")
print(" 2. Search Conversation ")
print(" 3. Weather ")
print(" 4. Exit ")

summary=""
if os.path.exists('summary1.txt'):
    with open('summary1.txt','r') as f:
        summary=f.read()
        print("\n ================================================================================ \n ")
        print(summary)


def get_weather(city):
    url=f"http://api.weatherapi.com/v1/current.json?key=b6e147f4fd904599be051348262706&q={city}&aqi=no"
    response=requests.get(url)
    return response.text

def weather_assisstant(city):
    weather=get_weather(city)
    prompt=(f"""Weather Information : {weather}
    Explain the Weather Information and
    Suggest Outdoor Activities and Wearing Clothes""")
    response=llm.invoke(prompt)
    return response.content


print(" Type here to Exit or Quit")

while True:
    query = input(" You : ")
    if query.lower().strip()=="exit":
        break

    if query.lower().strip()=="history":
        history=weather_assisstant(city=query)
        for msg in history:
            if msg.type=="human":
                print(" Human : ",msg.content)
            else:
                print(" AI : ",msg.content)
        continue

    if query.lower().startswith("search"):
        keyword=query[7:].lower()
        print(f" Search : {keyword}")
        found=False
        for msg in history:
            if keyword in msg.content.lower():
                found=True
                if msg.type=="human":
                    print(" Human ",msg.content)
                else:
                    print(" AI ",msg.content)

                print()

        if not found:
            print(" No Matching Found ")
            continue

    if query.lower()=="Weather Search":
        for msg in history:
            if msg['role']=="human":
                print(" Human : ",msg.content)
            else:
                print(" AI : ",msg.content)



    history.append(HumanMessage(content=query))
    response=llm.invoke(history)

    history.append(AIMessage(content=response.content))
    print(" AI ",response.content)

data=[]
for msg in history:
    data.append({
        "role":msg.type,
        "content":msg.content
    })

with open("umesh.json","w") as f:
    json.dump(data,f)
    print(" JSON FILE SAVED SUCCESSFULLY")


conversation=""
for msg in history:
    if msg.type=="human":
        conversation+=f" Human : {msg.content} \n"
    else:
        conversation+=f" AI : {msg.content} \n"


summary_prompt=f""" You are the AI Assistant Summarize the Following Conversation Includes
{conversation}"""
summary_response=llm.invoke(summary_prompt)
summary=summary_response.content

with open('summary1.txt','w') as f:
    f.write(summary)

print("Summary File Created")
