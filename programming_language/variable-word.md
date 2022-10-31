# 开发中常用的前后缀用法

> 注：pre- prefix 前缀，suf- suffix 后缀，alo-alone 单独使用

#### 真伪类型

| 位置 | 单词   | 意义                                                                               | 例            |
| :--- | :----- | :--------------------------------------------------------------------------------- | :------------ |
| pre  | is     | 对象是否符合期待的状态                                                             | isValid       |
| pre  | can    | 对象**能否执行** 所期待的动作                                                      | canRemove     |
| pre  | should | 调用方执行某个命令 或方法是**好还是不好** **应不应该** ， 或者说**推荐还是不推荐** | shouldMigrate |
| pre  | has    | 对象**是否持有** 所期待的数据和属性                                                | hasObservers  |
| pre  | needs  | 调用方**是否需要** 执行某个命令或方法                                              | needsMigrate  |

#### 检查类型

| 单词     | 意义                                                 | 例             |
| :------- | :--------------------------------------------------- | :------------- |
| ensure   | 检查是否为期待的状态 不是则抛出异常或返回 error code | ensureCapacity |
| validate | 检查是否为正确的状态 不是则抛出异常或返回 error code | validateInputs |

#### 执行类型

| 位置 | 单词      | 意义                                       | 例                     |
| :--- | :-------- | :----------------------------------------- | :--------------------- |
| suf  | IfNeeded  | 需要的时候执行 不需要则什么都不做          | drawIfNeeded           |
| pre  | might     | 同上                                       | mightCreate            |
| pre  | try       | 尝试执行 失败时抛出异常 或是返回 errorCode | tryCreate              |
| suf  | OrDefault | 尝试执行 失败时返回默认值                  | getOrDefault           |
| suf  | OrElse    | 尝试执行 失败时返回 实际参数中指定的值     | getOrElse              |
| pre  | force     | 强制尝试执行 error 抛出异常或是返回值      | forceCreate, forceStop |

#### 异步相关

| 位置      | 单词         | 意义                  | 例                    |
| :-------- | :----------- | :-------------------- | :-------------------- |
| pre       | blocking     | 线程阻塞方法          | blockingGetUser       |
| suf       | InBackground | 执行在后台线程        | doInBackground        |
| suf       | Async        | 异步方法              | sendAsync             |
| suf       | Sync         | 同步方法              | sendSync              |
| pre / alo | schedule     | Job 和 Tas k 放入队列 | schedule, scheduleJob |
| pre / alo | post         | 同上                  | postJob               |
| pre / alo | execute      | 执行异步 或同步方法   | execute, executeTask  |
| pre / alo | start        | 同上                  | star, startJob        |
| pre / alo | cancel       | 停止异步方法          | cancel, cancelJob     |
| pre / alo | stop         | 同上                  | stop,stopJob          |

#### 回调

| 位置 | 单词   | 意义                  | 例           |
| :--- | :----- | :-------------------- | :----------- |
| pre  | on     | 事件发生时执行        | onCompleted  |
| pre  | before | 事件发生前执行        | beforeUpdate |
| pre  | pre    | 同上                  | preUpdate    |
| pre  | will   | 同上                  | willUpdate   |
| pre  | after  | 事件发生后执行        | afterUpdate  |
| pre  | post   | 同上                  | postUpdate   |
| pre  | did    | 同上                  | didUpdate    |
| pre  | should | 确认事件 是否可以执行 | shouldUpdate |

#### 操作对象生命周期

| 单词       | 意义                   | 例              |
| :--------- | :--------------------- | :-------------- |
| initialize | 初始化或延迟初始化使用 | initialize      |
| pause      | 暂停                   | onPause , pause |
| stop       | 停止                   | onStop, stop    |
| abandon    | 销毁的替代             | abandon         |
| destroy    | 同上                   | destroy         |
| dispose    | 同上                   | dispose         |

#### 与集合操作相关

| 单词     | 意义                     | 例         |
| :------- | :----------------------- | :--------- |
| contains | 是包含指定对象相同的对象 | contains   |
| add      | 添加                     | addJob     |
| append   | 添加                     | appendJob  |
| insert   | 插入到下标 n             | insertJob  |
| put      | 添加与 key 对应的元素    | putJob     |
| remove   | 移除元素                 | removeJob  |
| enqueue  | 添加到队列的最末位       | enqueueJob |
| dequeue  | 从队列中头部取出并移除   | dequeueJob |
| push     | 添加到栈头               | pushJob    |
| pop      | 从栈头取出并移除         | popJob     |
| peek     | 从栈头取出但不移除       | peekJob    |
| find     | 寻找符合条件的某物       | findById   |

#### 与数据相关

| 单词   | 意义                                  | 例            |
| :----- | :------------------------------------ | :------------ |
| create | 新创建                                | createAccount |
| new    | 新创建                                | newAccount    |
| from   | 从既有的某物新建 或是从其他的数据新建 | fromConfig    |
| to     | 转换                                  | toString      |
| update | 更新既有某物                          | updateAccount |
| load   | 读取                                  | loadAccount   |
| fetch  | 远程读取                              | fetchAccount  |
| delete | 删除                                  | deleteAccount |
| remove | 删除                                  | removeAccount |
| save   | 保存                                  | saveAccount   |
| store  | 保存                                  | storeAccount  |
| commit | 保存                                  | commitChange  |
| apply  | 保存或应用                            | applyChange   |
| clear  | 清除或是恢复到初始状态                | clearAll      |
| reset  | 清除或是恢复到初始状态                | resetAll      |

#### 成对出现的动词

| 单词      | 含义 | 反义词      | 含义   |
| :-------- | :--- | :---------- | :----- |
| abort     | 放弃 | quit        | 离开   |
| add       | 加入 | append      | 添加   |
| add       | 增加 | remove      | 删除   |
| attach    | 附着 | detach      | 脱离   |
| backup    | 备份 | restore     | 恢复   |
| begin     | 起始 | end         | 结束   |
| bind      | 绑定 | separate    | 分离   |
| build     | 构建 | publish     | 发布   |
| check out | 签出 | check in    | 签入   |
| clean     | 清理 | clear       | 清除   |
| collect   | 收集 | aggregate   | 聚集   |
| compile   | 编译 | execute     | 执行   |
| compress  | 压缩 | decompress  | 解压缩 |
| connect   | 连接 | disconnect  | 断开   |
| copy      | 复制 | paste       | 粘贴   |
| create    | 创建 | destory     | 移除   |
| create    | 创建 | destroy     | 销毁   |
| debug     | 调试 | trace       | 跟踪   |
| download  | 下载 | upload      | 上传   |
| edit      | 编辑 | modify      | 修改   |
| encode    | 编码 | decode      | 解码   |
| encrypt   | 加密 | decrypt     | 解密   |
| enter     | 进入 | exit        | 退出   |
| expand    | 展开 | collapse    | 折叠   |
| find      | 查找 | search      | 搜索   |
| get       | 获取 | set         | 设置   |
| import    | 导入 | export      | 导出   |
| increase  | 增加 | decrease    | 减少   |
| index     | 索引 | sort        | 排序   |
| inject    | 注入 | extract     | 提取   |
| input     | 输入 | output      | 输出   |
| insert    | 插入 | delete      | 移除   |
| launch    | 启动 | run         | 运行   |
| load      | 载入 | save        | 保存   |
| lock      | 锁定 | unlock      | 解锁   |
| observe   | 观察 | listen      | 监听   |
| obsolete  | 废弃 | depreciate  | 废旧   |
| open      | 打开 | close       | 关闭   |
| pack      | 打包 | unpack      | 解包   |
| parse     | 解析 | emit        | 生成   |
| play      | 播放 | pause       | 暂停   |
| push      | 推   | pull        | 拉     |
| read      | 读取 | write       | 写入   |
| refresh   | 刷新 | synchronize | 同步   |
| select    | 选取 | mark        | 标记   |
| send      | 发送 | receive     | 接收   |
| split     | 分割 | merge       | 合并   |
| start     | 开始 | finish      | 完成   |
| start     | 启动 | stop        | 停止   |
| submit    | 提交 | commit      | 交付   |
| undo      | 撤销 | redo        | 重做   |
| update    | 更新 | revert      | 复原   |
| view      | 查看 | browse      | 浏览   |
