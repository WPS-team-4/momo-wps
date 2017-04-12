| Resource     | GET       | POST | PATCH      | DELETE  |
| ------------ | --------- | ---- | ---------- | ------- |
| /pin/{pinId} | 해당 핀 세부정보 |      | 해당 핀 정보 수정 | 해당 핀 삭제 |

## Pin 세부정보 조회

### 요청 주소

`/pin/{pinId}`

### method

GET

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

## Pin 세부정보 수정

### 요청 주소

`/pin/{pinId}`

### method

PATCH

### body
다음 중 하나 이상의 값을 받습니다  

- name
- place
- map
- pin_color

```
{
    "name": "바실",
}
```

### 반환

```
{
    "pk": "3",
    "author": "kay",
    "name": "바실",
    "place": 2,
    "map": 4,
    "pin_color": "0,0,0"
}
```

## Pin 삭제

### 요청 주소

`/pin/{pinId}`

### method

DELETE