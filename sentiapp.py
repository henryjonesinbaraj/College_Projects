import streamlit as st
import nltk
nltk.downloader.download('vader_lexicon')
 


from nltk.sentiment.vader import SentimentIntensityAnalyzer
method = SentimentIntensityAnalyzer()




st.header('Sentiment Analysis Web App - Henry Jones(DevOps)')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        sentimental_score=method.polarity_scores(text)
        positive_score = round((sentimental_score['pos']*10),2)
        negative_score = round((sentimental_score['neg']*10),2)
        Neutral_score  = round((sentimental_score['neu']*10),2)
        scores = [positive_score,negative_score,Neutral_score]
        max_value = max(scores)
        index = scores.index(max_value)
        max_value = max(scores)
        index = scores.index(max_value)
        if index == 0:
            st.write('The given text,tweet or paragraph is Positive')
        elif index == 1:
            st.write('The given text,tweet or paragraph is Negative')
        else:
            st.write('The given text,tweet or paragraph is Neutral')
        st.write('positive_score: ', round((sentimental_score['pos']*10),2))
        st.write('negative_score: ', round((sentimental_score['neg']*10),2))
        st.write('Neutral_score: ', round((sentimental_score['neu']*10),2))
        st.write('*Score Ranges from 0.00 to 10.00, A parameter which has highest score is the desired sentimental score of the given text')
    else:
        st.write('Please Type a sentence to give the output')
