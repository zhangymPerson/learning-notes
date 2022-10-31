
public class Hello {
    public static void main(String[] args) {
        System.out.println("hello word");
    }

    /**
     * 方法 = GET POST PUT ... 路径 = /danao/get/user 标题 = 获取用户信息
     * 
     * @api {POST} /java/post java中的注释测试
     * @apiGroup java-api
     * @apiDescription java代码中的注释，这个api主要是给前端提供获取用户信息的接口
     *
     * @apiParam {String} param 测试参数
     * @apiParamExample {json} 
     * request-example { "param": "测试参数" }
     *
     * @apiError {String} message 错误信息
     * @apiErrorExample {json} 
     * error-example { "message": "测试错误信息" }
     * 
     * 
     * @apiSuccess {String} code 成功状态码
     * @apiSuccess {String} createTime 创建时间
     * @apiSuccess {String} updateTime 更新时间
     * @apiSuccessExample {json} 
     * success-example { "userName": "Java", "createTime":
     *                    "1568901681", "updateTime": "1568901681" }
     */

    public void test() {

    }

    /**
     * 
     * @api {get} /company/list 获取公司信息
     * @apiName 获取公司列表
     * @apiGroup All
     * @apiVersion 0.1.0
     * @apiDescription 接口详细描述
     * 
     * @apiParam {int} pageNum分页大小
     * 
     * @apiSuccess {String} code 结果码
     * @apiSuccess {String} msg 消息说明
     * @apiSuccess {Object} data 分页数据封装
     * @apiSuccess {int} data.count 总记录数
     * @apiSuccess {Object[]} data.list 分页数据对象数组
     * @apiSuccessExample 
     * Success-Response: HTTP/1.1 200 OK { code:0, msg:‘success‘,
     *                    data:{} }
     * 
     * @apiError All 对应<code>id</code>的用户没找到 
     * @apiErrorExample {json} 
     * Error-Response: HTTP/1.1 404 Not Found 
     * { code:1,msg:‘user not found‘, }
     * 
     * @throws Exception
     */
    public void testTwo() {
    }

     /**
     * 
     * @api {get} /company/list 获取公司信息
     * @apiName 获取公司列表
     * @apiGroup All
     * @apiVersion 0.2.0
     * @apiDescription 接口详细描述
     * 
     * @apiParam {int} pageNum分页大小
     * 
     * @apiSuccess {String} code 结果码
     * @apiSuccess {String} msg 消息说明
     * @apiSuccess {Object} data 分页数据封装
     * @apiSuccess {int} data.count 总记录数
     * @apiSuccess {Object[]} data.list 分页数据对象数组
     * @apiSuccessExample 
     * Success-Response: HTTP/1.1 200 OK { code:0, msg:‘success‘,
     *                    data:{} }
     * 
     * @apiError All 对应<code>id</code>的用户没找到 
     * @apiErrorExample {json} 
     * Error-Response: HTTP/1.1 404 Not Found 
     * { code:1,msg:‘user not found‘, }
     * 
     * @throws Exception
     */
    public void testTwos() {
    }
}