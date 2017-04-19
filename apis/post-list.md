### 요청 주소
```
/api/post/
```
### Headers
```
Authorization : token [token_value]
```
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
      "photo": "http://momo-master-eb.ap-northeast-2.elasticbeanstalk.com/media/post/b_3GB3P3y.png",
    "created_date": "2017-04-13T09:25:05.357582Z",
    "description": "여기 좀 괜찮음!"
  }
  ...
]
```

## Post 생성

### method

POST

### body

- pin(post를 작성하려는 pin의 pk값)
- photo(optional)
- description(optional)

```
{
    "pin": "1",
    "photo": "http://127.0.0.1:8000/media/post/b_oFpdvZx.png",
    "description": "좋아요!"
}
```
> photo, description 두 값 모두 넣지 않은 상태로 생성할 수 없도록 처리 필요

### 반환

생성된 post 반환

```
{
  "pk": 1,
  "pin": 1,
  "author": "anohk",
  "photo": "http://127.0.0.1:8000/media/post/b_oFpdvZx.png",
  "description": "좋아요!"
  "created_date": "2017-04-12T17:07:54.108414Z",
}
```




