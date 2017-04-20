# send auth mail

> 사용자 계정을 활성화는 메일을 보냅니다. \(인증 메일 재발송\)

### URL

`/api/member/auth-mail/`

### Method

`POST`

### Data Params

| name | value | process |
| --- | --- | --- |
| pk | user\_pk | 해당 유저에게 계정 활성화 메일을 보냅니다. |

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



