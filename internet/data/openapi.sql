-- mysql
-- 环境配置
CREATE TABLE `openapi_env` (
    `id` int NOT NULL AUTO_INCREMENT,
    `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
    `create_by` varchar(255) DEFAULT NULL,
    `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `update_by` varchar(255) DEFAULT NULL,
    `env_name` varchar(255) DEFAULT NULL COMMENT '环境名称',
    `env_desc` varchar(255) DEFAULT NULL COMMENT '环境描述',
    `base_url` varchar(255) DEFAULT NULL COMMENT '环境地址',
    `variables` text COMMENT '环境变量',
    `remark` text,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 6 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = 'openapi 环境配置';

INSERT INTO
    openapi_env (
        create_time,
        create_by,
        update_time,
        update_by,
        env_name,
        env_desc,
        base_url,
        variables,
        remark
    )
VALUES
    (
        '2024-07-22 14:55:13',
        NULL,
        '2024-07-22 14:55:13',
        NULL,
        'local',
        NULL,
        'http://127.0.0.0.1:8080',
        NULL,
        '本地环境'
    );

INSERT INTO
    openapi_env (
        create_time,
        create_by,
        update_time,
        update_by,
        env_name,
        env_desc,
        base_url,
        variables,
        remark
    )
VALUES
    (
        '2024-07-22 14:55:13',
        NULL,
        '2024-07-22 14:57:10',
        NULL,
        'dev',
        NULL,
        'http://127.0.0.0.1:8080',
        NULL,
        '开发环境'
    );

INSERT INTO
    openapi_env (
        create_time,
        create_by,
        update_time,
        update_by,
        env_name,
        env_desc,
        base_url,
        variables,
        remark
    )
VALUES
    (
        '2024-07-22 14:55:13',
        NULL,
        '2024-07-22 14:57:10',
        NULL,
        'test',
        NULL,
        'https://echo.apifox.com',
        NULL,
        '测试环境'
    );

INSERT INTO
    openapi_env (
        create_time,
        create_by,
        update_time,
        update_by,
        env_name,
        env_desc,
        base_url,
        variables,
        remark
    )
VALUES
    (
        '2024-07-22 14:55:13',
        NULL,
        '2024-07-22 14:57:10',
        NULL,
        'prod',
        NULL,
        'https://echo.apifox.com',
        NULL,
        '生产环境'
    );

-- api 配置
CREATE TABLE `openapi` (
    `id` int NOT NULL AUTO_INCREMENT,
    `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
    `create_by` varchar(255) DEFAULT NULL,
    `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `update_by` varchar(255) DEFAULT NULL,
    `api_id` int DEFAULT NULL COMMENT 'api id',
    `api_group_id` int DEFAULT NULL COMMENT 'api 分组 id',
    `api_name` varchar(255) DEFAULT NULL COMMENT 'api 名称',
    `request_method` varchar(255) DEFAULT NULL COMMENT '请求方法',
    `url_type` varchar(255) DEFAULT NULL COMMENT '请求环境 dev/test/local/prod',
    `url_type_value` varchar(255) DEFAULT NULL COMMENT '请求环境地址',
    `request_path` varchar(255) DEFAULT NULL COMMENT '请求资源地址',
    `url` varchar(255) DEFAULT NULL COMMENT 'url = 环境地址+资源地址',
    `params` text COMMENT 'params',
    `body_type` varchar(255) DEFAULT NULL COMMENT '请求体类型',
    `body` text COMMENT '请求体数据',
    `headers` text COMMENT '请求头',
    `cookies` text COMMENT 'cookies',
    `auth_type` varchar(255) DEFAULT NULL COMMENT '鉴权方式',
    `auth_value` text COMMENT 'auth_value',
    `response_code` int DEFAULT NULL COMMENT '响应码',
    `response` text COMMENT '响应数据',
    `skip_status` varchar(255) DEFAULT NULL COMMENT '是否跳过',
    `remark` text,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT 'openapi';

INSERT INTO
    openapi (
        create_time,
        create_by,
        update_time,
        update_by,
        api_id,
        api_group_id,
        api_name,
        request_method,
        url_type,
        url_type_value,
        request_path,
        url,
        params,
        body_type,
        body,
        headers,
        cookies,
        auth_type,
        auth_value,
        response_code,
        response,
        skip_status,
        remark
    )
VALUES
    (
        '2024-07-22 15:00:36',
        NULL,
        NULL,
        NULL,
        1,
        1,
        'get 测试',
        'GET',
        'test',
        NULL,
        '/get',
        NULL,
        '{"a":"b"}',
        'application/json',
        '{"a":"b"}',
        '{"a":"b"}',
        '{"a":"b"}',
        '',
        NULL,
        NULL,
        NULL,
        NULL,
        NULL
    );