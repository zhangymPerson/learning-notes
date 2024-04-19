# vimium

- 介绍

  Vimium 是一个 Chrome 插件，它允许你用 Vim 键位来操作浏览器。

  [github](https://github.com/philc/vimium)

- 安装

  - 下载插件 (chrome 插件库)
  - 添加到 浏览器中
  - 配置

- 自定义配置

  在 `Custom key mappings` 中添加

  ```vimrc
  map j scrollPageDown
  map k scrollPageUp
  map T createTab
  map t Vomnibar.activateTabSelection
  map h previousTab
  map l nextTab
  map J scrollToBottom
  map K scrollToTop
  ```

  在 `Custom search engines` 中添加

  ```
  g: https://www.google.com/search?q=%s Google
  b: https://www.baidu.com/s?wd=%s Baidu
  gh: https://github.com/search?q=%s&type=repositoriesGitHub Github
  bing: https://www.bing.com/search?q=%s Bing
  # 其他自定义的
  ```
