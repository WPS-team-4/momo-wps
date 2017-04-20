### 요청 주소

```
/api/pin/{pinId}
```
### Headers
```
Authorization : token [token_value]
```


## Pin 세부정보 조회


### method
GET

### 반환

```
{
  "pk": 1,
  "author": "anohk",
  "pin_name": "루카루",
  "place": 1,
  "map": 2,
  "pin_label": "2",
  "created_date": "2017-04-12T17:07:54.108414Z",
  "post_list": [
    {
      "pk": 1,
      "pin": 1,
      "photo": "https://wps-momo-bucket.s3.amazonaws.com/media/post/b.png",
      "description": "조용하고 쾌적함",
      "created_date": "2017-04-12T17:16:27.177118Z",
    },
    ...
  ]
}
```

## Pin 세부정보 수정


### method

PATCH

### body

다음 중 하나 이상의 값을 받습니다  

- name
- map(map의 pk값)
- pin_label

```
{
    "pin_name": "스터디카페",

```

### 반환

```
{
  "pk": 1,
  "author": "anohk",
  "pin_name": "스터디카페",
  "place": 1,
  "map": 2,
  "pin_label": "2",
  "created_date": "2017-04-12T17:07:54.108414Z",
  "post_list": [
    {
      "pk": 1,
      "pin": 1,
      "photo": "https://wps-momo-bucket.s3.amazonaws.com/media/post/b.png",
      "description": "조용하고 쾌적함",
      "created_date": "2017-04-12T17:16:27.177118Z",
    }
  ]
}
```

## Pin 삭제

### method

DELETE