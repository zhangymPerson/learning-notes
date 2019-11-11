## powershell的使用


- powershell官方文档

    [官方文档](https://docs.microsoft.com/zh-cn/powershell/)

- [powershell学习网站](https://www.pstips.net/#)

- powershell 中需要打印数据到文件时

    ```powershell
    $log='script-run.log'
    Start-Transcript $log -Append -Force

    cmd

    Stop-Transcript
    ```

- powershell脚本后缀 ps1 表示powershell 1.*版本 避免与ps文件混淆

    如：ps_script.ps1

- powershell脚本注释

    ```powershell
    #单行注释
    # 定义一个计数变量
    $i = 0

    #块注释符、多行注释
    #如下:
    <#
    文件：xxx.ps1
    用途：用于测试的xxx功能脚本
    创建：2019-11-10，zhang
    修改：2019-11-11，danao
    #>

    ```