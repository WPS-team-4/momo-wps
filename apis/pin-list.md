| Resource     | GET       | POST | PATCH      | DELETE  |
| ------------ | --------- | ---- | ---------- | ------- |
| /pin/        | 핀 리스트     | 핀 생성 |            |         |


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

### 요청 주소

`/api/pin/`

### method

POST

### body
- name
- place
- map
- pin_color

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