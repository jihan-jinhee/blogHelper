# blogHelper
### 일부 유료 기능은 잠겨 있습니다. 문의 (e-mail: hanjinhee502@naver.com).
### 현재 개발, 유지보수 중단되어 대응에 오랜 시간이 걸리고 있습니다.

## 네이버 블로그 활동을 보조하는 목적으로 만든 프로그램
![image](https://user-images.githubusercontent.com/74603608/216958726-9dbee74b-0ed8-471d-b428-d601ae890ff5.png)

### 기능
* 사진에 워터마크 추가 (본인 전용. 타 워터마크 지원 X)
* [댓글 확인](https://github.com/jihan-jinhee/blogHelper/blob/master/README.md#%EB%8C%93%EA%B8%80-%ED%99%95%EC%9D%B8-%EA%B8%B0%EB%8A%A5)
* [이웃 글 방문](https://github.com/jihan-jinhee/blogHelper/blob/master/README.md#%EC%9D%B4%EC%9B%83-%EA%B8%80-%EB%B0%A9%EB%AC%B8)
* [글자수세기](https://github.com/jihan-jinhee/blogHelper/blob/master/README.md#%EA%B8%80%EC%9E%90%EC%88%98%EC%84%B8%EA%B8%B0)
* [미방문이웃 확인 & 삭제](https://github.com/jihan-jinhee/blogHelper/blob/master/README.md#%EB%AF%B8%EB%B0%A9%EB%AC%B8%EC%9D%B4%EC%9B%83-%ED%99%95%EC%9D%B8-%EA%B8%B0%EB%8A%A5)
* [이웃 추가](https://github.com/jihan-jinhee/blogHelper/blob/master/README.md#%EC%9D%B4%EC%9B%83-%EC%B6%94%EA%B0%80-%EA%B8%B0%EB%8A%A5)

## 메뉴바
![image](https://user-images.githubusercontent.com/74603608/216959070-af879fef-1a9f-4814-be97-5a9b0ae68020.png)

---

* 자동 로그인 설정

![image](https://user-images.githubusercontent.com/74603608/216960039-160fa0f8-38f5-4d62-a9d5-54423ba0f956.png)

![image](https://user-images.githubusercontent.com/74603608/216960328-40ffad19-d01e-423e-9e83-87b205f14115.png)

체크되어 있으면 네이버 자동 로그인 기능함.

![image](https://user-images.githubusercontent.com/74603608/216960221-823d941d-7861-4e85-99f1-9f0864295862.png)

---

* 댓글 문구 설정

![image](https://user-images.githubusercontent.com/74603608/216960369-e5a15d05-4585-411a-9b52-df11642ea5a1.png)

체크되어 있으면 기본 댓글이 아닌, 사용자 정의 댓글 남김.

![image](https://user-images.githubusercontent.com/74603608/216960403-74358cc8-fce3-4fe4-85b7-db4e03fec5c0.png)

# 워터마크 기능 (생략)

# 댓글 확인 기능
![image](https://user-images.githubusercontent.com/74603608/216961899-2f159a7a-2c79-43ba-a607-4c20c1e3a5dd.png)

댓글을 확인할 게시글 URL 복사

![image](https://user-images.githubusercontent.com/74603608/216962078-9bef8392-13f9-469b-b3c0-0bc898cb59de.png)

URL 입력 후 실행

![image](https://user-images.githubusercontent.com/74603608/216962242-375b3852-dbf5-49f9-8de6-d6cdbeafdbed.png)

댓글 중, 내가 읽지 않은 댓글을 확인(좋아요로 구분)
좋아요를 누르고, 해당 블로그의 최신 게시물로 이동.
게시물 좋아요를 누르고, 댓글을 남깁니다.
(*그 게시물을 읽었는지 유무는 내가 좋아요 체크를 예전에 했었는가)

![image](https://user-images.githubusercontent.com/74603608/216962565-69523176-5151-4b04-96b0-9053d1f7e744.png)

# 이웃 글 방문
* 이웃이 1명이라도 있어야 합니다. (권장 1000명 이상이라.. 하루 1~2번 돌릴 용으로 개발)
* 이웃이 너무 적을 경우, 자동 종료가 안될 수 있습니다. 프로그램이 멈춰있다 싶으면 수동 종료해주세요.


![image](https://user-images.githubusercontent.com/74603608/216962730-dbbc4088-121c-484d-bb1e-831926224a15.png)

시작하면 멈출 수 없습니다. (230206 기준)

![image](https://user-images.githubusercontent.com/74603608/216962908-94be9662-1a39-4d30-9e33-3ee529847dd5.png)

모든 이웃들 글을 읽으면서 좋아요 + 자동댓글.
(*이것도 내가 읽었는지 유무를 좋아요 체크가 되었나로 판단)


# 글자수세기
게시물 글자수 세주는 프로그램 (협찬용 등 게시물 글자수 제한 조건 확인할 떄)

![image](https://user-images.githubusercontent.com/74603608/216963035-ee71e024-7edf-42f3-9bd3-66401870321a.png)

포스팅 에디터 열기

![image](https://user-images.githubusercontent.com/74603608/216963060-424c710c-f10e-49c1-89f9-904d0913332f.png)

블로그 에디터에서 글 복사 Ctrl+A(전체 선택), ctrl+C(복사)

![image](https://user-images.githubusercontent.com/74603608/216963081-98e8256e-2d1f-4f04-a601-2aa0bd639370.png)

ctrl+V(붙여넣기)
총 글자수와, 순수 글자수(사진, 영상 등을 제외한 글자)가 나옴.

# 미방문이웃 확인& 기능

1. .opml 파일 추출. (블로그 관리, 열린이웃-이웃 그룹관리-이웃그룹-검사할그룹선택-내보내기)

![image](https://user-images.githubusercontent.com/74603608/216963614-cb6a15d2-95df-4f5e-a8cd-9891feefb2dc.png)

(삭제를 원하지 않는 그룹은 체크 제외)

2. Opml 파일 선택

![image](https://user-images.githubusercontent.com/74603608/216963689-513739bb-2246-48a6-a243-3b9b6f2369f0.png)

3. Opml 파일에 쓰여 있는 이웃들이, 최신 포스팅에 좋아요를 눌렀는지 검사. (예시에는 최근 5개 게시물 확인,)

![image](https://user-images.githubusercontent.com/74603608/216964143-dff3f51b-54ee-4a63-9fbc-6f92bb69e69d.png)

(아직 한달미만이웃제외 기능 미구현)

4. 검사가 완료되면 result 폴더에, 처단을 추천하는 user 목록이 뜸

![image](https://user-images.githubusercontent.com/74603608/216964008-4b3f8815-4d8c-40d2-91fe-6ccbdd4a6765.png)

5. 미방문 이웃 삭제 가능

![image](https://user-images.githubusercontent.com/74603608/216964241-4ae2f6fd-b8fe-480a-9ac6-61583d656f05.png)

   * 완전 삭제를 원하면, 추후 직접 삭제해주어야 함.
   ![image](https://user-images.githubusercontent.com/74603608/216964547-5bf946a1-dc3b-4418-baec-68b628a9bb38.png)

# 이웃 추가 기능

* 사전 작업으로, 이웃 그룹을 생성해주어야 합니다.

![image](https://user-images.githubusercontent.com/74603608/220338556-3ffcac43-93d4-4039-b491-c39f398a6edc.png)

1. 네이버 블로그로 이동해서, 관리 페이지에 들어갑니다.

![image](https://user-images.githubusercontent.com/74603608/220338798-edc891ef-10b1-4a0b-8a2b-743b3c09125d.png)

2. 관리 - 기본 설정 - 열린 이웃 - 이웃그룹관리에 들어갑니다.

![image](https://user-images.githubusercontent.com/74603608/220338949-f47f320d-9289-4d17-9bd0-02ea08248184.png)

3. 이웃그룹 - +그룹추가를 누릅니다.

![image](https://user-images.githubusercontent.com/74603608/220339096-f3f8a1dd-de70-4609-b861-d72d81e30973.png)

4. 그룹을 추가합니다. 이름, 공개 설정은 자유입니다.

![image](https://user-images.githubusercontent.com/74603608/220339170-0d893615-fccd-4bc5-94ed-31f8a8a61e07.png)

5. 그룹이 만들어지면, 이 그룹에 서로이웃들을 추가하게 됩니다.

![image](https://user-images.githubusercontent.com/74603608/220339998-5531c379-c537-481b-adf1-bddc86507899.png)

6. 그룹이 많으면, 제일 상단에 있는 그룹에만 이웃을 추가하게 됩니다.

![image](https://user-images.githubusercontent.com/74603608/220340149-7b4a0659-01f6-490e-ad0e-faffd89cd07d.png)

7. 이웃 그룹당, 인원 제한이 있습니다(500명). 따라서, 500명이 되어 더 이상 이웃 추가가 되지 않는다면,
   그룹 순서를 변경해주어야 합니다.


### 이웃 추가 기능 설명

![image](https://user-images.githubusercontent.com/74603608/216964803-e4f21860-7990-42a0-b581-194dc96bc36b.png)

게시물을 좋아요 한 계정들에게 서로이웃신청을 보내게 됩니다.
따라서, 좋아요가 많은 포스팅의 URL을 입력하는 것이 유리합니다.

![image](https://user-images.githubusercontent.com/74603608/216964992-958832dd-76a7-488a-8187-462ef7955cd3.png)

이렇게, 게시물을 좋아요 누른 인원들에게 서로이웃 신청을 보내게 됩니다.
(단, 네이버에서 막아놓은 하루 신청 제한에 도달하면 중지됩니다.)

### 서로이웃 신청이 진행되었나 확인 방법
![image](https://user-images.githubusercontent.com/74603608/220340376-1d21f4be-a38d-4071-a1fd-56a5166877ea.png)

블로그 관리 - 기본 설정 - 열린 이웃 - 서로이웃 신청 - 보낸 신청
에서 확인 가능합니다.
요청이 승인되야, 최종적으로: 열린 이웃 - 이웃그룹관리에 서로이웃이 추가됩니다.



