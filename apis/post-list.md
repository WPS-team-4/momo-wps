| Resource | GET | POST | PATCH | DELETE |
| --- | --- | --- | --- | --- |
| /api/post/ | 포스트 리스트 조회 | 포스트 생성 |  |  |


### 요청 주소

`/api/post/`

## Post 리스트 조회

### method

GET

### 반환

```
[
  {
    "pk": 28,
    "pin": 3,
    "author": "anohk",
    "photo": "http://127.0.0.1:8000/media/post/b_G2uZbLq.png",
    "created_date": "2017-04-13T09:25:05.357582Z",
    "comment_list": [
      {
        "pk": 2,
        "contents": "여기 좀 괜찮음!",
        "author": "anohk"
      }
    ]
  }
  ...
]
```

## Post 생성

### method

POST

### body

- pin
- photo

```
{
    "pin": "1",
    "photo": "",
}
```

### 반환

생성된 post 반환

```
{
  "pk": 1,
  "pin": 1,
  "author": "anohk",
  "photo": "http://127.0.0.1:8000/media/post/b_oFpdvZx.png",
  "created_date": "2017-04-12T17:07:54.108414Z",
  "comment_list": []
}
```




