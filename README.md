# پردازش بر روی متن توسط nltk در زبان پایتون

## گزارش

بدهی است که کد نوشته شد در قسمت `src` قابل رویت است و هر برنامه ای نسبت به
عملکردی که انتظار می رود برنامه نویس آن را نوشته است لازمه مستندسازی معقول است.
در صورتی که تابع نوشته شده در برنامه انتظار مورد نظر را برآورده نمی کند گزارشی
در قسمت این مخزن آماده کنید که برنامه در طی فرآیند تکامل، تصحیح شود.

### سازماندهی فضاهای خالی و یکپارچه سازی حروف

شاید در متد های کتابخانه `nltk` متدی برای کوچکسازی کلمات وجود داشته باشد اما
برای به چالش کشیدن برنامه خود از متد `lower` بعد از پاک کردن فضای اضافی بیش از
حد استفاده کردم.

```python
# WhiteSpace remove
result_en = rm_whitespace(file_path=short_sample_en)
result_fa = rm_whitespace(file_path=short_sample_fa)
print(result_fa, result_en)
```

```text
سلام! امیدوارم خوب باشید :-) . این یک متن کوتاه نمونه است.این تمرین ۱ ما است.
```

```text
hello! hope you're doing well. it is a sample short text.this is our 1 st the assignment :) .
```

### استخراج جملات به همراه توکن ها

دلیل مشکل می تواند همراه داشتن کلمات نگارشی باشد. به همین دلیل میتوان از تابع
مناسب آن در برنامه قبل از استفاده از متد های زیر استفاده کرد که تقسیم جمله و
کلمات (توکن) های مناسبی داشته باشیم.

```python
print(tokenize.PunktSentenceTokenizer().tokenize(result_en))

> ['hello!', "hope you're doing well.", 'it is a sample short text.this is our 1
st the assignment :) .']
```

```text
print(tokenize.TreebankWordTokenizer().tokenize(result_en))

> ['hello', '!', 'hope', 'you', "'re", 'doing', 'well.', 'it', 'is', 'a',
'sample', 'short', 'text.this', 'is', 'our', '1', 'st', 'the', 'assignment',
':', ')', '.']
```

### حذف کلمات نگارشی

```python
# Punctuation remove
print(rm_punctuations(data=result_en))
print(rm_punctuations(data=result_fa))
```

خروجی به شکل زیر است

```python
['hello', 'hope', 'you', 're', 'doing', 'well', 'it', 'is', 'a', 'sample',
'short', 'text', 'this', 'is', 'our', '1', 'st', 'the', 'assignment']

['سلام', 'امیدوارم', 'خوب', 'باشید', 'این', 'یک', 'متن', 'کوتاه', 'نمونه',
'است', 'این', 'تمرین', '۱', 'ما', 'است']

```

### کلمات stopword

در زبان انگلیسی وقتی در مورد کلمات stopword صحبت می شود در واقع وقتی در متنی
کلماتی مانند the، in، on و کلمات ربط دیگه ای وجود داشته باشد، به عنوان
stopwordها شناخته می شود.

متن ورودی:

```python
print(rm_stopwords(data=rm_whitespace(short_sample_en)))
```

متن کوتاه خام انگلیسی

```text
hello! hope you're doing well. it is a sample short text.this is our 1 st the assignment :) .
```

خروجی بدست آمده

```python
['hello', '!', 'hope', "'re", 'well', '.', 'sample', 'short', 'text.this', '1', 'st', 'assignment', ':', ')', '.']
```

### ریشه یابی یا Stemming

با استفاده از متد PorterStemmer در متن Beanstalk:

```python
# Porter stemming
beantalk_stemmed: list = word_stemmer(data=beanstalk, method=stemmer.PorterStemmer())
print(
    beantalk_stemmed[3],
    beantalk_stemmed[11],
    beantalk_stemmed[60],
    beantalk_stemmed[68],
    sep="-",
)
```

```text
time-into-thi-,

```

با استفاده از متد LancasterStemmer در متن Beanstalk:

```python
# Lancaster stemming
beantalk_stemmed: list = word_stemmer(data=beanstalk, method=stemmer.LancasterStemmer())
print(
    beantalk_stemmed[3],
    beantalk_stemmed[11],
    beantalk_stemmed[60],
    beantalk_stemmed[68],
    sep="-",
)
```

```text
tim-into-thi-,
```

با استفاده از متد PorterStemmer در متن کوتاه انگلیسی:

```python
short_sample_en_stemmd: list = word_stemmer(
    data=result_en, method=stemmer.PorterStemmer()
)
print(short_sample_en_stemmd[2])
```

```text
hop
```

با استفاده از متد LancasterStemmer در متن کوتاه انگلیسی:

```python
short_sample_en_stemmd: list = word_stemmer(
    data=result_en, method=stemmer.LancasterStemmer()
)
print(short_sample_en_stemmd[2])
```

```text
hope
```

### Lemmatizing

نتیجه دیتای داده شده جهت رسیدن به قسمت اصلی و اولیه نوشته. برای اطلاعات بیشتر به
`./src/lemm_words` مراجعه کنید.

```python
# Lemmatizing
special_words_lemmatizer(words=lemm_words.words)
```

```text
went -> go
better -> good
was -> be
eaten -> eat
bufferfiles -> bufferfiles
fishing -> fishing
signaling -> signaling
```
