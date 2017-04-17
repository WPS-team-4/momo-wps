### 요청 주소
```
/api/post/comment/add/
```
### Headers
```
Authorization : token [token_value]
```
## Comment 생성

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