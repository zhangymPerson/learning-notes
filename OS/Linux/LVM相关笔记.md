# LVM 概念

- 概念

    LVM是 Logical Volume Manager（逻辑卷管理）的简写，它是Linux环境下对磁盘分区进行管理的一种机制，它由Heinz Mauelshagen在Linux 2.4内核上实现;
    [百度百科](https://baike.baidu.com/item/LVM/6571177)

- 相关术语


    - 物理存储介质（PhysicalStorageMedia）
    
        指系统的物理存储设备：磁盘，如：/dev/hda、/dev/sda等，是存储系统最底层的存储单元。
    - 物理卷（Physical Volume，PV）
    
        指磁盘分区或从逻辑上与磁盘分区具有同样功能的设备（如RAID），是LVM的基本存储逻辑块，但和基本的物理存储介质（如分区、磁盘等）比较，却包含有与LVM相关的管理参数。
    - 卷组（Volume Group，VG）
    
        类似于非LVM系统中的物理磁盘，其由一个或多个物理卷PV组成。可以在卷组上创建一个或多个LV（逻辑卷）。
    - 逻辑卷（Logical Volume，LV）
    
        类似于非LVM系统中的磁盘分区，逻辑卷建立在卷组VG之上。在逻辑卷LV之上可以建立文件系统（比如/home或者/usr等）。
    - 物理块（Physical Extent，PE）
        
        每一个物理卷PV被划分为称为PE（Physical Extents）的基本单元，具有唯一编号的PE是可以被LVM寻址的最小单元。PE的大小是可配置的，默认为4MB。所以物理卷（PV）由大小等同的基本单元PE组成。
    - 逻辑块（Logical Extent，LE）
    
        逻辑卷LV也被划分为可被寻址的基本单位，称为LE。在同一个卷组中，LE的大小和PE是相同的，并且一一对应。

