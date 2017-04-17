### 요청 주소
```
/api/search/place/
```
### Headers
```
Authorization : token [token_value]
```

## 장소 검색

### method

GET

### params
- keyword

```
{
	"keyword": "성신여대 카페"
}
```

### 반환
google place API로 `keyword` 검색 후 결과 반환

```
[
  {
    "lat": 37.5911159,
    "name": "띠아모(성신여대점)",
    "lng": 127.019687,
    "place_id": "ChIJb1JOkri8fDURJGHuFTAOqnY",
    "address": "135-1 Dongseondong 2(i)-ga, Seongbuk-gu, Seoul, South Korea"
  },
  {
    "lat": 37.5931137,
    "name": "스타벅스 성신여대점",
    "lng": 127.0184022,
    "place_id": "ChIJHaMBVce8fDURQi0W3BjXqlc",
    "address": "92-1 Dongseondong 1(il)-ga, 성북구 South Korea"
  },
  {
    "lat": 37.59089099999999,
    "name": "스타벅스 성신여대정문점",
    "lng": 127.018793,
    "place_id": "ChIJiUrpgLi8fDURWxYu7Q8-AJs",
    "address": "South Korea, Seoul, Seongbuk-gu, 2가 134"
  },
  ...
]
```