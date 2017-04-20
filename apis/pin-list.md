# Pin List view

>



### URL

`/api/pin/`



### Headers
`Authorization : token [token_value]`



### Method

`GET`



### Success Response

* Code: 200 OK
* Content:

```json
[
  {
    "pk": 1,
    "author": "kay",
    "pin_name": "패캠 옆 카페",
    "place": 1,
    "map": 1,
    "pin_label": "2",
    "created_date": "2017-04-09T06:30:01.772763Z"
  },
  ...
]
```



### Error Response

* Code:
* Reason:
* Content:

```json

```



---



# Pin Create

>



### Method

`POST`



### Body

| name      | value | label name |
| --------- | ----- | ---------- |
| pin_label | 0     | place      |
|           | 1     | food       |
|           | 2     | cafe       |
|           | 3     | shop       |
|           | 4     | etc        |

#### A. 지도에서 장소를 선택해서 핀을 만드는 경우

- pin  
  <<<<<<< HEAD
-  pin_name
-  map
-  pin_color
   =======
   - pin_name
   - map
   - pin_label
>>>>>>> 88772c41520ee44574885fdaab53202bf9d71215
- place  
- lat
- lng


```
{
	"pin": {
		"map": "5",
		"pin_name": "CafeB",
		"pin_label: "2"
	},
	"place": {
		"lng": "126.9760823",
		"lat": "37.5667701"
	}
}
```

#### B. 장소 검색결과에서 장소를 선택하여 핀을 만드는 경우
- pin  
  <<<<<<< HEAD
-  pin_name
-  map
-  pin_color
   =======
   - pin_name
   - map
   - pin_label
>>>>>>> 88772c41520ee44574885fdaab53202bf9d71215
- place  
- place_id
- name
- address
- lat
- lng


```
{
	"pin": {
		"map": "5",
		"pin_name": "CafeB",
		"pin_label: "2"
	},
	"place": {
		"place_id": "ChIJmc7grvKifDURHm9YxvGM9Rg",
		"name": "카페비",
		"address": "3-7 Jeong-dong, Jung-gu, Seoul, South Korea",
		"lng": "126.9760823",
		"lat": "37.5667701"
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
    "pin_label": "2",
    "created_date": "2017-04-16T15:52:26.979675Z",
    "post_list": []
}
```