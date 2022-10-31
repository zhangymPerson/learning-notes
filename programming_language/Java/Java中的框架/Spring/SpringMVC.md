# Spring MVC 解析

- [返回](./README.md)

## MVC 分析

- M(Model) 模型

- V(View) 视图

- C(Controller) 控制器

- 如下图所示

![MVC结构图](../../../../Picture/MVC.png)

## Spring 中 mvc

### 核心类

- DispatcherServlet (控制器核心类)

- ContextLoaderListener (加载 spring 的配置文件)

- HandlerMapping(请求转发)

- Controller(控制器,注解)

- ModelAndView(处理 Model 返回的结果)

- ViewResolver(视图处理返回)

### 运行原理

具体流程：

- 首先用户发送请求——>DispatcherServlet，前端控制器收到请求后自己不进行处理，而是委托给其他的解析器进行处理，作为统一访问点，进行全局的流程控制；

- DispatcherServlet——>HandlerMapping，映射处理器将会把请求映射为 HandlerExecutionChain 对象（包含一个 Handler 处理器（页面控制器）对象、多个 HandlerInterceptor 拦截器）对象；

- DispatcherServlet——>HandlerAdapter，处理器适配器将会把处理器包装为适配器，从而支持多种类型的处理器，即适配器设计模式的应用，从而很容易支持很多类型的处理器；

- HandlerAdapter——>调用处理器相应功能处理方法，并返回一个 ModelAndView 对象（包含模型数据、逻辑视图名）；

- ModelAndView 对象（Model 部分是业务对象返回的模型数据，View 部分为逻辑视图名）——> ViewResolver， 视图解析器将把逻辑视图名解析为具体的 View；

- View——>渲染，View 会根据传进来的 Model 模型数据进行渲染，此处的 Model 实际是一个 Map 数据结构；

- 返回控制权给 DispatcherServlet，由 DispatcherServlet 返回响应给用户，到此一个流程结束。

### 优秀文章
