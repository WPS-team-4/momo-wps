&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD  
Resource \| GET \| POST \| PATCH \| DELETE \|   
--- \| --- \| --- \| --- \| --- \|  
/post/ \| 포스트 리스트 \| 포스트 생성 \|  \|  \|

### 요청 주소

`/api/post/`

## Post 리스트 조회

### method

GET

### 반환

```
[
  {
    "pk": 1,
    "pin": 1,
    "photo": "https://wps-momo-bucket.s3.amazonaws.com/media/post/b.png",
    "created_date": "2017-04-12T17:16:27.177118Z",
    "comment_list": [
      {
        "pk": 1,
        "contents": "여기 다시 와볼만함",
        "author": "anohk"
      }
    ]
  },
  ...
]
```

## Post 생성 \(수정중\)

### 요청 주소

`/api/pin/`

### method

POST

### body

* pin

```
{
    "pin": "1",
}
```

### 반환

생성된 post 반환

```
{
  "pk": 1,
  "pin": 1,
  "created_date": "2017-04-12T17:07:54.108414Z",
  "comment_list": []
}
```

=======  
\| Resource                                 \| GET         \| POST   \| PATCH        \| DELETE    \|  
\| ---------------------------------------- \| ----------- \| ------ \| ------------ \| --------- \|  
\| /post/                                   \| 포스트 리스트     \| 포스트 생성 \|              \|           \|  
\| /post/{postId}/                          \| 해당 포스트 세부정보 \|        \| 해당 포스트 정보 수정 \| 해당 포스트 삭제 \|  
\| /post/{postId}/comment/add/              \|             \| 코멘트 생성 \|              \|           \|  
\| /post/{postId}/comment/{commentId}/delete/ \|             \|        \|              \| 코멘트 삭제    \|

## Post 리스트 조회

### 요청 주소

`/api/post/`

### method

GET

### 반환

## Post 생성

### 요청 주소

`/api/pin/`

### method

POST

### 반환

> > > > > > > 9549e77e500331f94b7e6ce91784ded3bb8fec34



