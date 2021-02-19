import matplotlib.pyplot as plt
import json
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def analysis(text):
    # converting to lowercase
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

        # Using word_tokenize because it's faster than split()
        tokenized_words = word_tokenize(cleaned_text, "english")

        # Removing Stop Words
        final_words = []
        for word in tokenized_words:
            if word not in stopwords.words('english'):
                final_words.append(word)

        # Lemmatization - From plural to single + Base form of a word (example better-> good)
        lemma_words = []
        for word in final_words:
            word = WordNetLemmatizer().lemmatize(word)
            lemma_words.append(word)

        emotion_list = []
        with open('emotions.txt', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')

                if word in lemma_words:
                    emotion_list.append(emotion)


        w = Counter(emotion_list)

        return json.dumps(w)

        # def sentiment_analyse(sentiment_text):
        #     score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        #     print(score)
        #     if score['neg'] > score['pos']:
        #         print("Negative Sentiment")
        #     elif score['neg'] < score['pos']:
        #         print("Positive Sentiment")
        #     else:
        #         print("Neutral Sentiment")

    #     sentiment_analyse(cleaned_text)

    #     Plotting the emotions on the graph

    #     fig, ax1 = plt.subplots()
    #     ax1.bar(w.keys(), w.values())
    #     fig.autofmt_xdate()
    #     plt.savefig('graph.png')
    #     plt.show()
    #     figureObject, axesObject = plt.subplots()

    

    # # Draw the pie chart

    #     axesObject.pie(w.values(),
    #     labels=w.keys(),
    #     autopct='%1.2f',
    #     startangle=90)

    #     # Aspect ratio - equal means pie is a circle
        
    #     axesObject.axis('equal')
    #     plt.savefig('pie.png')
    #     plt.show()
    # return 'success'