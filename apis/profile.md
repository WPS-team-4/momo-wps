# member profile view

> user 정보와 user가 소유한 지도, 핀을 리턴합니다

**URL**
`/api/member/{user_id}/`

**Method**
`GET`

**URL Params**

| name    | value   | type     | process |
| ------- | ------- | -------- | ------- |
| user_id | User PK | Interger | 해당 User |

**Data Params**

```

```

header

```
Authorization : token {token_value}
```



**Success Response**

- Code: 200

- Content:

  ```json
  {
      "pk": 2,
      "username": "superkiz",
      "email": "superkiz@momo.com",
      "profile_img": "http://127.0.0.1:8000/media/member/img1_leSRAnI.jpg",
      "following": [],
      "date_joined": "2017-04-05T13:40:52.914047Z",
      "is_facebook": false,
      "is_active": true,
      "is_staff": false,
      "map_list": [
          {
              "pk": 6,
              "name": "고부기 지도",
              "description": "맵 생성 테스트2",
              "pin_list": [
                  {
                      "pk": 11,
                      "author": "superkiz",
                      "name": "리자몽 핀",
                      "place": 1,
                      "map": 6,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-11T10:05:04.807125Z",
                      "post_list": [
                          {
                              "pk": 2,
                              "pin": 11,
                              "photo": "http://127.0.0.1:8000/media/post/img3.jpg",
                              "created_date": "2017-04-11T13:50:54.904918Z",
                              "comment_list": [
                                  {
                                      "pk": 1,
                                      "contents": "테스트 코멘트",
                                      "author": "superkiz"
                                  }
                              ]
                          },
                          {
                              "pk": 3,
                              "pin": 11,
                              "photo": null,
                              "created_date": "2017-04-11T13:51:01.913089Z",
                              "comment_list": [
                                  {
                                      "pk": 2,
                                      "contents": "테스트 코멘트 2",
                                      "author": "superkiz"
                                  }
                              ]
                          }
                      ]
                  },
                  {
                      "pk": 8,
                      "author": "superkiz",
                      "name": "파이리 핀",
                      "place": 1,
                      "map": 6,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-11T10:04:43.624667Z",
                      "post_list": [
                          {
                              "pk": 1,
                              "pin": 8,
                              "photo": "http://127.0.0.1:8000/media/post/fsociety.png",
                              "created_date": "2017-04-11T13:50:19.981681Z",
                              "comment_list": []
                          }
                      ]
                  }
              ],
              "created_date": "2017-04-11T10:04:16.485838Z",
              "is_private": false
          },
          {
              "pk": 5,
              "name": "파이리 지도",
              "description": "맵 생성 테스트2",
              "pin_list": [
                  {
                      "pk": 10,
                      "author": "superkiz",
                      "name": "피카츄 핀",
                      "place": 1,
                      "map": 5,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-11T10:04:56.819697Z",
                      "post_list": []
                  },
                  {
                      "pk": 7,
                      "author": "superkiz",
                      "name": "파이리 핀",
                      "place": 1,
                      "map": 5,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-11T10:04:41.036908Z",
                      "post_list": []
                  }
              ],
              "created_date": "2017-04-11T10:04:09.938776Z",
              "is_private": false
          },
          {
              "pk": 4,
              "name": "피카츄 지도",
              "description": "맵 생성 테스트2",
              "pin_list": [
                  {
                      "pk": 12,
                      "author": "superkiz",
                      "name": "리자몽 핀",
                      "place": 1,
                      "map": 4,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-11T10:05:08.838754Z",
                      "post_list": []
                  },
                  {
                      "pk": 9,
                      "author": "superkiz",
                      "name": "피카츄 핀",
                      "place": 1,
                      "map": 4,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-11T10:04:53.806308Z",
                      "post_list": []
                  },
                  {
                      "pk": 6,
                      "author": "superkiz",
                      "name": "파이리 핀",
                      "place": 1,
                      "map": 4,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-11T10:04:37.145303Z",
                      "post_list": []
                  }
              ],
              "created_date": "2017-04-11T10:04:01.926819Z",
              "is_private": false
          },
          {
              "pk": 3,
              "name": "CREATEMAP2",
              "description": "맵 생성 테스트2",
              "pin_list": [
                  {
                      "pk": 5,
                      "author": "superkiz",
                      "name": "파이리 핀",
                      "place": 1,
                      "map": 3,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-05T16:14:35.163253Z",
                      "post_list": []
                  }
              ],
              "created_date": "2017-04-05T16:13:50.230454Z",
              "is_private": false
          },
          {
              "pk": 2,
              "name": "CREATEMAP2",
              "description": "맵 생성 테스트2",
              "pin_list": [
                  {
                      "pk": 4,
                      "author": "superkiz",
                      "name": "피카츄 핀2",
                      "place": 3,
                      "map": 2,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-05T16:14:17.539655Z",
                      "post_list": []
                  }
              ],
              "created_date": "2017-04-05T16:13:48.633710Z",
              "is_private": false
          },
          {
              "pk": 1,
              "name": "CREATEMAP2",
              "description": "맵 생성 테스트2",
              "pin_list": [
                  {
                      "pk": 3,
                      "author": "superkiz",
                      "name": "피카츄 핀3",
                      "place": 3,
                      "map": 1,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-05T16:13:36.453281Z",
                      "post_list": []
                  },
                  {
                      "pk": 2,
                      "author": "superkiz",
                      "name": "피카츄 핀2",
                      "place": 2,
                      "map": 1,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-05T16:13:31.598636Z",
                      "post_list": []
                  },
                  {
                      "pk": 1,
                      "author": "superkiz",
                      "name": "피카츄 핀",
                      "place": 1,
                      "map": 1,
                      "pin_color": "0,0,0",
                      "created_date": "2017-04-05T16:12:21.760048Z",
                      "post_list": []
                  }
              ],
              "created_date": "2017-04-05T14:35:24.560494Z",
              "is_private": false
          }
      ]
  }
  ```

**Error Response**

- Code: 404

  - Reason: Not found
  - Content: 해당 user가 없음

  ```json
  {
    "detail": "찾을 수 없습니다.",
    "exception": "No MomoUser matches the given query.",
    "status_code": "404 - Not Found"
  }
  ```

  ​

- Code: 401

  - Reason: Unauthorized
  - Content:token 없음

  ```json
  {
    "detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다.",
    "exception": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다.",
    "status_code": "401 - Unauthorized"
  }
  ```

  * Content: token 만료

  ```json
  {
    "detail": "토큰이 유효하지 않습니다.",
    "exception": "토큰이 유효하지 않습니다.",
    "status_code": "401 - Unauthorized"
  }
  ```

  ​

  ​

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



## member profile update

### method

`patch`



### params

email (optional)

profile_img (optional)



### success

200

유저 정보를 반환



### failed

500

파일 형식이 이미지가 아님

