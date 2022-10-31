/**
 * @api {GET} /js/get js中注释测试
 * @apiGroup JS-api
 * @apiDescription 描述这个API的信息 Js文件中的内容,js中的注释测试
 *
 * @apiParam {String} userName 用户名
 * @apiParamExample {json} request-example
 * {
 *  "userName": "JavaScript"
 * }
 *
 * @apiError {String} message 错误信息
 * @apiErrorExample  {json} error-example
 * {
 *   "message": "用户名不存在"
 * }
 * 
 * 
 * @apiSuccess {String} userName 用户名
 * @apiSuccess {String} createTime 创建时间
 * @apiSuccess {String} updateTime 更新时间
 * @apiSuccessExample  {json} success-example
 * {
 *   "userName": "JavaScript",
 *   "createTime": "1568901681",
 *   "updateTime": "1568901681"
 * }
 */
function test() {

}