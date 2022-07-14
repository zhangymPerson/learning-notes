# git 的使用笔记

## 目录

- [返回](../README.md)

## 其他

- 学习网站

  https://git-scm.com/book/zh/v2

## git 结构图

![git的各个存储位置图](../../Picture/git%E7%9A%84%E5%90%84%E4%B8%AA%E5%AD%98%E5%82%A8%E4%BD%8D%E7%BD%AE%E5%9B%BE.png)

## git 相关命令

![git命令](../../Picture/git%E5%91%BD%E4%BB%A4.png)

- [git 使用教程](https://github.com/firstcontributions/first-contributions/blob/master/README.md)

## git 与 svn 对比

最核心的区别就是**Git 是分布式的， SVN 是集中式的。**

**SVN 必须有一个服务器版本库就放在一个中央服务器。**

所有开发人员都是与服务器进行交互的。

开发流程 -> 从中央服务器得到最新的版本 -> 开发 -> 把自己做的工作推送到中央服务器。

Git 不需要有中心服务器，

Git 更倾向于分布式开发，每台计算机上都有一个完整的本地版本库。和服务器上的一模一样。

## git 分支的理解

git 有一个主分支 master

可以创建多个分支 并且 任意命名

可以任意合并两个分支

分支之间无任何父子关系， 之所以有 dev-等分支 是人为约定， 任何分支可以不合并到主分支 可以随便切换所需分支

开发组可以定义自己的分支之间逻辑，但是在 git 层面上，所有分支之间无特定关系 都是平级的

## tag

git 的 tag 是标签 给项目打一个标签号

如 给当前版本打个标签 `git tag -a v0.1 -m "version 0.1 released"`
