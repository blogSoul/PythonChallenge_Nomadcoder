## section 4.6 Rendering Jobs

report.html에서
```
<!DOCTYPE html>
<html>
  <head>
    <title>Job Search</title>
    <style>
      section {
        display:grid;
        gap: 20px;
        grid-template-columns: repeat(4, 1fr);
      }
    </style>
  </head>
  <body>
    <h1>Search Resuls</h1>
    <h3>Found {{resultsNumber}} results for: {{searchingBy}}</h3>
    <section>
      <h4>Title</h4>
      <h4>Company</h4>
      <h4>Location</h4>
      <h4>Link</h4>
      {% for potato in jobs %}
        <span>{{potato.title}}</span>
        <span>{{potato.company}}</span>
        <span>{{potato.location}}</span>
        <a href="{{potato.link}}" target="_blank">Apply</a>
      {% endfor %}
    </section>
    </form>
  </body>
</html>
```
grid를 사용하면 조금 더 깔끔하게 사용할 수 있습니다.