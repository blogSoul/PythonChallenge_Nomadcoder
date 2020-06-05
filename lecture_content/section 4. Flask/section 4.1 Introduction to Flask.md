## section 4.1 Introduction to Flask

```
from flask import Flask

app = Flask("SuperScrapper")
# 서버를 구축합니다.
@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"

# @는 데코레이터를 의미합니다. 바로 아래 함수를 봅니다.
@app.route("/contact")
def potato():
  return "Contact me!"

app.run(host="0.0.0.0")
# 0.0.0.0이면 사이트를 공개하겠다는 의미입니다.
```