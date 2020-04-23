import joblib
import praw
import json 
import re
import sklearn
from praw.models import MoreComments
from nltk.corpus import stopwords 
import os

dir_ = os.getcwd()

config_file =dir_+"\\flairdetector\\config.json"

model_file = dir_+"\\flairdetector\\predictorfiles\\finalmodel.sav"
preprocessor_file = dir_+"\\flairdetector\\predictorfiles\\preprocessor.sav"

with open(config_file) as f:
    config = json.load(f)

preprocessor = joblib.load(preprocessor_file)
ml_model = joblib.load(model_file)

reddit = praw.Reddit(client_id = config['client_id'],
                     client_secret = config['client_secret'],
                     user_agent = config['user_agent'],
                     username = config['user_name'],
                     password = config['password'],)

stopwords = set(stopwords.words('english'))

labeltoflair = {
    0: 'AskIndia',
    1: 'Non-Political', 
    2:'Scheduled', 
    3: 'Photography', 
    4: 'Coronavirus',
    5: 'Science/Technology', 
    6: 'Politics', 
    7: 'Business/Finance',
    8: 'Policy/Economy',
    9: 'Sports',
   10: 'Food'
}

def cleanText(text):
    text = re.sub('[0-9]','',text)
    text = re.sub(r"http\S+", " ", text)
    result = re.sub('[^A-Za-z0-9]+', ' ', text)
    result = result.lower()
    return result

def makePredictions(url,ml_model,preprocessor,reddit,stopwords,labeltoflair):
    spl = 'https://www.reddit.com/r/india/comments/' 

    
    x = url.split(spl)[1]
    x_ = x.split('/')[0]

    subred = reddit.submission(id=x_)
    title = cleanText(subred.title)
    body = cleanText(subred.selftext)

    comment = ''
    for top_level_comment in subred.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        comment = comment + ' ' + top_level_comment.body
    comments = cleanText(comment)
    
    combined = ''+ title + body + comments

    combined = ' '.join(word for word in combined.split() if word not in stopwords)
    combined = [combined]
    preprocessed = preprocessor.transform(combined).toarray()
    predictions = ml_model.predict(preprocessed)
    print(predictions[0])
    return labeltoflair[predictions[0]]
    
    





