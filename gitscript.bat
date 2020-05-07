@echo off
rem git切换脚本
call:gitcheckout dev
call:gitmerge person
call:gitcheckout master
call:gitmerge dev
call:gitcheckout person
exit

rem 切换分支
:gitcheckout
git checkout %1
goto:eof

rem 合并分支
:gitmerge
git merge %1
goto:eof