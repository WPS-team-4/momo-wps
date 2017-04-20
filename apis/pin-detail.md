# Pin Detail view

>



### URL

`/api/pin/{pin_pk}`



### Headers

`Authorization : token [token_value]`



### Method

`GET`



### Success Response

* Code:200 OK
* Content:

```json
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



### Error Response

* Code:
* Reason:
* Content:

```json
{
  
}
```


<<<<<<< HEAD
=======
- name
- map(map의 pk값)
- pin_label
>>>>>>> 88772c41520ee44574885fdaab53202bf9d71215

___



# Pin Detail update(partial)

>



### Method

`PATCH`



### Body

| name      | value       | process |
| --------- | ----------- | ------- |
| name      | 핀 이름        |         |
| map       | map_pk      |         |
| pin_label | 핀 라벨 값[0-4] |         |



### Success Response

* Code:
* Content:

```json
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



### Error Response

* Code:
* Reason:
* Content:

```json
{
  
}
```



___



# Pin Delete

### Method

`DELETE`



### Success Response

* Code:
* Content:

```json

```



### Error Response

* Code:
* Reason:
* Content:

```json

```

