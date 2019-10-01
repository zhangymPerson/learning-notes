## powershell的使用

- [powershell学习网站](https://www.pstips.net/#)

- powershell中需要打印数据到文件时

    ```powershell
    $log='script-run.log'
    Start-Transcript $log -Append -Force

    cmd

    Stop-Transcript
    ```