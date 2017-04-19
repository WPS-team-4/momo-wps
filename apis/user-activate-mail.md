# send activate mail

> 사용자 계정을 활성화는 메일을 보냅니다.



### URL

`/api/member/activate/`



### Method

`POST`



### Data Params

| name | value   | process                  |
| ---- | ------- | ------------------------ |
| pk   | user_pk | 해당 유저에게 계정 활성화 메일을 보냅니다. |



### Success Response

* Code: 200 OK
* Content:

```json
{
  "detail": "인증메일이 발송되었습니다"
}
```



### Error Response

* Code:

