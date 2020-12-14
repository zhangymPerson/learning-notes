# vim 操作中遇到的问题

- xshell/shell 命令行中操作的界面卡死

  由于习惯`ctrl + s` 来保存文件，所以 linux 下 也会使用此快捷键

  本质是 shell 界面按下 `ctrl+s` 后，页面被锁定，不能继续更改 需要按下 `ctrl + q` 进行解锁 与 vim 无关

- vim(windows 的 gvim) 出现 在插入模式下 `delete/backspce`键失效 问题

  解决方案 `set backspace=2`
