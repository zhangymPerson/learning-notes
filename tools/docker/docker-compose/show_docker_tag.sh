#!/bin/env bash

###########################################################
# @file : show_docker_tag.sh
# @desc : 脚本执行方式 [bash show_docker_tag.sh]
#         脚本说明:
# @date : 2022-07-15 14:05:19
# @auth : test
# @version : 1.0
###########################################################

function name() {
    for Repo in $*; do
        url="https://registry.hub.docker.com/v2/repositories/library/${Repo}/tags/"
        echo "版本获取链接[${url}]"
        curl -s -S ${url} |
            sed -e 's/,/,\n/g' -e 's/\[/\[\n/g' |
            grep '"name"' |
            awk -F\" '{print $4;}' |
            sort -fu |
            sed -e "s/^/${Repo}:/"
    done
}

main() {
    echo "获取[$*]版本"
    name $*
    exit 0
}
main "$@"
