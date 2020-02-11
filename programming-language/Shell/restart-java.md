# 重启Java项目的简单脚本

```sh
#-------------------------------------------------------------------#
#                                                                   #
#                                                                   #
#                       更新代码 重启服务                           #
#                                                                   #
#                                                                   #
#-------------------------------------------------------------------#

start=`date +%Y%m%d%H%M`
# 项目位置
file=/home/user/projectname
#备份jar包位置
back_file=/home/user/backup

#jar包名

jar_name=jarname

echo ${start} " info : 开始重启服务"
cd ${file}
echo "=================================更新代码============================="
svn update --username username --password password
echo "================================更新完成=============================="
echo "===============================开始构建项目============================"
mvn clean package -Dmaven.test.skip=true
echo "==============================备份jar包==============================="
now=`date +%Y%m%d%H%M`
$(cp ${file}/target/${jar_name}.jar ${back_file}/${jar_name}_${now}.jar)
echo "备份  ${file}/target/${jar_name}.jar  到  ${back_file}/${jar_name}_${now}.jar位置"
echo "=============================开始重启服务器============================="
# 停止脚本 需自定义实现
sh stop-jar.sh
# 启动脚本 
sh start-jar.sh

end=`date +%Y%m%d%H%M`
echo ${end} " info : 重新启动服务成功"
```