Resource | GET | POST | PATCH | DELETE | 
--- | --- | --- | --- | --- |
/post/ | 포스트 리스트 | 포스트 생성 |  |  |

### 요청 주소
`/api/post/`

## Post 리스트 조회

### method
GET

### 반환


## Post 생성
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
	"name": "루카루",
	"place": "1",
	"map": "2"
}
```

### 반환
생성된 post 반환

```
{
  "pk": 1,
  "author": "anohk",
  "name": "루카루",
  "place": 1,
  "map": 2,
  "pin_color": "0,0,0",
  "created_date": "2017-04-12T17:07:54.108414Z",
  "post_list": []
}
```

> 반환 시 post_list 는 표현되지 않게 수정해야함