import requests
import json
import pandas as pd
from transformers import pipeline
from textblob import TextBlob
from langdetect import detect
from googletrans import Translator

def detect_language_and_translate_to_english(text):
    translator = Translator()
    try:
        detected_language = detect(text)
        
        if detected_language != 'en':
            translated_text = translator.translate(text, src=detected_language, dest='en')
            return translated_text.text, detected_language
        else:
            return text, detected_language
    except:
        return "",""


# Define the URL
def sent(x):
    url = "http://52.20.167.25:5001/analyze_sentiment"

    # Define the JSON object
    json_data = {"text":x}

    # Define headers with content type as JSON
    headers = {"Content-Type": "application/json"}

    # Send the request
    try:
        response = requests.get(url, data=json.dumps(json_data), headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Print the response content
            print(response.json())
            return response.json()
        else:
            print("Error:", response.status_code)

    except:
        pass

def sentimenter(text):
    
    pipe = pipeline('sentiment-analysis')
    # st.title("Sentiment Analysis")

    # st.subheader("Which framework would you like to use for sentiment analysis?")
    # option = st.selectbox('Choose Framework:',('Transformers', 'TextBlob')) # option is stored in this variable

    # st.subheader("Enter the text you want to analyze")
    # text = st.text_input('Enter text:') # text is stored in this variable
    option = 'Transformers'
    if option == 'Transformers':
        try:
            out = pipe(text)
        except:
            out ={}
            pass
    else:
        out = TextBlob(text)
        out = out.sentiment
    print(out) 
    return out 
    # st.write("Sentiment of Text: ")
    # st.write(out)

def process_excel(filename):
    # Read the Excel file
    xls = pd.ExcelFile(filename)
    
    # Process each sheet
    for sheet_name in xls.sheet_names[3:]:
        # Read the sheet into a DataFrame
        df = pd.read_excel(filename, sheet_name=sheet_name, usecols='R, S')
        
        # Create a new DataFrame to store processed data
        processed_df = pd.DataFrame(columns=['R', 'S'])
        
        # Traverse each row
        for index, row in df.iterrows():
            # Get the value from column R
            value = row[0]
            
            # Call the API
            value,detected = detect_language_and_translate_to_english(value)
            api_result = sentimenter(value)
            
            # Store the result in column S
            processed_df = processed_df.append({'R': value, 'S': api_result}, ignore_index=True)
            print(processed_df)
        # Save the updated DataFrame to a new Excel file with sheet name
        new_filename = f"{sheet_name}_processed_again.xlsx"
        processed_df.to_excel(new_filename, index=False)


# Usage
filename = 'xx.xlsx'
process_excel(filename)