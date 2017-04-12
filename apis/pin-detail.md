| Resource     | GET       | POST | PATCH      | DELETE  |
| ------------ | --------- | ---- | ---------- | ------- |
| /pin/{pinId} | 해당 핀 세부정보 |      | 해당 핀 정보 수정 | 해당 핀 삭제 |

<<<<<<< HEAD
=======
## Pin 세부정보 조회

>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34
### 요청 주소

`/pin/{pinId}`

<<<<<<< HEAD
## Pin 세부정보 조회

=======
>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34
### method

GET

### 반환

```
{
<<<<<<< HEAD
  "pk": 1,
  "author": "anohk",
  "name": "루카루",
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

> `name`은 `pin_name`으로 변경될 예정입니다.

## Pin 세부정보 수정

=======
    "pk": "3",
    "author": "kay",
    "name": "패캠 카페",
    "place": 2,
    "map": 4,
    "pin_color": "0,0,0"
}
```

## Pin 세부정보 수정

### 요청 주소

`/pin/{pinId}`

>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34
### method

PATCH

### body
<<<<<<< HEAD
다음 중 하나 이상의 값을 받습니다  

- name
- place
- map
- pin_color

```
{
    "name": "스터디카페",
=======

```
{
    "name": "바실",
>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34
}
```

### 반환

```
{
<<<<<<< HEAD
  "pk": 1,
  "author": "anohk",
  "name": "스터디카페",
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
=======
    "pk": "3",
    "author": "kay",
    "name": "바실",
    "place": 2,
    "map": 4,
    "pin_color": "0,0,0"
>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34
}
```

## Pin 삭제

<<<<<<< HEAD
=======
### 요청 주소

`/pin/{pinId}`

>>>>>>> 9549e77e500331f94b7e6ce91784ded3bb8fec34
### method

DELETE