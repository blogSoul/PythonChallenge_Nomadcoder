## section 4.3 Forms and Query Arguments

```https://superscrapper--minwooksoul.repl.co/report?word=asd``` 여기 링크 중에서 ?이전까지는 url입니다. ?이후는 Query Argument라고 부릅니다.

```
from flask import Flask, render_template, request

app = Flask("SuperScrapper")
# 서버를 구축합니다.
@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  print(request.args.get('word'))
  return "this is the report"

app.run(host="0.0.0.0")
# 0.0.0.0이면 사이트를 공개하겠다는 의미입니다.
```

flask는 html파일을 보고 Rendering을 해줍니다. Ex)Rendering to {{}}

main.py
```
from flask import Flask, render_template, request

app = Flask("SuperScrapper")
# 서버를 구축합니다.
@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html", searchingBy=word, potato='sexy')

app.run(host="0.0.0.0")
# 0.0.0.0이면 사이트를 공개하겠다는 의미입니다.
```

templates/potato.py
```
<!DOCTYPE html>
<html>
  <head>
    <title>Job Search</title>
  </head>
  <body>
    <h1>Job Search</h1>
    <form action="/report" method="get">
      <input placeholder='Search for a job' required name="word"/>
      <button>Search</button>
    </form>
  </body>
</html>
```

templates/report.py
```
<!DOCTYPE html>
<html>
  <head>
    <title>Job Search</title>
  </head>
  <body>
    <h1>Search Resuls</h1>
    <h3>You are looking for {{searchingBy}}</h3>
    {{potato}}
    </form>
  </body>
</html>
```