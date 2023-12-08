# windows 的包管理工具

## 地址

- [github](https://github.com/microsoft/winget-cli)

- [官网](https://learn.microsoft.com/zh-cn/windows/package-manager/)

## 配置

- 修改为本地源

  ```shell
  # 默认地址 https://cdn.winget.microsoft.com/cache
  winget source remove winget
  winget source add winget https://mirrors.ustc.edu.cn/winget-source
  ```

### 使用

- 查找软件包

  `winget search openjdk`
