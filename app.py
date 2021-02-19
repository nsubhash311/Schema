from flask import request, jsonify, Flask, render_template
import flask
import string
from collections import Counter
import matplotlib.pyplot as plt
import json
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import shutil
# from .sentiment import setimentanalysis
app = Flask(__name__, static_url_path='/static')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/shop', methods=['GET', 'POST'])
def shop():
    return render_template('shop.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    return render_template('checkout.html')


@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    return render_template('confirmation.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/productdetails', methods=['GET', 'POST'])
def product_details():
    var1=''
    var2=''
    var3=''

    if flask.request.method == 'POST':
        text = request.form['comments']
        print(text)
        lower_case = text.lower()
        cleaned_text = lower_case.translate(
            str.maketrans('', '', string.punctuation))

        # Using word_tokenize because it's faster than split()
        tokenized_words = word_tokenize(cleaned_text, "english")

        # Removing Stop Words x
        final_words = []
        for word in tokenized_words:
            if word not in stopwords.words('english'):
                final_words.append(word)

        # Lemmatization - From plural to singlular + Base form of a word (example better-> good)
        lemma_words = []
        for word in final_words:
            word = WordNetLemmatizer().lemmatize(word)
            lemma_words.append(word)

        # emotion_list = []
        # with open('emotions.txt', 'r') as file:
        #     for line in file:
        #         clear_line = line.replace("\n", '').replace(
        #             ",", '').replace("'", '').strip()
        #         word, emotion = clear_line.split(':')

        #         if word in lemma_words:
        #             emotion_list.append(emotion)

        # w = Counter(emotion_list)

        # find score of the comment
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        print(score)
        score.pop('compound', None)
        print(score)
        var1=score['neg']
        var2=score['pos']
        var3=score['neu']
        print(var1)
        print(var2)
        print(var3)
        # Sc=abs(score['compound'])
        # print(Sc)
        type_of_sentiment = ""
        if score['neg'] > score['pos']:
            type_of_sentiment = "Negative Sentiment"
            # print("Negative Sentiment")
        elif score['neg'] < score['pos']:
            type_of_sentiment = "Positive Sentiment"
            # print("Positive Sentiment")
        else:
            type_of_sentiment = "Neutral Sentiment"
            # print("Neutral Sentiment")

   
        results = {"Score": score,
                   "typeofSentiment": type_of_sentiment, "comments": text , "var1" : var1,"var2" : var2, "var3" : var3 }
        return render_template('product_details.html', results=results)
        # return jsonify({"Emotions":w, "Score": score, "typeofSentiment" :type_of_sentiment})
        # Comment_analytics = setimentanalysis.analysis(text)
        # print(Comment_analytics)
        # return Comment_analytics

    return render_template('product_details.html')


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
