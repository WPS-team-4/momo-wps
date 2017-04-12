| Resource                                 | GET         | POST   | PATCH        | DELETE    |
| ---------------------------------------- | ----------- | ------ | ------------ | --------- |
| /post/                                   | 포스트 리스트     | 포스트 생성 |              |           |
| /post/{postId}/                          | 해당 포스트 세부정보 |        | 해당 포스트 정보 수정 | 해당 포스트 삭제 |
| /post/{postId}/comment/add/              |             | 코멘트 생성 |              |           |
| /post/{postId}/comment/{commentId}/delete/ |             |        |              | 코멘트 삭제    |

## Post 리스트 조회

### 요청 주소

`/api/post/`

### method

GET

### 반환

## Post 생성

### 요청 주소

`/api/pin/`

### method

POST

### 반환