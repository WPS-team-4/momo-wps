| Resource     | GET       | POST | PATCH      | DELETE  |
| ------------ | --------- | ---- | ---------- | ------- |
| /api/pin/    | 핀 리스트     | 핀 생성 |         |         |

### 요청 주소

`/api/pin/`


## Pin 리스트 조회


### method

GET

### 반환

```
[
  {
    "pk": 1,
    "author": "kay",
    "pin_name": "패캠 옆 카페",
    "place": 1,
    "map": 1,
    "pin_color": "0,0,0",
    "created_date": "2017-04-09T06:30:01.772763Z"
  },
  ...
]

```

## Pin 생성

### 요청 주소

`/api/pin/`

### method

POST

### body

- pin  
	- pin_name
	- map
	- pin_color
- place  
	- place_id
	- name
	- lat
	- lng
	- address

```
{
	"place": {
		"place_id": "ChIJmc7grvKifDURHm9YxvGM9Rg",
		"name": "카페비",
		"formatted_address": "3-7 Jeong-dong, Jung-gu, Seoul, South Korea",
		"lng": "126.9760823",
		"lat": "37.5667701"
	},
	"pin": {
		"map": "5",
		"pin_name": "CafeB"
	}
}

```

### 반환

```
{
    "pk": "3",
    "author": "kay",
    "pin_name": "CafeB",
    "place": 2,
    "map": 5,
    "pin_color": "0,0,0"
}
```