# markdown 文档编写

## 格式

### 基本语法

- 标题书写方式

  ```md
  # 一级标题

  ## 二级标题

  ### 三级标题

  #### 四级标题

  ##### 五级标题

  ###### 六级标题
  ```

- 效果

  # 一级标题

  ## 二级标题

  ### 三级标题

  #### 四级标题

  ##### 五级标题

  ###### 六级标题

- 字体书写方式

  ```md
  _斜体_

  或

  _斜体_

  **粗体**

  **_加粗斜体_**

  ~~删除线~~
  ```

- 效果

  _斜体_

  _斜体_

  **粗体**

  **_加粗斜体_**

  ~~删除线~~

- 超链接


    Go [Home][home].

    [home]: https://example.org
    ```md
    欢迎来到[github项目-learning-notes-首页](https://github.com/zhangymPerson/learning-notes)

    ![微信好友](../Picture/wechat-info.png)
    ```

- 效果

  欢迎来到[github 项目-learning-notes-首页](https://github.com/zhangymPerson/learning-notes)

  ![微信好友](../Picture/wechat-info.png)

- 参考式

  ```md
  我经常去的几个网站[GitHub][1]、[知乎][2]以及[简书][3]
  [简书][3]是一个不错的[写作社区][]。

  [1]: https://github.com "GitHub"
  [2]: https://www.zhihu.com "知乎"
  [3]: http://www.jianshu.com "简书"
  [写作社区]: http://www.jianshu.com
  ```

- 效果

  我经常去的几个网站[GitHub][1]、[知乎][2]以及[简书][3]
  [简书][3]是一个不错的[写作社区][]。

  [1]:https://github.com "GitHub"
  [2]:https://www.zhihu.com "知乎"
  [3]:http://www.jianshu.com "简书"
  [写作社区]:http://www.jianshu.com

- 自动连接

  ```md
  <http://example.com/>
  <zhangyanmingjiayou@163.com>
  ```

- 效果

  http://example.com/

  <http://example.com/>

  zhangyanmingjiayou@163.com

  <zhangyanmingjiayou@163.com>

- 锚点

  **注意**

  Markdown Extra 只支持在标题(#标题)后插入锚点，其它地方无效。

  **经过实际使用 标题中不能有 . 号，否则页面跳转失败**

  语法描述：
  在你准备跳转到的指定标题后插入锚点{#标记}，然后在文档的其它地方写上连接到锚点的链接。

  ```md
  [跳转到本页面基本语法](#基本语法)
  ```

- 效果

  [跳转到本页面基本语法](#基本语法)

- 列表

  ```md
  - 无序列表项 一
  - 无序列表项 二
  - 无序列表项 三
  ```

- 效果

  - 无序列表项 一
  - 无序列表项 二
  - 无序列表项 三

- 有序列表

  ```md
  1. 有序列表项 一
  2. 有序列表项 二
  3. 有序列表项 三
  ```

- 效果

  1. 有序列表项 一
  2. 有序列表项 二
  3. 有序列表项 三

- 包含引用的列表

  ```md
  - 阅读的方法:

    > 打开书本。

    > 打开电灯。
  ```

- 效果

  - 阅读的方法:

    > 打开书本。

    > 打开电灯。

- 表格

  ```md
  | 学号 | 姓名 | 分数 |
  | ---- | ---- | ---- |
  | 小明 | 男   | 75   |
  | 小红 | 女   | 79   |
  | 小陆 | 男   | 92   |
  ```

- 效果

  | 学号 | 姓名 | 分数 |
  | ---- | ---- | ---- |
  | 小明 | 男   | 75   |
  | 小红 | 女   | 79   |
  | 小陆 | 男   | 92   |

- 指定表格显示内容(内容靠右显示)

  ```md
  | 产品             |      价格 |
  | ---------------- | --------: |
  | Leanote 高级账号 |  60 元/年 |
  | Leanote 超级账号 | 120 元/年 |
  ```

- 效果
  | 产品 | 价格 |
  |------------------------|--------------------------:|
  | Leanote 高级账号 | 60 元/年 |
  | Leanote 超级账号 | 120 元/年 |
  | Leanote 超级管理员账号 | 12000000000000000000 元/年 |

- 分割线

  ```md
  ---
  ---
  ---

  ---

  ---
  ```

- 效果

  ***

  ***

  ***

  ***

  ***

- 代码

  使用 [\```code 代码内容 ```]code 表示语言标识 如 json html java，py shell ... 等

  例如：

  ````md
    ```java
        public static void main(String[] args) {
            System.out.println("Hello Word!");
        }
    ```
  ````

- 效果

  ```java
  public static void main(String[] args) {
      System.out.println("Hello Word!");
  }
  ```

- todolist


    ```
    近期任务安排:
    - [x] 整理Markdown手册
    - [ ] 改善项目
        - [x] 优化首页显示方式
        - [x] 修复闪退问题
        - [ ] 修复视频卡顿
    - [ ] A3项目修复
        - [x] 修复数值错误
    ```

    近期任务安排:
    - [x] 整理Markdown手册
    - [ ] 改善项目
        - [x] 优化首页显示方式
        - [x] 修复闪退问题
        - [ ] 修复视频卡顿
    - [ ] A3项目修复
        - [x] 修复数值错误

- 支持 UML 中的部分图 过于复杂 不予记录

- 部分折叠的显示

- 效果

    <details>
    <summary><strong>MarkDown折叠显示效果</strong></summary>
    <div>

  # 一级标题

  ## 二级标题

  ### 三级标题

  #### 四级标题

  ##### 五级标题

  ###### 六级标题

    </div>
    </details>

- 代码

  ```md
  <details>
  <summary><strong>MarkDown折叠显示效果</strong></summary>
  <div>

  # 一级标题

  ## 二级标题

  ### 三级标题

  #### 四级标题

  ##### 五级标题

  ###### 六级标题

  </div>
  </details>
  ```
