# git 提交注释规范

## commit message

- Angular 规范

  每次提交，Commit message 都包括三个部分：Header，Body 和 Footer。

  ```xml
  <type>(<scope>): <subject>
  // 空一行
  <body>
  // 空一行
  <footer>
  ```

  - type

    feat：新功能（feature）

    fix：修补 bug

    docs：文档（documentation）

    style： 格式（不影响代码运行的变动）

    refactor：重构（即不是新增功能，也不是修改 bug 的代码变动）

    test：增加测试

    chore：构建过程或辅助工具的变动

  - scope

    scope 用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。

  - subject

    subject 是 commit 目的的简短描述，不超过 50 个字符。

          以动词开头，使用第一人称现在时，比如change，而不是changed或changes
          第一个字母小写
          结尾不加句号（.）

  - Body

    Body 部分是对本次 commit 的详细描述，可以分成多行

  - Footer

    只用于两种情况。

    - 不兼容变动

      如果当前代码与上一个版本不兼容，则 Footer 部分以 BREAKING CHANGE 开头，后面是对变动的描述、以及变动理由和迁移方法。

    - 如果当前 commit 针对某个 issue，那么可以在 Footer 部分关闭这个 issue 。

            Closes #234

      也可以一次关闭多个 issue 。

            Closes #123, #245, #992

  - Revert

    还有一种特殊情况，如果当前 commit 用于撤销以前的 commit，则必须以 revert:开头，后面跟着被撤销 Commit 的 Header。

          revert: feat(pencil): add 'graphiteWidth' option
          This reverts commit 667ecc1654a317a13331b17617d973392f415f02.


        Body部分的格式是固定的，必须写成This reverts commit hash.，其中的hash是被撤销 commit 的 SHA 标识符。

- 插件

  安装 npm

  安装插件

  npm install -g commitizen

  使用插件

  cd 到.git 所在目录

  commitizen init cz-conventional-changelog --save --save-exact

  用 git cz 命令来取代 git commit

* 本项目中常用提交规范实例

  docs(笔记文件名): 修改笔记的内容
