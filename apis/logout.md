# logout

> token과 함께 요청을 보내면 token을 삭제하고 로그아웃 처리를 합니다.

### **URL**

###### `/api/member/logout/`

### **Method**

`POST`

### Headers

```json
Authorization : token [token_value]
```

### **Success Response**

* Code: 200

* Content:

  ```json
  [
    "정상적으로 로그아웃 되었습니다"
  ]
  ```

### **Error Response**

* Code: 401

  * Reason: token 만료
  * Content: 

  ```json
  {
    "detail": "토큰이 유효하지 않습니다.",
    "errors": [],
    "status_code": "401 - Unauthorized"
  }
  ```

  * Reason: token 없음
  * Content:

  ```json
  {
    "detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다.",
    "errors": [],
    "status_code": "401 - Unauthorized"
  }​
  ```



### **Sample Call**

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



