| Resource | GET | POST | PATCH | DELETE |
| --- | --- | --- | --- | --- |
| /api/post/comment/add/| 코멘트 생성 |  |  |  |
| /api/post/comment/{comment_id}/delete/| |  |  | 코멘트 삭제 |


## Comment 생성

### 요청 주소
`/api/post/comment/add/`


### method
POST

### 반환

```
{
  "pk": 5,
  "contents": "6월엔 예약이 많다고함",
  "author": "anohk"
}
```

## Comment 삭제
### 요청 주소
`/api/post/comment/{comment_id}/delete/`


### method
DELETE