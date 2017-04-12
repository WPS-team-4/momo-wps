| Resource     | GET       | POST | PATCH      | DELETE  |
| ------------ | --------- | ---- | ---------- | ------- |
| /pin/        | 핀 리스트     | 핀 생성 |            |         |
<<<<<<< HEAD

=======
| /pin/{pinId} | 해당 핀 세부정보 |      | 해당 핀 정보 수정 | 해당 핀 삭제 |
>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34

## Pin 리스트 조회

### 요청 주소

`/api/pin/`

### method

GET

### 반환

```
[
  {
    "pk": 1,
    "author": "kay",
    "name": "패캠 옆 카페",
    "place": 1,
    "map": 1,
    "pin_color": "0,0,0",
    "created_date": "2017-04-09T06:30:01.772763Z"
  }
]

```

## Pin 생성

<<<<<<< HEAD
=======
### 1. keyword 검색을 통한 Pin 생성

### 2. 지도 마킹을 통한 Pin 생성

>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34
### 요청 주소

`/api/pin/`

### method

POST

### body
<<<<<<< HEAD
- name
- place
- map
- pin_color
=======
>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34

```
{
    "name": "패캠 카페",
    "place": 2,
    "map": 4,
    "pin_color": "0,0,0"
}

```

### 반환

```
{
    "pk": "3",
    "author": "kay",
    "name": "패캠 카페",
    "place": 2,
    "map": 4,
    "pin_color": "0,0,0"
}
```