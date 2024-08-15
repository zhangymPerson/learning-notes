#!/bin/bash

# 定义颜色变量
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# 定义帮助信息
usage() {
    echo "Usage: $0 [command]"
    echo "Available commands:"
    echo "  start      Start the services defined in docker-compose.yml"
    echo "  stop       Stop the services defined in docker-compose.yml"
    echo "  logs       View the logs of the services"
    echo "  help       Show this help message"
}

# 检查是否提供了足够的参数
if [ "$#" -ne 1 ]; then
    usage
    exit 1
fi

# 主要逻辑
case $1 in
    start)
        echo -e "${GREEN}Starting services...${NC}"
        docker compose up -d
        ;;
    stop)
        echo -e "${GREEN}Stopping services...${NC}"
        docker compose down
        ;;
    logs)
        echo -e "${GREEN}Viewing service logs...${NC}"
        docker compose logs --follow
        ;;
    help)
        usage
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        usage
        ;;
esac