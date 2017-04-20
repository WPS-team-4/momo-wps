### 요청 주소
```
/api/search/
```
### Headers
```
Authorization : token [token_value]
```

## Map or User 검색

### method

GET

### params
- keyword

```
{
	"keyword": "조용한"
}
```

### 반환
`keyword`값은 아래와 같은 필드에서 대소문자 구분없이 포함되는 데이터를 필터링한다.

model | fields |
--- | --- |
Map | map_name, description |
User | username |


```
{
  "maps": [
      {
      "pk": 52,
      "map_name": "조용한 장소",
      "description": "주변 소음이 없어 녹음하기 좋은 곳들",
      "is_private": false,
      "author": "anny",
      "created_date": "2017-04-13T09:20:53.583006Z"
    },
    {
      "pk": 3,
      "map_name": "서울 카페지도",
      "description": "조용한 카페, 채광이 좋음",
      "is_private": false,
      "author": "anohk",
      "created_date": "2017-04-13T09:20:53.583006Z"
    },
    ...
  ],
  "users": [
    {
      "pk": 2,
      "username": "조용한",
      "profile_img": "http://momo-master-eb.ap-northeast-2.elasticbeanstalk.com/media/post/b_3GB3P3y.png",
    },
    ...
  ]
}
```