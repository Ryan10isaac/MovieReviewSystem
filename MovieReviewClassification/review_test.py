import pickle
from preprocessing import preprocesing


svm = pickle.load(open('svc.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))


r1 =  "This film was a rollercoaster of emotions, with brilliant performances and a gripping storyline. However, the ending left me feeling unsatisfied and confused."
r2 = "Worst Movie"
r3 = "plot was convoluted and hard to follow. It felt like the director was trying too hard to be artistic"



def predictReview(text):
    input_data = preprocesing(text)
    transformed_data = tfidf.transform([input_data])
    result =  svm.predict(transformed_data)[0]

    if result == 1:
        return 'Positive'
    elif result==0:
        return 'Negative'


print(predictReview(r2))

