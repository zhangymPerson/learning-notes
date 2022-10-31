#!/bin/bash

# exec > script.log

# 执行各个脚本
# c ++
path=$(pwd)
# echo ${path}
g++ ${path}/cpp-list.cpp && ${path}/a.out && rm ${path}/a.out

# php
php ${path}/php-list.php
