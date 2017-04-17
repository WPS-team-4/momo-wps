# sign-up

> 새로운 유저를 생성합니다.

**URL**
`/api/member/signup/`

**Method**
`POST`

**Data Params**

| name               | value  | type   | process |
| ------------------ | ------ | ------ | ------- |
| username(required) | 회원 아이디 | string |         |
| password(required) |        |        |         |
| email(required)    |        |        |         |



**Success Response**

- Code: 201 CREATED

- Content:

  ```json
  {
      "username":"",
    	"password":"",
    	"email":""
  }
  ```

**Error Response**

- Code: 400 BAD REQUEST

  - Reason: BAD REQUEST
  - Content: username 중복, email 유효하지 않음

  ```json
  {
    "email": [
      "유효한 이메일 주소를 입력하십시오."
    ],
    "username": [
      "momo user의 username은/는 이미 존재합니다."
    ],
    "status_code": "400 - Bad Request",
    "exception": "{'email': ['유효한 이메일 주소를 입력하십시오.'], 'username': ['momo user의 username은/는 이미 존재합니다.'], 'status_code': '400 - Bad Request'}"
  }
  ```

  ​

- Code: 500

  - Reason:
  - Content: 필수 파라미터 없을때
