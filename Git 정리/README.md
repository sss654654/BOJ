#### Change Management

소프트웨어는 지속적으로 변화한다. (개발중에도, 개발후에도) 지속적으로 변화하는 소프트웨어의 변경은 관리되어야한다. 
프로젝트 진행 중 새로운 산출물이 축적되고, 모든 산출물은 버전업된다.
이렇게 변경되는 산출물들을 관리하는 것이 형상관리(configuration management)이다.


#### Git 정리

맨 처음 vscode 폴더의 위치의 terminal에서 git init 선언

이후 ls -la(os가 숨긴 폴더, 파일 보이기) 실행 시 BOJ 폴더에 .git이 있는 것이 확인 가능함 이는 git init을 통해 생성한 것

.git에는 커밋이나 코드 변경 사항을 저장하는 모든 파일을 실제로 저장

<br/>

## Git 원격 저장소 연결

1. git remote add <저장소 별칭, origin> <원격저장소url>

    <원격저장소url> : 사용자는 sss654654이고 저장소 이름은 BOJ

    git remote add origin https://github.com/sss654654/BOJ.git

    git remote -v 시, 연결한 repositroy가 보임

2. git push <원격 저장소 별칭> <로컬 브랜치>
   
    git push -u origin master
    로컬 브랜치 이름은 관례적으로 master로 함
    -u는 upstream으로 앞으로 origin main까지 안써도 되도록 함
    즉, 앞으로는 
    1. git add 파일이름(.를 쓸 경우 모든 파일)
    2. git commit -m 메시지 (git commit 전에는 git status로 먼저 확인!!)
    3. git push (origin master)
   로만 원격 저장소에 저장 가능

<br/>

## Github Workflow

1. 코드 작성

2. commit을 통해 변경사항 저장

3. pull request 생성(이후 설명)

<br/>

## Local Git Workflow

1. 코드 작성 (Working Directory)

2. git add를 통해 변경사항 추적 (Staging Area)

*git diff : Working Directory에서의 변경점 확인. 즉, Staging Area와 차이를 확인하기 위해 사용(다만, git add를 통해 Staging Area로 올라간 변경사항은 git diff로 체크 불가능)

*git diff HEAD : Working Directory와 Staging Area의 변경사항 모두를 Repository의 Head 커밋과 비교

*git diff --staged(cached) : Staging Area와 Repository의 Head 커밋 사이의 변경 사항 확인

*git diff [옵션] [파일이름] : 옵션을 적용한 후 파일이름을 입력하면 해당 파일의 diff만 확인 가능

3. git commit을 통해 변경사항 저장(Repository)

4. 코드 변경사항을 git push를 통해 github의 브랜치(원격 저장소)로 push 

<br/>

## Git Branching

웹, 앱을 개발할 시 기능 별로 여러 브랜치를 생성해서 각각의 기능이 구현될 때마다 해당하는 브랜치에 commit

ex) 

master branch : 기본 branch, 따로 생성한 branch들로 부터 pull request를 받아 통합
study branch : 스터디 서비스 구현
planner branch :  플래너 서비스 구현

변경사항을 원하는 branch에 알맞게 commit 해야 함

<br/>

## branch 명령어(checkout)

1. local에서 branch 생성, 전환
 
=> git branch : 현재 폴더의 브랜치를 보여줌

=> git checkout -b (새 브랜치 이름) : 새 브랜치 생성 후 그 브랜치로 전환

(checkout -b : *detached Head에 브랜치 부여)

=> git checkout (브랜치 이름) : 해당 브랜치로 전환 

*Detached HEAD란?

보통 브랜치(branch)는 특정 커밋(commit)을을 가리키고 HEAD가 이 브랜치를 가리킨다. 이렇게 HEAD -> 브랜치 -> 특정 커밋 순서로 commit을 가리키는 상태를 ‘attached HEAD’ 상태(state)라고 한다. 그리고, Detached HEAD란 HEAD가 브랜치를 통해 간접적으로 commit을 가리키지 않고, 직접 커밋을 가리키는 것을 말한다.

모르는 사이에 detached HEAD가 된 커밋은 브랜치를 따로 만들거나 기존 브랜치에 변경사항을 이동 , git checkout -b (브랜치) or git checkout (브랜치)를 이용!

</br>

1. local에서 github에 새 branch 생성(추가)

=> git push -u origin (생성한 브랜치 이름)

3. 수정사항은 git add, git commit으로 저장한 이후 checkout을 통해 변경된 브랜치로 push함 

=> git push origin (변경한 브랜치)

4. 3 이후 github 홈페이지 확인 시 새 브랜치를 다른 브랜치와 비교하여 PULL REQUEST를 생성하고 싶은지 여부를 확인함

=> Compare & pull request 버튼 클릭 후 화살표 인터페이스를 통해 원하는 브랜치로 병합(merge)
ex) 원래 존재하는 브랜치(main) <- 새로 생성한 브랜치(study)

5. branch 삭제
   
git branch -d (삭제할 브랜치)

* PULL REQUEST(PR)

: 기본적으로 코드를 다른 브랜치로 가져오도록 요청
즉, 새로 생성한 브랜치에 계속 커밋하다가 마스터 브랜치로 통합해야 할 경우 생성

ex)study 브랜치에서 main 브랜치로 PR, 이후 merge

ex)planner 브랜치에서 main 브랜치로 PR, 이후 merge

<br/>

## merge, rebase(두 가지의 브랜치 병합 방법)

merge란?

현재(checkout) 브랜치를 다른 브랜치로 합치는 과정. merge의 기본 단위는 브랜치이며, git merge로 커밋 단위의 병합은 불가

<merge의 종류>

1. Fast Forard Merge

현재 브랜치의 커밋 내용을 병합할 브랜치의 커밋까지 옮기는 작업

다만 이는 두 브랜치가 동일 선상에 놓여있어야 함!!(뒤에 쳐진 브랜치의 참조 개체가 앞서있는 브랜치가 가리키는 개체를 참조하도록 이동)

=> (현재 브랜치에서)$git merge (병합할 브랜치)


2. 3-way merge

base 커밋에서 두 브랜치가 모두 커밋을 진행하여 분기해서 나간 상태의 merge

두 브랜치가 각각의 분기에서 자신의 커밋을 가리키고 있고 git merge 명령을 실행하면 새로운 commit이 생성됨

3-way로 불리는 이유는 각 커밋을 병합할 때 base 커밋과 각 브랜치가 참조하는 2개의 커밋을 기준으로 병합을 진행하기 때문

다만 base에서 분기된 각 브랜치가 똑같은 파일의 똑같은 부분에 대해서 커밋을 한 뒤 병합하려 한다면 충돌(conflict)가 발생함

</br>

<충돌(conflict) ex>

<<<<<< HEAD

[현재 브랜치의 변경 사항]

============================

[merge할 대상 브랜치의 변경 사항]

>>>>>> (대상 브랜치 이름)

=> 위의 충돌을 해결하기 위해서는 <<, ==, >>를 모두 제거 후 선택해야 되는 변경사항만을 택하여 반영한 뒤 merge를 진행함

<br/>

## pull

git checkout (브랜치) 을 통해 가르킬 브랜치로 변경
git pull origin (브랜치)를 이용하여 해당 브랜치에서 로컬로 코드를 업데이트함

<br/>

## branch conflict

여러 사람과 같이 협업하는 경우 다수가 자신의 브랜치에서 master 브랜치로 병합하기 때문에 파일의 conflict(충돌)가 발생함
=> github 사이트는 conflict를 고칠 수 있는 인터페이스를 제거

<br/>

## undoing(의도치 않은 작업)

1. git add를 실수한 경우

    git add Readme.md
    => git reset Readme.md (undo)

2. git commit을 실수한 경우, 또는 커밋이 여러 개인 경우
   
    git commit -m "메세지"
    => git reset HEAD(물결표)1
    
    (HEAD는 마지막 커밋에 대한 포인터, git reset HEAD~1은 내가 방금 만든 커밋을 완전히 취소한다는 의미)


3. git log

시간의 역순으로 모든 커밋의 로그를 확인 가능
=> 스페이스바를 사용하여 아래로 스크롤 가능, q로 빠져나가기

    commit 93bd6a96c89ba7aad194cbc380fd7461a01457fb (HEAD -> main, origin/main)
    Author: sss654654 <zed6740@naver.com>
    Date:   Fri Nov 18 16:09:48 2022 +0900

    git 정리 업데이트ㅎ

    commit c2c45c8c1d8c74289b0d8449428d4f32b5ced823
    Author: sss654654 <zed6740@naver.com>
    Date:   Fri Nov 18 15:01:18 2022 +0900

    git 내용 정리

4. 특정 커밋으로 돌아가고 싶을 때

git log를 통해 보이는 log에서 특정 커밋의 우측 해시 중 하나를 복사

    $git log
    commit c2c45c8c1d8c74289b0d8449428d4f32b5ced823
    Author: sss654654 <zed6740@naver.com>
    Date:   Fri Nov 18 15:01:18 2022 +0900

    git 내용 정리

    => copy c2c45c8c1d8c74289b0d8449428d4f32b5ced823

=> git reset --hard c2c45c8c1d8c74289b0d8449428d4f32b5ced823

<주의!!!>
해당 커밋까지 작성한 모든 기록들이 삭제됨 즉, 파일이 완전히 과거로 돌아감