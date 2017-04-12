# login

> 

**URL**
`/api/member/login/`

**Method**
`POST`

**Data Params**

| name     | value | type   | process |
| -------- | ----- | ------ | ------- |
| username |       | string |         |
| password |       | string |         |



**Success Response**

- Code: 200

- Content:

  ```json
  {
    "token": {token_value}
  }
  ```

**Error Response**

- Code: 400

  - Reason: 비번틀림, username 틀림,
  - Content:

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

