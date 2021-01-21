# yum 的概念和相关的操作

- [返回](./README.md)
- 什么是 yum

  Yum（全称 Yellow Dog Updater）是一个在 Fedora 和 RedHat 以及 CentOS 中的 Shell 前端软件包管理器。基于 RPM 包管理，能够从指定的服务器自动下载 RPM 包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软件包.

- 常用的命令有

  ```sh
  # 安装软件(以foo-x.x.x.rpm为例）：
  yum install foo-x.x.x.rpm

  # 删除软件：
  yum remove foo-x.x.x.rpm
  # 或者
  yum erase foo-x.x.x.rpm

  # 升级软件：
  yum upgrade foo
  # 或者
  yum update foo

  # 查询信息：
  yum info foo

  # 搜索软件（以包含foo字段为例）：
  yum search foo

  # 显示软件包依赖关系：
  yum deplist foo

  # 检查可更新的包:
  yum check-update

  # 清除全部:
  yum clean all

  # 清除临时包文件（/var/cache/yum 下文件):
  yum clean packages

  # 清除rpm头文件:
  yum clean headers

  # 清除旧的rpm头文件:
  yum clean oldheaders

  # 可安装和可更新的rpm包:
  yum list　

  # 已安装的包:
  yum list installed

  # 已安装且不在资源库的包:
  yum list extras
  ```

- 可选项说明:

  -e 静默执行

  -t 忽略错误

  -R [分钟] 设置等待命令执行结束的最大时间

  -y 自动应答，在执行 yum 操作时不需要用户交互确认

  --skip-broken 忽略依赖问题

  --nogpgcheck 忽略 GPG 校验过程

- 修改 yum 仓库

- 阿里安装软件镜像源

  阿里云 Linux 安装镜像源地址：http://mirrors.aliyun.com/

  备份你的原镜像文件，以免出错后可以恢复。

  `mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup`

  下载新的 CentOS-Base.repo 到/etc/yum.repos.d/

  `wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo`

  运行 yum makecache 生成缓存

- 163 安装软件镜像源

  `wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.163.com/.help/CentOS5-Base-163.repo`
