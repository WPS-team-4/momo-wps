### 요청 주소
```
/api/post/{postId}/
```
### Headers
```
Authorization : token [token_value]
```

## Post 세부정보 조회

### method

GET

### 반환

```
[
  {
    "pk": 1,
    "pin": 1,
    "photo": "https://wps-momo-bucket.s3.amazonaws.com/media/post/b.png",
    "description": "조명이 좋아요",
    "created_date": "2017-04-12T17:16:27.177118Z",
  }
]
```

## Post 세부정보 수정

### method

PATCH

### body

- photo(optional)
- description(optional)

```
[
  {
    "description": "조명이 잘되있고, 의자가 편함!",
  }
]
```

### 반환

```
[
  {
    "pk": 1,
    "pin": 1,
    "photo": "https://wps-momo-bucket.s3.amazonaws.com/media/post/b.png",
    "description": "조명이 잘되있고, 의자가 편함!",
    "created_date": "2017-04-12T17:16:27.177118Z",
  }
]
```

## Post 삭제

### method

DELETE

