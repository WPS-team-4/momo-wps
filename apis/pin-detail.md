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
  "pin_color": "0,0,0",
  "created_date": "2017-04-12T17:07:54.108414Z",
  "post_list": [
    {
      "pk": 1,
      "pin": 1,
      "photo": "https://wps-momo-bucket.s3.amazonaws.com/media/post/b.png",
      "created_date": "2017-04-12T17:16:27.177118Z",
      "comment_list": [
        {
          "pk": 1,
          "contents": "또와야지",
          "author": "anohk"
        }
      ]
    }
  ]
}
```

## Pin 세부정보 수정


### method

PATCH

### body

다음 중 하나 이상의 값을 받습니다  

- name
- place
- map
- pin_color

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
  "pin_color": "0,0,0",
  "created_date": "2017-04-12T17:07:54.108414Z",
  "post_list": [
    {
      "pk": 1,
      "pin": 1,
      "photo": "https://wps-momo-bucket.s3.amazonaws.com/media/post/b.png",
      "created_date": "2017-04-12T17:16:27.177118Z",
      "comment_list": [
        {
          "pk": 1,
          "contents": "또와야지",
          "author": "anohk"
        }
      ]
    }
  ]
}
```

## Pin 삭제

### method

DELETE