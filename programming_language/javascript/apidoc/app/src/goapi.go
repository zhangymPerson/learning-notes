package main

import "fmt"

func main() {
	fmt.Print("Hello Word!")
}

/**
* 方法 = GET POST PUT ... 路径 = /danao/get/user 标题 = 获取用户信息
*
* @api {POST} /go/post java中的注释测试
* @apiGroup go-api
* @apiDescription go代码中的注释，这个api主要是给前端提供获取用户信息的接口
*
* @apiParam {String} param 测试参数
* @apiParamExample {json}
* request-example
* { "param": "测试参数" }
*
* @apiSuccess {String} code 成功状态码
* @apiSuccess {String} createTime 创建时间
* @apiSuccess {String} updateTime 更新时间
*
* @apiSuccessExample {json} Success-Response:
* {
*   "userName": "Java",
*   "createTime": "1568901681",
*   "updateTime": "1568901681"
* }
*
* @apiSuccessExample {json} 返回结果2:
* {
*   "userName": "Java",
*   "createTime": "1568901681",
*   "updateTime": "1568901681"
* }
*
* @apiErrorExample {json} 错误信息1
* { "message": "测试错误信息" }
* @apiErrorExample {json} 错误返回:
* {
* 	"code":500,
* 	"msg":"错误信息"
* }
 */
func test() {

}
