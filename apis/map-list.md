| Resource | GET    | POST  | PATCH | DELETE |
| -------- | ------ | ----- | ----- | ------ |
| /map/    | 지도 리스트 | 지도 생성 |       |        |

## Map 리스트 조회

### 요청 주소

`/api/map/`

### method

GET

### 반환

map list 반환

```
[
    {
        "pk": "1",
        "name": "카페지도",
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

### 요청 주소

`/api/map/`

### method

POST

### body
- name
- description
- is_private

```
{
    "name": "카페지도",
    "description": "조명이 좋은 카페 리스트",
    "is_private": "false",  
}

```

### 반환

생성된 map 객체를 반환한다.

```
{
    "pk": "1",
    "name": "카페지도",
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