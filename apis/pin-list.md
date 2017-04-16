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
  }
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
	"pin" : {
	   "pin_name": "패캠 카페",
   		"map": 4,
    	"pin_color": "0,0,0"
    },
    "place" : {
    	"place_id" : " - ",
    	"name" : " ",
    	"address" : " ",
    	"lat" : " ",
    	"lng" : " "
    }
}

```

### 반환

```
{
    "pk": "3",
    "author": "kay",
    "pin_name": "패캠 카페",
    "place": 2,
    "map": 4,
    "pin_color": "0,0,0"
}
```