import nltk
nltk.download('popular')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import pickle
import numpy as np

from keras.models import load_model
model = load_model('model.h5')
import json
import random

intents = json.loads(open('datap.json').read())
words = pickle.load(open('texts.pkl','rb'))
classes = pickle.load(open('labels.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intents": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json, company_data):
    tag = ints[0]['intents']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            if tag == 'company_info':
                response = i['responses'][0]
                response = response.replace("[company]", company_data['name'])
                response = response.replace("[description]", company_data['description'])
                response = response.replace("[location]", company_data['location'])
                response = response.replace("[contactNumber]", company_data['contactNumber'])
                response = response.replace("[website]", company_data['website'])
            elif tag == 'services':
                response = i['responses'][0]
                response = response.replace("[company]", company_data['name'])
                response = response.replace("[services]", ', '.join(company_data['services']))
                response = response.replace("[specialization]", company_data['specialization'])
            else:
                response = random.choice(i['responses'])
            break
    else:
        response = "I'm sorry, I don't have information about that topic."
    return response

def chatbot_response(msg, intents_json, company_name):
    ints = predict_class(msg, model)
    company_data = None
    if company_name:
        for company in intents_json['companies']:
            if company['name'].lower() == company_name.lower():
                company_data = company
                break
    print(f"Input Message:",msg)
    print(f"Company Name: ",company_name)
    print(f"Matched Company Data: ",company_data)

    if company_data:
        response = getResponse(ints, intents_json, company_data)
    else:
        response = "I'm sorry, I don't have information about that company."

    print(f"Bot Response: ",response)
    return response


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    company_name = request.args.get('company')
    return chatbot_response(userText, intents, company_name)


if __name__ == "__main__":
    app.run()
