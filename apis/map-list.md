### 요청 주소

```
/api/map/
```

## Map 리스트 조회

### Method

GET

### Headers

`Authorization : token [token_value]`

### URL Params

| name | value | process |
| --- | --- | --- |
| opt | recent\_updated | 가장 최근에 수정된 순서대로 지도목록을 반환합니다. |
|  | recent\_created | 가장 최근에 생성된 순서대로 지도목록을 반환합니다.\(지금은 생성된 시간 기준으로 반환합니다.-모델 수정후에 반영될예정\) |
|  | most\_pins | 핀수가 많은 순서대로 지도목록을 반환합니다. |

### 반환

map list 반환

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



