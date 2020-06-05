## section 4.2 Dynamic URLs and Templates

```
from flask import Flask

app = Flask("SuperScrapper")
# 서버를 구축합니다.
@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"

# @는 데코레이터를 의미합니다. 바로 아래 함수를 봅니다.
@app.route("/<username>")
def potato(username):
  return f"Hello {username} how are you doing"

app.run(host="0.0.0.0")
# 0.0.0.0이면 사이트를 공개하겠다는 의미입니다.
```
->
```
from flask import Flask, render_template

app = Flask("SuperScrapper")
# 서버를 구축합니다.
@app.route("/")
def home():
  return render_template("potato.html")
  
app.run(host="0.0.0.0")
# 0.0.0.0이면 사이트를 공개하겠다는 의미입니다.
```
potato.html은
```
<!DOCTYPE html>
<html>
  <head>
    <title>Job Search</title>
  </head>
  <body>
    <h1>Job Search</h1>
    <form>
      <input placeholder='Search for a job' required/>
      <button>Search</button>
    </form>
  </body>
</html>
```