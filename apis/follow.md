# follow

> 요청을 보내면 접속중인 유저\(from\_user\)가 to\_user\(pk=user\_pk\)를 팔로우, 언팔로우 합니다.

### URL

`/api/member/{user_pk}/follow/`

### Method

`PATCH`

### Headers

`Authorization : token [token_value]`

### 

### Success Response

* Code: 201 CREATED
* Content:

```json
{
  "to_user": 20,
  "from_user": 12,
  "status": "follow"
}
```

* Code: 204 NO CONTENT

* Content:



### 

### Error Response

* Code: 406 Not Acceptable
* Content:

```json
{
  "status_code": "406 - Not Acceptable",
  "errors": [],
  "detail": "자기 자신은 follow할 수 없습니다"
}
```





