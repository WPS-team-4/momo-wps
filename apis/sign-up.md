# sign-up

> 새로운 유저를 생성합니다. 유저를 생성 후에 인증메일을 발송합니다.

**URL**  
`/api/member/signup/`

**Method**  
`POST`

**Data Params**

| name | value | type | process |
| --- | --- | --- | --- |
| username\(required\) | 회원 아이디 | string |  |
| password\(required\) |  |  |  |
| email\(required\) |  |  |  |

**Success Response**

* Code: 201 CREATED

* Content:

  ```json
  {
    "pk": 41,
    "username": "kizmo20",
    "password": "pbkdf2_sha256$30000$6U1fg7I0Uepe$0CaaLLmxnznQ8K8caJRrMFyTcNKUvhRPgfJRxtTQ2/I=",
    "email": "superkiz@momo.com",
    "profile_img": null,
    "relation_user_set": [],
    "date_joined": "2017-04-18T09:16:48.082391Z",
    "last_login": null,
    "is_facebook": false,
    "is_active": true,
    "is_staff": false,
    "is_superuser": false,
    "map_list": []
  }
  ```

**Error Response**

* Code: 400 BAD REQUEST

  * Reason: BAD REQUEST
  * Content: username 중복, email 유효하지 않음

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

* Code: 500

  * Reason:
  * Content: 필수 파라미터 없을때



