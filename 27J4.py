from langchain_google_genai import ChatGoogleGenerativeAI
import requests

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key="****************************")


def get_weather(city):
    url=(f"http://api.weatherapi.com/v1/current.json?key=b6e147f4fd904599be051348262706&q={city}&aqi=no")
    response = requests.get(url)
    return response.text

def weather_assistant(city):
    weather=get_weather(city)
    prompt=f"""
    Weather Information :{weather}
    Explain the Weather Information and
    Suggest Outdoor Wearing and Activities"""
    response=llm.invoke(prompt)
    return response.content


while True:
    city = input("Enter the city you are looking for: ")
    if city.lower()=="exit":
        break
    print(weather_assistant(city))
