<?php

/**
 * 执行任务
 */
class Task {

    private $dbConf = [
        'dbhost' => '127.0.0.1',
        'dbuser' => 'root',
        'dbpwd'  => '123456',
        'dbname' => 'test',
        'dbport' => '3306',
    ];

    private $db;

    /**
     * 执行内容
     */
    public function run() {
        echo "script";
        $this->initDB($this->dbConf);
        $this->exeuteSql("show tables;");
    }

    /**
     * 初始化DB
     *
     * @param array $conf 配置文件
     *
     * @return null
     */
    private function initDB($conf) {
        $this->db = new mysqli($conf['dbhost'], $conf['dbuser'], $conf['dbpwd'], $conf['dbname'], $conf['dbport']);
        if ($this->db->connect_errno) {
            $msg = sprintf('mysql connection error. error no: %s; error info: %s', $this->db->connect_error, $this->db->connect_errno);
            file_put_contents($this->errLogPath, date('Y-m-d H:i:s', time()) . $msg . PHP_EOL, FILE_APPEND | LOCK_EX);
            exit();
        }
        $this->db->set_charset("utf8");
        echo "连接成功" . PHP_EOL;
    }

    private function exeuteSql($sql) {
        $res = $this->db->query($sql);
        if ($res === false) {
            $msg = sprintf('sql: [%s]; db errno: %d; db error: %s', $sql, $this->db->errno, $this->db->error);
            file_put_contents($this->errLogPath, $msg . PHP_EOL, FILE_APPEND | LOCK_EX);
            return false;
        }
        var_dump($res);
        echo "执行的结果" . gettype($res) . PHP_EOL;
        return true;
    }
}

$task = new Task();
$task->run();
