# <Git 정리>

맨 처음 vscode 폴더의 위치의 terminal에서 git init 선언

이후 ls -la(os가 숨긴 폴더, 파일 보이기) 실행 시 BOJ 폴더에 .git이 있는 것이 확인 가능함 이는 git init을 통해 생성한 것

.git에는 커밋이나 코드 변경 사항을 저장하는 모든 파일을 실제로 저장

## <Git 원격 저장소 연결>

1. git remote add <저장소 별칭, origin> <원격저장소url>

    <원격저장소url> : 사용자는 sss654654이고 저장소 이름은 BOJ

    git remote add origin https://github.com/sss654654/BOJ.git

    git remote -v 시, 연결한 repositroy가 보임

2. git push <원격 저장소 별칭> <로컬 브랜치>
    git push -u origin master
    로컬 브랜치 이름은 관례적으로 master로 함
    -u는 upstream으로 앞으로 origin main까지 안써도 되도록 함
    즉, 앞으로는 
    1. git add 파일이름 
    2. 2.git commit -m 메시지 
    3. 3.git push (origin master)
   로만 원격 저장소에 저장 가능

# <Github Workflow>

1. 코드 작성

2. commit을 통해 변경사항 저장

3. pull request 생성(이후 설명)

# <Local Git Workflow>

1. 코드 작성

2. git add를 통해 변경사항 추적

3. git commit을 통해 변경사항 저장

4. 코드 변경사항을 git push를 통해 github의 원격 저장소로 push 

5. pull request 생성

## <Git Branching>

웹, 앱을 개발할 시 기능 별로 여러 브랜치를 생성해서 각각의 기능이 구현될 때마다 해당하는 브랜치에 commit

ex) 
master branch : 모든 branch 통합(Merge)
user branch : 로그인, 회원가입, 로그아웃 서비스 구현
homepage branch : 홈페이지 화면 서비스 구현

변경사항을 원하는 branch에 알맞게 commit 해야 함

# branch 명령어

1. local에서 branch 생성, 전환
=> git branch : 현재 폴더의 브랜치를 보여줌
=> git checkout : 새 브랜치 생성 후 전환
=> git checkout -b (새 브랜치 이름) : 새 브랜치 생성 후 전환
=> git checkout (브랜치 이름) : 해당 브랜치로 전환 

2. local에서 github에 새 branch 생성
=> git push -u origin (생성한 브랜치 이름)

3. 수정사항은 git add, git commit으로 저장한 이후 checkout을 통해 변경된 브랜치로 push함 
=> git push origin (변경한 브랜치)

4. 3 이후 github 홈페이지 확인 시 새 브랜치를 다른 브랜치와 비교하여 PULL REQUEST를 생성하고 싶은지 여부를 확인함
=> Compare & pull request 버튼 클릭 후 화살표 인터페이스를 통해 원하는 브랜치로 병합(merge)
ex) 원래 존재하는 브랜치(main) <- 새로 생성한 브랜치(study)

* PULL REQUEST(PR)
: 기본적으로 코드를 다른 브랜치로 가져오도록 요청
즉, 새로 생성한 브랜치에 계속 커밋하다가 마스터 브랜치로 통합해야 할 경우 생성
EX)study 브랜치에서 main 브랜치로 PR을 만듬
EX)planner 브랜치에서 main 브랜치로 PR을 만듬

