# apidoc 项目 使用

## 网站

- [官网](https://apidocjs.com/)

- [github](https://github.com/apidoc/apidoc)

## 安装使用

- 依赖 nodejs

- 安装 apidoc

  `npm install -g apidoc`

## 命令

apidoc 参数

一些重要的参数如下表所示：

| 参数 | 描述                                                                          |
| ---- | ----------------------------------------------------------------------------- |
| -f   | 选择要解析的文件，支持正则表达式。-f 参数可以使用多次，多个表达式可以对应不同 | 的-f。如：apidoc -f "._\.js\$" -f "._\\.ts\$" |
| -i   | 选择源代码所在的位置。如：apidoc -i src/                                      |
| -o   | 选择生成的目标文件所在的位置。如：apidoc -o apidoc/                           |
| -t   | 为生成文件选择模板，可以创建和使用自定义的模板。                              |
| -h   | 打印帮助文档                                                                  |

> apidoc -i src/ -o apidoc/ # 可以通过搜索 src 目录中的文件快速的生成文档文件，|并将这些文件放在 apidoc 目录下。

## 使用

- 需要主配置文件

  在项目根目录下创建 apidoc.json 文件

  ```json
  {
    "name": "appleFarm", //文档项目名
    "title": "appleFarmAPI", //html标题
    "description": "appleFarmAPI接口文档", //文档描述
    "url": "https: //xxx.com", //公共接口地址
    "version": "0.1.0" //文档版本
  }
  ```

  注释文件 可以在代码中，也可以在别的文件中

  ```
  /**
   * 定义一个变量 用于apiGroup 因为不支持直接输入中文
   * @apiDefine test 测试
   */

  /**
   * @api {post} /Index/getVip 获取vip列表   页面加载时自动获取
   * @apiName GetUser
   * @apiGroup test
   *
   * @apiParam {string} req1 请求值
   *
   * @apiSuccess {String} res1 返回值1
   * @apiSuccessExample Success-Response:
   * {
   * 　　res1:"test"
   * }
   */
  ```

- 构建文档
  ```sh
  # src/      为配置文件所在位置，可以是任意位置
  # apidoc/   表示创建的文档页面的位置
  apidoc -i src/ -o apidoc/
  ```

## 常见注释

- @api {get} /users/:user_id Request User Information

  最主要的参数，”{get}”定义了 HTTP 请求是 GET，API 地址是”/users/:user_id”，文档中 API 的名称是”Request User Information”。

- @apiVersion 0.1.0

  API 的版本号，默认显示在 API 名称的右方。该参数可用来在不同的版本之间做比较，后面会介绍。

- @apiName GetUser

  API 名称，不影响文档。

- @apiGroup User

  API 分组名，文档内容中和菜单栏中同一组的 API 会在一同显示，方便阅读。

- @apiPermission admin

  API 的访问权限，文档中默认会 API 地址下面显示。没有权限要求的话，此项可以省略。

- @apiDescription API to get the user information.
  API 的详细描述，默认显示在 API 名称的下方。
- @apiExample Example usage:

  API 调用示例，该参数的下一行就是示例的内容，直到有空行结束。可以定义多@apiExample，默认在文档中会以标签形式列出，标签名就是”Example usage:”。

- @apiParam {Number} user_id The user’s unique ID.

  API 参数字段介绍，”{Number}”定义了字段类型，”user_id”是字段名称，后面则是字描述。可以定义多个@apiParam 字段。

- @apiSuccess {String} name Name of the User.

  API 成功后返回的字段，如同@apiParam，”{String}”定义了字段类型，”name”是返回段名称，后面则是字段描述。可以定义多个@apiSuccess 字段。

- @apiSuccessExample {json} Success-Response:

  显示一个 API 成功返回后 Response 响应的示例，”{json}”代表响应体是 JSON 类型。该数的下行就是响应体内容，直到有空行结束。可以定义多个@apiSuccessExample，默在文档中会以标签形式列出，标签名就是”Success-Response:”。

- @apiError UserNotFound User was not found.

  API 发生错误后的返回，”UserNotFound”是错误名称，后面则是错误描述。可以定义多错误返回。

- @apiErrorExample {json} Error-Response:

  显示一个 API 错误返回后 Response 响应的示例，”{json}”代表响应体是 JSON 类型。该数的下行就是响应体内容，直到有空行结束。可以定义多个@apiErrorExample，默认在档中会以标签形式列出，标签名就是”Error-Response:”。

- @apiSampleRequest http://localhost:5000/users/:user_id

  文档提供的 API Sample 测试的地址。其实在”apidoc.json”中配过”sampleUrl”项后此参数即可省去，除非这个 API 的测试 URL 比较特殊，需特别指定。
