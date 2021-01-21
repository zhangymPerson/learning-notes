# linux 上的命名空间

- [返回](./README.md)
- Linux Namespaces 机制提供一种资源隔离方案

## 类型

- CLONE_NEWIPC: 进程间通信(IPC)的命名空间，可以将 SystemV 的 IPC 和 POSIX 的消息队列独立出来。
- CLONE_NEWPID: 进程命名空间。空间内的 PID 是独立分配的，意思就是命名空间内的虚拟 PID 可能会与命名空间外的 PID 相冲突，于是命名空间内的 PID 映射到命名空间外时会使用另外一个 PID。比如说，命名空间内第一个 PID 为 1，而在命名空间外就是该 PID 已被 init 进程所使用。
- CLONE_NEWNET: 网络命名空间，用于隔离网络资源（/proc/net、IP 地址、网卡、路由等）。后台进程可以运行在不同命名空间内的相同端口上，用户还可以虚拟出一块网卡。
- CLONE_NEWNS: 挂载命名空间，进程运行时可以将挂载点与系统分离，使用这个功能时，我们可以达到 chroot 的功能，而在安全性方面比 chroot 更高。
- CLONE_NEWUTS: UTS 命名空间，主要目的是独立出主机名和网络信息服务（NIS）。
- CLONE_NEWUSER: 用户命名空间，同进程 ID 一样，用户 ID 和组 ID 在命名空间内外是不一样的，并且在不同命名空间内可以存在相同的 ID。

- 如下表所示:

  | Namespace | 变量            | 隔离资源                       |
  | --------- | --------------- | ------------------------------ |
  | Cgroup    | CLONE_NEWCGROUP | Cgroup 根目录                  |
  | IPC       | CLONE_NEWIPC    | System V IPC, POSIX 消息队列等 |
  | Network   | CLONE_NEWNET    | 网络设备，协议栈、端口等       |
  | Mount     | CLONE_NEWNS     | 挂载点                         |
  | PID       | CLONE_NEWPID    | 进程 ID                        |
  | User      | CLONE_NEWUSER   | 用户和 group ID                |
  | UTS       | CLONE_NEWUTS    | Hostname 和 NIS 域名           |

- Namespace API 提供了三种系统调用接口：

  - clone()：创建新的进程
  - setns()：允许指定进程加入特定的 namespace
  - unshare()：将指定进程移除指定的 namespace
