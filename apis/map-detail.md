# Map Detail view

> 지도의 세부정보를 반환합니다.



### URL

`/api/map/{map_pk}`



### Headers

`Authorization : token [token_value]`



### Method

`GET`



### Success Response

* Code: 200 OK
* Content:

```json
{
    "pk": "1",
    "map_name": "카페지도",
    "description": "조명이 좋은 카페 리스트",
    "is_private": "false",
    "author": {
        "pk": "5",
        "username": "kay",
        "profile_image": "/media/post/provisional_dtP071M.png"
    },
    "pin_list": [
      {
      "pk": 1,
      "author": "kay",
      "pin_name": "신사 스터디 카페",
      "place": 1,
      "map": 1,
      "pin_label": "2",
      "created_date": "2017-04-09T06:30:01.772763Z"
      },
    ],
    "created_date": "2017-04-09T06:26:10.279343Z"
}
```



### Error Response

* Code:
* Reason:
* Content:

```json
{
  
}
```



___



# Map Detail update(partial)

> 지도의 세부정보를 업데이트 합니다.



### Method

`PATCH`



### Body

| name        | value             | process          |
| ----------- | ----------------- | ---------------- |
| name        | 지도 이름             | 지도 이름을 업데이트 합니다. |
| description | 지도 설명             |                  |
| is_private  | 지도 공개 여부(boolean) | 지도 공개 여부를 변환합니다. |



### Success Response

* Code:
* Content:

```json
{
    "pk": "1",
    "map_name": "카페지도",
    "description": "조명이 좋은 카페 리스트",
    "is_private": "true",
    "author": {
        "pk": "5",
        "username": "kay",
        "profile_image": "/media/post/provisional_dtP071M.png"
    },
    "pin_list": [
      {
      "pk": 1,
      "author": "kay",
      "pin_name": "신사 스터디 카페",
      "place": 1,
      "map": 1,
      "pin_label": "2",
      "created_date": "2017-04-09T06:30:01.772763Z"
      },
    ],
    "created_date": "2017-04-09T06:26:10.279343Z"
}
```



### Error Response

* Code:
* Reason:
* Content:

```json
{
  
}
```



___



# Map Delete

> 특정 pk값의 지도객체를 삭제합니다.



### Method

`DELETE`



### Success Response

* Code: 204 No Content
* Content:

```json

```



### Error Response

* Code: 
* Reason:
* Content:

```json

```

