 <!--git 笔记  -->

 <!-- git 是什么 -->
 Git 是版本控制工具，用以记录代码每次修改

======== 第一次提交的操作 ========

 <!-- git init -->
 作用：把当前文件夹变成 Git 仓库（项目刚开始时调用）
 语法：git init

<!-- git config user.name / user.email -->
作用：设置提交者的姓名和邮箱（项目刚开始时调用一次）
语法：git config --global user.name "姓名"
git config --global user.email "邮箱"   

<!-- git remote add origin URL -->
作用：把本地仓库连接到远程仓库（项目刚开始时调用一次）
语法：git remote add origin <远程仓库 URL>(如:https://github.com/用户名/项目名.git)

<!-- git branch -M main -->
作用：把当前分支重命名为 main（项目刚开始时调用一次）
语法：git branch -M <分支名>(如:main)

======== 第一次提交的操作 ========



======== 每次修改代码后重复执行 ========

<!-- git add . -->
作用：把修改的文件加入到“暂存区”
语法：git add .

<!-- git status -->
作用：查看当前仓库的状态（查看修改的文件、暂存区、已提交文件）  
语法：git status

<!-- git commit -m "对这个文件的描述" -->
作用：提交修改（把暂存区的文件提交到仓库）
语法：git commit -m "对这个文件的描述"    

<!-- git push -->
作用:把当前文件的修改提交到Github仓库
语法：git push

======== 每次修改代码后重复执行 ========



<!-- git log --oneline -->
作用：查看提交记录（以一行显示每个提交记录）
语法：git log --oneline 

<!-- git show -->
作用：查看当前提交的详细信息（包括提交者、提交时间、提交信息等）
语法：git show <提交哈希值>(如:git show 1234567890abcdef1234567890abcdef1234567890)



