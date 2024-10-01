import re 
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
stopwords = set(stopwords.words("english"))

def preprocesing(text):
    text= text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r"https\S+|www\S+|http\S+", '', text, flags = re.MULTILINE)
    text = re.sub(r'\@w+|\#', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words = [ word for word in words if word not in stopwords]

    stemmer = PorterStemmer()
    stems = [stemmer.stem(word) for word in words]    

    return " ".join(stems)