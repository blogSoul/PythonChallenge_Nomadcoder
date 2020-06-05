## section 4.4~5 Scrapper Intergration and Faster Scrapper

main.py에선
```
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")
# 서버를 구축합니다.

db = {}

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    fromDb = db.get(word)
    if fromDb:
      jobs = fromDb
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html", 
  searchingBy=word,
  resultsNumber=len(jobs)
  )

app.run(host="0.0.0.0")
# 0.0.0.0이면 사이트를 공개하겠다는 의미입니다.
```
fakeDB는 라우터 밖에 있어야 합니다.