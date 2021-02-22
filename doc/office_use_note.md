# office 使用技巧记录

- 给 wps word 中的表格加实线框

  选中表格 - 表格工具(顶部出现 - 设计 - 边框样式) 边框 - 选择所有边框

  不能批量操作(目前不知道怎么批量)

  然后 选择其他要操作的表格 ctrl + y , 表示对新选中的表格进行相同的操作

- excel 中多个工作表

  工作簿和工作表的关系就像书本和页面的关系，每个工作簿中可以包含多张工作表，工作簿所能包含的最大工作表数受内存的限制。默认每个新工作簿中包含 3 个工作表，在 Excel 程序界面的下方可以看到工作表标签，默认的名称为“Sheet1”、“Sheet2”、“Sheet3”。每个工作表中的内容相对独立，通过单击工作表标签可以在不同的工作表之间进行切换。

  搜索整个工作簿的方式 ctrl + f 打开搜索和替换框

  范围 选择 工作簿 点击查找全部/查找下一个 即可

  工作表太多，查看的方式

  excel 中 在 工作表 < > 箭头的位置点右键即可显示所有工作表

  wps 中在 ... 位置直接点击即可

- 打开 word / wps 的 word 文档的**目录导航**

  wps 打开默认是打开的。word 需要单独打开

  在视图下 选择 导航窗格

  或者 在 word 内的`告诉我您想要做什么`位置处直接搜索 **导航窗格**

- 选中 word 中的所有表格

  使用宏实现这一功能

  快捷键 `alt+F8` 创建一个宏，命名为`alltable`

  编写一下脚本

  ```vb
  Sub alltable()
    Dim tempTable As Table

        Application.ScreenUpdating = False

    '判断文档是否被保护

    If ActiveDocument.ProtectionType = wdAllowOnlyFormFields Then

        MsgBox "文档已保护，此时不能选中多个表格！"

        Exit Sub

    End If

    '删除所有可编辑的区域

    ActiveDocument.DeleteAllEditableRanges wdEditorEveryone

    '添加可编辑区域

    For Each tempTable In ActiveDocument.Tables

        tempTable.Range.Editors.Add wdEditorEveryone

    Next

    '选中所有可编辑区域

    ActiveDocument.SelectAllEditableRanges wdEditorEveryone

    '删除所有可编辑的区域

    ActiveDocument.DeleteAllEditableRanges wdEditorEveryone

    Application.ScreenUpdating = True

  End Sub
  ```

  单击运行，返回文档即可看到已经选中的所有表格
