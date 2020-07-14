echo "#-------------------------------------------------------------------#"
echo "#                                                                   #"
echo "#                                                                   #"
echo "#                  更新代码 重启项目                                  #"
echo "#                                                                   #"
echo "#                                                                   #"
echo "#-------------------------------------------------------------------#"

start=`date +%Y%m%d%H%M`
# 项目位置
file=
#备份jar包位置
back_file=
#jar包名
jar_name=

echo ${start} " info : start project (开始重启服务) ..."

cd ${file}
echo "update code (更新代码)..."
svn update --username username --password password
echo "update end (更新完成)..."

# 打包项目跳过 test
mvn clean package -Dmaven.test.skip=true

echo "backup jar (备份jar包)..."
now=`date +%Y%m%d%H%M`
$(cp ${file}/health-web/target/${jar_name}.jar ${back_file}/${jar_name}_${now}.jar)

echo "start project (开始重启服务器)..."
sh stop-jar.sh
sh start-jar.sh
end=`date +%Y%m%d%H%M`
echo ${end} " info : start project success (重新启动服务成功) ..."

