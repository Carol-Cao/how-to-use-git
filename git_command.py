创建账号，登录账号
git config --global user.name "user"
git config --global user.email "user@name.com"

创建代码仓库，准备文件
Git init 创建git仓库
创建readme.txt
更新文件到仓库
使用命令 git add readme.txt添加到暂存区里面去
git commit告诉Git，把文件提交到仓库
查看状态或区别
git status来查看是否还有文件未提交
git diff readme.txt 看下readme.txt文件到底改了什么内容

查看历史记录版本号
git log查看下历史记录
git log –pretty=oneline
git reflog  查看版本号

回退版本
git reset --hard HEAD^  返回上个版本
git reset --hard HEAD^^返回上上个版本
git reset --hard~100   退到前100个版本
git reset --hard 版本号

撤销修改
git restore <filename>
git checkout --readme.txt 意思就是，把readme.txt文件在工作区做的修改全部撤销

删除文件以及撤销删除
rm 删除文件
git checkout -- 


生成public key 和 pravite key
ssh-keygen -t rsa –C “youremail@example.com”

添加github库到本地
git clone github地址


git到github
git push orinit master

github 拉取文件
git pull oginit master


git account
carol-cao
Chh




工作区：
就是你在电脑上看到的目录，比如目录下testgit里的文件(.git隐藏目录版本库除外)。或者以后需要再新建的目录文件等等都属于工作区范畴。
版本库(Repository)：
工作区有一个隐藏目录.git,这个不属于工作区，这是版本库。其中版本库里面存了很多东西，其中最重要的就是stage(暂存区)，还有Git为我们自动创建了第一个分支master,以及指向master的一个指针HEAD。

我们前面说过使用Git提交文件到版本库有两步：

第一步：是使用 git add 把文件添加进去，实际上就是把文件添加到暂存区。

第二步：使用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支上。
