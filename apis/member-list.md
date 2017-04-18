# member-list

> 옵션별로 정렬한 사용자 목록을 반환합니다.



### URL

`/api/member/`



### Method

`GET`



### Headers

`Authorization : token [token_value]`



### URL Params

| name  |     value     |             type             |
| :---: | :-----------: | :--------------------------: |
| field |      pk       |                              |
|       |   username    |                              |
|       |   password    |                              |
|       |     email     |                              |
|       |   map_list    |                              |
|  opt  | most_follower |   팔로워가 가장 많은 순서대로 유저목록을 반환   |
|       |   most_maps   | 생성한 지도가 가장 많은 순서대로 유저 목록을 반환 |






### Success Response

- Code: 200
- Content:

- `{{host}}/api/member/?fields=pk,username,email?opt=most_follower`


```
{
  "count": 14,
  "next": "http://127.0.0.1:8000/api/member/?fields=pk%2Cusername%2Cemail&opt=most_follower&page=2",
  "previous": null,
  "results": [
    {
      "pk": 34,
      "username": "superkiz7",
      "email": "superkiz5@momo.com"
    },
    {
      "pk": 10,
      "username": "adminkiz",
      "email": "123123@momo.com"
    },
    {
      "pk": 30,
      "username": "superkiz3",
      "email": ""
    },
    {
      "pk": 33,
      "username": "superkiz6",
      "email": "superkiz5@momo.com"
    },
    {
      "pk": 32,
      "username": "superkiz5",
      "email": "superkiz5@momo.com"
    }
  ]
}
```

- `no params`

```
{
  "count": 14,
  "next": "http://127.0.0.1:8000/api/member/?page=2",
  "previous": null,
  "results": [
    {
      "pk": 35,
      "username": "testkizmo",
      "password": "pbkdf2_sha256$30000$G3OLh0YNcfxL$k5vlP73O5SAzxYkDsLuyBwXFTj4zV19f2Aq1/1vPWdg=",
      "email": "superkiz5@momo.com",
      "profile_img": "http://127.0.0.1:8000/media/member/img1_GUbEg0M.jpg",
      "relation_user_set": [],
      "date_joined": "2017-04-14T15:09:07.132277Z",
      "last_login": null,
      "is_facebook": false,
      "is_active": true,
      "is_staff": false,
      "is_superuser": false,
      "map_list": [
        {
          "id": 1,
          "author": {
            "pk": 35,
            "username": "testkizmo",
            "profile_img": "http://127.0.0.1:8000/media/member/img1_GUbEg0M.jpg"
          },
          "pin_list": [],
          "map_name": "지도1",
          "description": "설명1",
          "created_date": "2017-04-15T01:50:40.132357Z",
          "updated_date": "2017-04-17T13:13:03.086724Z",
          "is_private": false
        },
        {
          "id": 2,
          "author": {
            "pk": 35,
            "username": "testkizmo",
            "profile_img": "http://127.0.0.1:8000/media/member/img1_GUbEg0M.jpg"
          },
          "pin_list": [
            {
              "pk": 1,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:56.838371Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 2,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:57.673291Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 3,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:58.311011Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 4,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:58.867878Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 5,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:59.188629Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 6,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:59.409685Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 7,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:59.628068Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 8,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:05:59.840403Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 9,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:00.014384Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 10,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:00.201671Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 11,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:00.363339Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 12,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:00.526253Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 13,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:00.685469Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 14,
              "map": 2,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:00.852910Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            }
          ],
          "map_name": "지도2",
          "description": "설명2",
          "created_date": "2017-04-15T01:50:46.282086Z",
          "updated_date": "2017-04-17T13:13:03.086724Z",
          "is_private": false
        },
        {
          "id": 3,
          "author": {
            "pk": 35,
            "username": "testkizmo",
            "profile_img": "http://127.0.0.1:8000/media/member/img1_GUbEg0M.jpg"
          },
          "pin_list": [],
          "map_name": "지도3",
          "description": "설명3",
          "created_date": "2017-04-15T01:50:52.652704Z",
          "updated_date": "2017-04-17T13:13:03.086724Z",
          "is_private": false
        },
        {
          "id": 4,
          "author": {
            "pk": 35,
            "username": "testkizmo",
            "profile_img": "http://127.0.0.1:8000/media/member/img1_GUbEg0M.jpg"
          },
          "pin_list": [
            {
              "pk": 15,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:06.044952Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 16,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:06.243196Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 17,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:06.412109Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 18,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:06.586335Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 19,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:06.747785Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 20,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:06.924227Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 21,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:07.100546Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 22,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:07.259240Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 23,
              "map": 4,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:07.444746Z",
              "author": "testkizmo",
              "place": 1,
              "post_list": []
            }
          ],
          "map_name": "지도4",
          "description": "설명4",
          "created_date": "2017-04-15T01:50:58.196601Z",
          "updated_date": "2017-04-17T13:13:03.086724Z",
          "is_private": false
        }
      ]
    },
    {
      "pk": 36,
      "username": "kizmo1122",
      "password": "pbkdf2_sha256$30000$FkGA7r5GQUiI$57JgVcSmVDleLc9VkgvdbALQB+0nr1UaY0nw8hdFgQw=",
      "email": "superkiz@momo.com",
      "profile_img": "http://127.0.0.1:8000/media/member/fsociety_6PacNLm.png",
      "relation_user_set": [],
      "date_joined": "2017-04-16T18:35:15.871913Z",
      "last_login": null,
      "is_facebook": false,
      "is_active": true,
      "is_staff": false,
      "is_superuser": false,
      "map_list": []
    },
    {
      "pk": 37,
      "username": "1888023274813222",
      "password": "1888023274813222",
      "email": "",
      "profile_img": null,
      "relation_user_set": [],
      "date_joined": "2017-04-16T19:22:44.404348Z",
      "last_login": null,
      "is_facebook": false,
      "is_active": true,
      "is_staff": false,
      "is_superuser": false,
      "map_list": []
    },
    {
      "pk": 38,
      "username": "kizmo17",
      "password": "pbkdf2_sha256$30000$hF96VIJ9xYW1$zF2uRslhr8siDMhS69lmZxeylcrRJHOQov/+wDP8TD0=",
      "email": "superkiz@momo.com",
      "profile_img": null,
      "relation_user_set": [],
      "date_joined": "2017-04-17T13:05:26.519121Z",
      "last_login": null,
      "is_facebook": false,
      "is_active": true,
      "is_staff": false,
      "is_superuser": false,
      "map_list": []
    },
    {
      "pk": 34,
      "username": "superkiz7",
      "password": "!Rhu8RqbZn5A5MdJt29bZtuYGlMCa1coJFVK0bzgU",
      "email": "superkiz5@momo.com",
      "profile_img": "http://127.0.0.1:8000/media/member/img2_5F9JccF.gif",
      "relation_user_set": [
        35,
        28,
        32,
        33
      ],
      "date_joined": "2017-04-14T14:34:47.345725Z",
      "last_login": null,
      "is_facebook": false,
      "is_active": true,
      "is_staff": false,
      "is_superuser": false,
      "map_list": [
        {
          "id": 5,
          "author": {
            "pk": 34,
            "username": "superkiz7",
            "profile_img": "http://127.0.0.1:8000/media/member/img2_5F9JccF.gif"
          },
          "pin_list": [
            {
              "pk": 24,
              "map": 5,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:10.868452Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 25,
              "map": 5,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:11.365070Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            }
          ],
          "map_name": "다른 지도4",
          "description": "설명4",
          "created_date": "2017-04-15T01:54:00.014065Z",
          "updated_date": "2017-04-17T13:13:03.086724Z",
          "is_private": false
        },
        {
          "id": 6,
          "author": {
            "pk": 34,
            "username": "superkiz7",
            "profile_img": "http://127.0.0.1:8000/media/member/img2_5F9JccF.gif"
          },
          "pin_list": [
            {
              "pk": 26,
              "map": 6,
              "pin_name": "*_*",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:06:14.389895Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 27,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:28.975104Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 28,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:29.169151Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 29,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:29.366891Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 30,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:29.568959Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 31,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:29.763252Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 32,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:29.941300Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 33,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:30.141833Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 34,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:30.339845Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 35,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:30.719075Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 36,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:30.901139Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 37,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:31.065429Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 38,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:31.243930Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 39,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:31.433000Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 40,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:31.594402Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 41,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:31.776383Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 42,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:31.963741Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 43,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:32.144630Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 44,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:32.344488Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 45,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:32.538744Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 46,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:32.721337Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 47,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:32.916203Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 48,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:33.103302Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 49,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:33.275664Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 50,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:33.442420Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 51,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:33.614089Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 52,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:33.791672Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 53,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:33.968280Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 54,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:34.145964Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 55,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:34.328242Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 56,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:34.496371Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 57,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:34.677834Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 58,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:34.847668Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 59,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:35.032263Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 60,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:35.216773Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 61,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:35.392602Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 62,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:35.584978Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 63,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:35.753104Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 64,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:35.938348Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 65,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:36.120496Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 66,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:36.291259Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 67,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:36.472299Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 68,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:36.645633Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 69,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:36.810827Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 70,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:36.977924Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 71,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:37.154307Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 72,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:37.319381Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 73,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:37.483020Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 74,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:37.655783Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 75,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:37.824721Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 76,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:37.993011Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 77,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:38.161998Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            },
            {
              "pk": 78,
              "map": 6,
              "pin_name": "핀",
              "pin_color": "0,0,0",
              "created_date": "2017-04-15T02:20:38.341033Z",
              "author": "superkiz7",
              "place": 1,
              "post_list": []
            }
          ],
          "map_name": "지도4",
          "description": "설명4",
          "created_date": "2017-04-15T01:54:06.170745Z",
          "updated_date": "2017-04-17T13:13:03.086724Z",
          "is_private": false
        },
        {
          "id": 7,
          "author": {
            "pk": 34,
            "username": "superkiz7",
            "profile_img": "http://127.0.0.1:8000/media/member/img2_5F9JccF.gif"
          },
          "pin_list": [],
          "map_name": "지도6",
          "description": "설명6",
          "created_date": "2017-04-15T01:54:11.959200Z",
          "updated_date": "2017-04-17T13:13:03.086724Z",
          "is_private": false
        }
      ]
    }
  ]
}
```

      

### Error Response

- Code:401




