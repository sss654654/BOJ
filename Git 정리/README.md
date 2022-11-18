### BOJ 알고리즘 문제풀이

<br/>
<br/>
<br/>
<br/>

Git 정리

git 원격 저장소 연결

git init

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
    3. 3.git push
   로만 원격 저장소에 저장 가능

ls -la(os가 숨긴 폴더, 파일 보이기) 실행 시 BOJ 폴더에 .git이 있는 것이 확인 가능함 이는 git init을 통해 생성한 것

.git에는 커밋이나 코드 변경 사항을 저장하는 모든 파일을 실제로 저장