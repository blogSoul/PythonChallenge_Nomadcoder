from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")
# 서버를 구축합니다.

db = {}
db['vuejs']=''

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html",
    searchingBy=word,
    resultsNumber=len(jobs),
    jobs=jobs
  )

app.run(host="0.0.0.0")
# 0.0.0.0이면 사이트를 공개하겠다는 의미입니다.