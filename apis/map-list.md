### 요청 주소

```
/api/map/
```
### Headers
```
Authorization : token [token_value]
```

## Map 리스트 조회

### Method

GET

### URL Params

| name | value | process |
| --- | --- | --- |
| opt | recent\_created | 가장 최근에 생성된 순서대로 지도목록을 반환합니다.|
|  | most\_pins | 핀수가 많은 순서대로 지도목록을 반환합니다. |



### 반환
기본적으로 가장 최근에 업데이트된 순서로 지도목록을 반환합니다

```
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

## Map 생성

### method

POST

### body

* name
* description
* is\_private

```
{
    "map_name": "카페지도",
    "description": "조명이 좋은 카페 리스트",
    "is_private": "false",  
}
```

### 반환

생성된 map 객체를 반환한다.

```
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



