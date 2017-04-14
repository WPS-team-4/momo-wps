| Resource | GET | POST | PATCH | DELETE |
| --- | --- | --- | --- | --- |
| /api/search/ | map 또는 user 검색 |  |  |  |

### 요청 주소

`/api/search/`

## Map or User 검색

### method

GET

### params
- key

```
{
	"key": "조용한"
}
```

### 반환
`key`값은 아래와 같은 필드에서 대소문자 구분없이 포함되는 데이터를 필터링한다.

model | fields |
--- | --- |
Map | map_name, description |
User | username |


```
{
	"map": [
		{
        "pk": "1",
        "map_name": "카페지도",
        "description": "조용한 카페 모음",
        "is_private": "false"
        "author": {
            "pk": "5",
            "username": "kay",
            "profile_image": "/media/post/provisional_dtP071M.png"
    		},
        "created_date": "2017-04-09T06:26:10.279343Z"
    	},
    	...
	],
	"user": [
			
	]
}
```
