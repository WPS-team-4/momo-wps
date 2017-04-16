<!--| Resource     | GET        | POST | PATCH       | DELETE   |
| ------------ | ---------- | ---- | ----------- | -------- |
| /api/map/{mapId} | 해당 지도 세부정보 |      | 해당 지도 정보 수정 | 해당 지도 삭제 |-->


### 요청 주소

```
/api/map/{mapID}
```


## Map 세부정보 조회

### method

GET

### 반환

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
    "pin_list": [
      {
      "pk": 1,
      "author": "kay",
      "pin_name": "신사 스터디 카페",
      "place": 1,
      "map": 1,
      "pin_color": "0,0,0",
      "created_date": "2017-04-09T06:30:01.772763Z"
      },
    ],
    "created_date": "2017-04-09T06:26:10.279343Z"
}
```

## Map 수정

### method

PATCH

### body

다음 중 하나 이상의 값을 받습니다  

- name
- description
- is_private

```
{
    "is_private": "true"
}
```

### 반환

수정된 map 반환

```
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
      "pin_color": "0,0,0",
      "created_date": "2017-04-09T06:30:01.772763Z"
      },
    ],
    "created_date": "2017-04-09T06:26:10.279343Z"
}
```

## Map 삭제

### method

DELETE