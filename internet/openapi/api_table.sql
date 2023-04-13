-- mysql
CREATE DATABASE `apijson`;
DROP TABLE IF EXISTS openapi;
CREATE TABLE openapi(
    id VARCHAR(32) NOT NULL AUTO_INCREMENT COMMENT '',
    name VARCHAR(255) COMMENT '此次请求名称',
    desc VARCHAR(900) COMMENT '此次请求描述',
    protocol VARCHAR(255) COMMENT '请求协议',
    host VARCHAR(255) COMMENT '主机',
    port VARCHAR(255) COMMENT '端口',
    method VARCHAR(255) COMMENT '方法',
    header VARCHAR(255) COMMENT '协议头',
    params VARCHAR(255) COMMENT '请求参数',
    body VARCHAR(255) COMMENT '请求体内容',
    file_key VARCHAR(255) COMMENT '文件类型时的文件key',
    file_name VARCHAR(255) COMMENT '文件名',
    create_time VARCHAR(255) COMMENT '创建时间',
    update_time VARCHAR(255) COMMENT '更新时间',
    order_id VARCHAR(255) COMMENT '请求顺序',
    group_id VARCHAR(255) COMMENT '请求组',
    skip_status VARCHAR(255) COMMENT '是否跳过',
    remark VARCHAR(900) COMMENT '备注',
    PRIMARY KEY (id)
) COMMENT = 'openapi';
INSERT INTO openapi (id, api_name, api_desc, protocol, host, port, `method`, header, params, body, file_key, file_name, create_time, update_time, order_id, group_id, group_name, skip_status, remark) VALUES(1, '测试百度', '测试请求', 'https', 'baidu.com', '80', 'get', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1', '1', '测试组', NULL, NULL);
-- postgresql
DROP TABLE IF EXISTS openapi;
CREATE TABLE openapi(
    id SERIAL NOT NULL,
    api_name VARCHAR(255),
    api_desc VARCHAR(900),
    protocol VARCHAR(255),
    host VARCHAR(255),
    port VARCHAR(255),
    method VARCHAR(255),
    header VARCHAR(255),
    params VARCHAR(255),
    body VARCHAR(900),
    file_key VARCHAR(255),
    file_name VARCHAR(255),
    create_time VARCHAR(255),
    update_time VARCHAR(255),
    order_id VARCHAR(255),
    group_id VARCHAR(255),
    group_name VARCHAR(255),
    skip_status VARCHAR(255),
    remark VARCHAR(900),
    PRIMARY KEY (id)
);
COMMENT ON TABLE openapi IS 'openapi';
COMMENT ON COLUMN openapi.api_name IS '此次请求名称';
COMMENT ON COLUMN openapi.api_desc IS '此次请求描述';
COMMENT ON COLUMN openapi.protocol IS '请求协议';
COMMENT ON COLUMN openapi.host IS '主机';
COMMENT ON COLUMN openapi.port IS '端口';
COMMENT ON COLUMN openapi.method IS '方法';
COMMENT ON COLUMN openapi.header IS '协议头';
COMMENT ON COLUMN openapi.params IS '请求参数';
COMMENT ON COLUMN openapi.body IS '请求体内容';
COMMENT ON COLUMN openapi.file_key IS '文件类型时的文件key';
COMMENT ON COLUMN openapi.file_name IS '文件名';
COMMENT ON COLUMN openapi.create_time IS '创建时间';
COMMENT ON COLUMN openapi.update_time IS '更新时间';
COMMENT ON COLUMN openapi.order_id IS '请求顺序';
COMMENT ON COLUMN openapi.group_id IS '请求组';
COMMENT ON COLUMN openapi.group_name IS '请求组名';
COMMENT ON COLUMN openapi.skip_status IS '是否跳过';
COMMENT ON COLUMN openapi.remark IS '备注';
INSERT INTO public.openapi (id, api_name, api_desc, protocol, host, port, "method", "header", params, body, file_key, file_name, create_time, update_time, order_id, group_id, group_name, skip_status, remark) VALUES(1, '测试百度', '测试接口', 'https', 'baidu.com', '80', 'get', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1', '1', '组名', NULL, NULL);
