# facebook login

> facebook user access token을 받아 새로운 user를 가져오거나 생성해서 user의 token을 반환합니다.

**URL**  
`/api/member/fb/`

**Method**  
`POST`

**Data Params**

| name | value | type | process |
| --- | --- | --- | --- |
| access\_token | facebook user access token |  | facebook debug token을 요청하고 user 가입처리를 한 뒤에 token과 DB에 존재하는 유저인지 여부를 반환 |

**Success Response**

* Code: 200

* Content:

  ```json
  {
    "token": "270e7dbfc4d066ec33f6b46a91b11f6fc21df63e",
    "created": false
  }
  ```

**Error Response**

* Code: 400

* Reason: @@@

* Content:

` `

* Code: 401

* Reason: Unauthorized

* Content:

```json
{
  "detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
}
```

**Sample Call**

```javascript
$.ajax({
  url: '/api/member/{user_id}/',
  dataType: 'json',
  type: 'GET',
  success: function(response) {
    console.log(response);
  }
});
```



