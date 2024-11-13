import google.generativeai as genai
genai.configure(api_key="AIzaSyB4OdTs0k7mEFZR3oI7G4-4zxFsPGqzLLw")
model = genai.GenerativeModel("gemini-1.5-flash")
system_prompt="Answer as a fun easy going female fashion designer who will help in finding good dress to wear or if someone wants to buy for someone first ask them out the events and suggest good dress combo if the want wear two pieces or dress or ethnic wear, if they give body type suggest dress accordingly, and suggest good color combo, and if they want a dress then give them good neck line or length and tell them what they can wear and look good in"
def chat_with_bot(user_input):
  prompt=system_prompt+user_input
  response=model.generate_content(prompt)
  return response.text
if __name__=="__main__":
  while True:
    print("Hi I am a fashion chatbot \n I will suggest you a good dress to impress ")
    user_input=input("You ")
    if user_input.lower()=="exit":
      print("Chatbot: Goodbye\n have a great day :)")
      break
    response=chat_with_bot(user_input)
    print("Chatbot:",response)
