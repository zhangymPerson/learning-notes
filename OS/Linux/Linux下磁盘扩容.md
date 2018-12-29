# 阿里云磁盘扩容方法

- 连接地址

    [点击此处](https://bbs.aliyun.com/read/239398.html)


- 大致过程

    
    ```sh

    #先卸载旧盘
    umount /dev/vdb1
    #查看是否卸载成功，如果看不到 /dev/vdb1 的信息表示卸载成功 
    df -h 
    #使用 fdisk 命令删除原来的分区并创建新分区
    #部分操作系统里，修改分区后可能会重新自动挂载文件系统。建议先执行 df -h 重新查看文件系统空间和使用情况。如果文件系统重新被挂载，执行 umount [文件系统名称] 再次卸载文件系统。
    
    #检查文件系统，并变更文件系统大小。
    e2fsck -f /dev/vdb1 # 检查文件系统
    resize2fs /dev/vdb1 # 变更文件系统大小

    #将扩容完成的文件系统挂载到原来的挂载点
    mount /dev/vdb1 /resizetest
    ```
    [扩容数据盘_Linux](https://help.aliyun.com/document_detail/25452.html)



