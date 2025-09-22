# https://just.systems

default:
    @just --list

# 拉取代码
pull:
    git fetch --all --tags --prune --jobs=10
    git pull --rebase

push:
    git push origin "$(git branch --show-current)"
    git push gitee "$(git branch --show-current)"