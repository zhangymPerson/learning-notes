
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
     * request-example 
     * { "param": "测试参数" }
     *
     * @apiError {String} message 错误信息
     * @apiErrorExample {json} 
     * error-example { "message": "测试错误信息" }
     * 
     * 
     * @apiSuccess {String} code 成功状态码
     * @apiSuccess {String} createTime 创建时间
     * @apiSuccess {String} updateTime 更新时间
     * @apiSuccessExample {json} success-example { "userName": "Java", "createTime":
     *                    "1568901681", "updateTime": "1568901681" }
     */

    public void test() {

    }
}