# login

> username과 password가 일치하면, token값과 token생성일, user\_pk 값을 반환합니다.



### **URL**

`/api/member/login/`



### **Method**

`POST`



### **Data Params**

| name     | value | type   | process |
| -------- | ----- | ------ | ------- |
| username |       | string |         |
| password |       | string |         |



### **Success Response**

* Code: 200 OK

* Content:

  ```json
  {
    "user_pk": 1,
    "created": "2017-04-13T17:56:08.106760Z",
    "token": [token_value]
  }
  ```



### **Error Response**

* Code: 400

* Reason: password불일치, username 불일

* Content:

  ```json
  {
    "detail": "['사용자를 찾을 수 없습니다. username과 password를 다시 확인해주세요.']",
    "errors": [],
    "status_code": "400 - Bad Request"
  }
  ```

  ​

* Code: 403 Forbidden

* Reason: is\_active=False\(인증 메일로 인증과정을 거쳐야 함\)

* Content:

  ```json
  {
    "detail": "인증 메일을 확인해주세요.",
    "errors": [],
    "status_code": "403 - Forbidden"
  }
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



