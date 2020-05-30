## section 2.6 ~ 2.8 Extracting Titles, Companies, Locations

```
def extract_job(html):
  title = html.find("h2", {"class" : "title"}).find("a")["title"]
  company = html.find("span", {"class": "company"})
  if company:
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor. string)
    else:
      company = str(company.string)
    company = company.strip()
  else:
    company = None
  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]
  return {
    'title': title, 
    'company': company, 
    'location': location,
    "link": f"{URL}&vjk={job_id}"
  }

```
이와 같은 방식으로 페이지에서 scrapping을 진행합니다.
vjk부분에 따라 부분 페이지가 출력됩니다.
None이 있는 부분이 존재하니 체크할 수 있도록 합니다.
