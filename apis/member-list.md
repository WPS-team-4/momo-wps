# member-list

> 옵션별로 정렬한 사용자 목록을 반환합니다.



### URL

`/api/member/`



### Method

`GET`



### Headers

`Authorization : token [token_value]`



### URL Params

| name  |     value     |             type             |
| :---: | :-----------: | :--------------------------: |
| field |      pk       |                              |
|       |   username    |                              |
|       |   password    |                              |
|       |     email     |                              |
|       |   map_list    |                              |
|  opt  | most_follower |   팔로워가 가장 많은 순서대로 유저목록을 반환   |
|       |   most_maps   | 생성한 지도가 가장 많은 순서대로 유저 목록을 반환 |






### Success Response

- Code: 200
- Content:
- {{host}}/api/member/?fields=pk,username,email?opt=most_followers
      

### Error Response

- Code:401




