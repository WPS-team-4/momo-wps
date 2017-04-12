# login

> 

**URL**
`/api/member/logout/`

**Method**
`POST`

**header**

| name  | value | type   | process |
| ----- | ----- | ------ | ------- |
| token |       | string |         |



**Success Response**

- Code: 200

- Content:

  ```json
  [
    "정상적으로 로그아웃 되었습니다"
  ]
  ```

**Error Response**

- Code: 401

  - Reason: 
  - Content: 만료된 토큰, 토큰 없음

  ```

  ```

  ​

**Sample Call**

```javascript
$.ajax({
  url: '/api/member/login/',
  data: {},
  dataType: 'json',
  type: 'POST',
  success: function(response) {
    console.log(response);
  }
});
```

