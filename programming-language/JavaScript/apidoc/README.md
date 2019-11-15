# apidoc 项目 使用

## 网站

- [官网](https://apidocjs.com/)

- [github](https://github.com/apidoc/apidoc)

## 安装使用

- 依赖nodejs

- 安装apidoc

    npm install -g apidoc

## 使用

- 需要主配置文件 


    在项目根目录下创建apidoc.json文件

    ```json
    {
        "name": "appleFarm", //文档项目名
        "title": "appleFarmAPI", //html标题
        "description":"appleFarmAPI接口文档", //文档描述
        "url" : "https: //xxx.com",//公共接口地址
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
    
    最主要的参数，”{get}”定义了HTTP请求是GET，API地址是”/users/:user_id”，文档中API的名称是”Request User Information”。

- @apiVersion 0.1.0
  
    API的版本号，默认显示在API名称的右方。该参数可用来在不同的版本之间做比较，后面会介绍。

- @apiName GetUser
 
    API名称，不影响文档。

- @apiGroup User
 
    API分组名，文档内容中和菜单栏中同一组的API会在一同显示，方便阅读。

- @apiPermission admin

    API的访问权限，文档中默认会API地址下面显示。没有权限要求的话，此项可以省略。
- @apiDescription API to get the user information.
    
    API的详细描述，默认显示在API名称的下方。
- @apiExample Example usage:

    API调用示例，该参数的下一行就是示例的内容，直到有空行结束。可以定义多@apiExample，默认在文档中会以标签形式列出，标签名就是”Example usage:”。
- @apiParam {Number} user_id The user’s unique ID.

    API参数字段介绍，”{Number}”定义了字段类型，”user_id”是字段名称，后面则是字描述。可以定义多个@apiParam字段。
- @apiSuccess {String} name Name of the User.

    API成功后返回的字段，如同@apiParam，”{String}”定义了字段类型，”name”是返回段名称，后面则是字段描述。可以定义多个@apiSuccess字段。
- @apiSuccessExample {json} Success-Response:

    显示一个API成功返回后Response响应的示例，”{json}”代表响应体是JSON类型。该数的下行就是响应体内容，直到有空行结束。可以定义多个@apiSuccessExample，默在文档中会以标签形式列出，标签名就是”Success-Response:”。
- @apiError UserNotFound User was not found.

    API发生错误后的返回，”UserNotFound”是错误名称，后面则是错误描述。可以定义多错误返回。
- @apiErrorExample {json} Error-Response:

    显示一个API错误返回后Response响应的示例，”{json}”代表响应体是JSON类型。该数的下行就是响应体内容，直到有空行结束。可以定义多个@apiErrorExample，默认在档中会以标签形式列出，标签名就是”Error-Response:”。
- @apiSampleRequest http://localhost:5000/users/:user_id

    文档提供的API Sample测试的地址。其实在”apidoc.json”中配过”sampleUrl”项后此参数即可省去，除非这个API的测试URL比较特殊，需特别指定。
