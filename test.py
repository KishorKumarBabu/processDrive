import google.generativeai as genai
from PIL import Image #PIL-Python Imaging Library
import os
model=genai.GenerativeModel('gemini-1.5-flash')# mentioning the model of genarative ai
os.environ['API_KEY']="AIzaSyA0QQMux7zHqX9XsLCOZI-Q-zmcANMtWIo"

api_key = os.environ['API_KEY']# seting the api key in environment

genai.configure(api_key=api_key)# verify the api key 
def prompt():
    try:
        a ="Describe this image" # input
        images=input("Enter the image file name:")
        img=Image.open(images)# input
        response=model.generate_content([a, img],stream=True)# in its line it generate the content 
        response.resolve()
        return response
    except Exception as e:
        print("The error is ",e)

if __name__=="__main__":
    result=prompt()
    print(result.text) # return the result in text formate