from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import Lobbob
from mozg import *

# Преобразование текстовых данных в числовые векторы
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(list(Lobbob.dataset.keys()))

# Обучение модели логистической регрессии
clf = LogisticRegression()
clf.fit(vectors, list(Lobbob.dataset.values()))

del Lobbob.dataset


while True:
    ques = input('Введите свой вопрос:')
    text_vector = vectorizer.transform([ques])
# Предсказание ответа
    answer = clf.predict(text_vector)[0]
    print(str(answer))

