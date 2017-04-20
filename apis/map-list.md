# Map List view

> 전체 지도 목록을 옵션값대로 정렬해서 반환합니다.



### URL

`/api/map/`



### Headers

`Authorization : token [token_value]`



### Method

`GET`



### URL Params

| name | value           | process                                  |
| ---- | --------------- | ---------------------------------------- |
| opt  | recent\_created | 가장 최근에 생성된 순서대로 지도목록을 반환합니다.             |
|      | most\_pins      | 핀수가 많은 순서대로 지도목록을 반환합니다.                 |
| page |                 | 특정 페이지의 목록만 반환합니다.                       |
|      |                 | 파라미터가 없으면 기본값으로 최근 업데이트 순 으로 정렬해서 지도목록을 반환합니다. |



### Success Response
> 기본적으로 가장 최근에 업데이트된 순서로 지도목록을 반환합니다

* Code: 200 OK
* Content:

```json
[
    {
        "pk": "1",
        "map_name": "카페지도",
        "description": "조명이 좋은 카페 리스트",
        "is_private": "false"
        "author": {
            "pk": "5",
            "username": "kay",
            "profile_image": "/media/post/provisional_dtP071M.png"
        },
        "created_date": "2017-04-09T06:26:10.279343Z"
    },
    {
    ...
    },
]
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



# Map Create

> 맵을 생성하고, 생성된 맵을 반환합니다.



### URL

`/api/map/`



### Headers

`Authorization : token [token_value]`



### Method

`POST`



### Body

| name        | value            | process |
| ----------- | ---------------- | ------- |
| name        | 지도 이름            |         |
| description | 지도 설명            |         |
| is_private  | 지도 공개여부(boolean) |         |



### Success Response

* Code: 201 CREATED
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

