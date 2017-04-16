Resource | GET | POST | PATCH | DELETE | 
--- | --- | --- | --- | --- |
/api/place/ | 장소 리스트 | |  |  |
/api/place/{placeId}/ | 해당 장소 세부정보 |  | 해당 장소 정보 수정 | 해당 장소 삭제 |

### 요청 주소
`/api/place/`


## Place 조회

### method
GET

### 반환
장소 리스트 반환

```
[
    {
        "pk": "1",
        "name": "스테파니 카페",
        "place_id": "ChIJO88Tq5SjfDURVM1dMXzYDGs"
        "address": "551-11, Sinsa-dong, Gangnam-gu, Seoul, South Korea",
        "lat": "37.522"
        "lng": "127.024"
    },
    {
     ...
    },
]
```

## Place 등록

### method
POST

### body
- name
- place_id
- address
- lat
- lng

```
{
    "name": "스테파니 카페",
    "place_id": "ChIJO88Tq5SjfDURVM1dMXzYDGs"
    "address": "551-11, Sinsa-dong, Gangnam-gu, Seoul, South Korea",
    "lat": "37.522"
    "lng": "127.024"
}
```

### 반환
생성된 장소 반환

```
{
    "pk": "1",
    "name": "스테파니 카페",
    "place_id": "ChIJO88Tq5SjfDURVM1dMXzYDGs"
    "address": "551-11, Sinsa-dong, Gangnam-gu, Seoul, South Korea",
    "lat": "37.522"
    "lng": "127.024"
}
```