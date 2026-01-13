import google.generativeai as genai

genai.configure(api_key="AIzaSyAgSyrrUBEAue-ynNeanuZjIcF6Y7IF1Gw")
for m in genai.list_models():
    print(m.name)