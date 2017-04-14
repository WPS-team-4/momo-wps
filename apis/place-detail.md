Resource | GET | POST | PATCH | DELETE | 
--- | --- | --- | --- | --- |
/api/place/{placeId}/ | 해당 장소 세부정보 |  |  | 해당 장소 삭제 |

### 요청 주소
`/api/place/{placeId}/`


## Place 세부정보 조회

### method
GET

### 반환
{placeId} 에 해당하는 장소 반환

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

## Place 삭제

### method

DELETE