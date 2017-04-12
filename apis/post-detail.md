Resource | GET | POST | PATCH | DELETE | 
--- | --- | --- | --- | --- |
/post/{postId}/ | 해당 포스트 세부정보 |  |  | 해당 포스트 삭제 |

### 요청 주소
`/api/post/{postId}/`

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
    "created_date": "2017-04-12T17:16:27.177118Z",
    "comment_list": []
  }
]
```

## Post 세부정보 수정

### method
PATCH

### body
다음 중 하나 이상의 값을 받습니다
- photo


## Post 삭제

### method

DELETE



> `pin` 은 `pin_name` 으로 pk값이 아닌 pin 이름을 보여주도록 변경될 예정입니다.


