## section 2.5 Requesting Each Page

```
result = requests.get(f"{URL}&start={page*LIMIT}")
```
이와 같은 방식으로 해당 사이트에 Request를 요청합니다.