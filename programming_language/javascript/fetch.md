# Fetch API

- [返回](./README.md)
## 简介

- Fetch API 提供了一个获取资源的接口（包括跨域请求）。任何使用过 XMLHttpRequest 的人都能轻松上手，而且新的 API 提供了更强大和灵活的功能集。

- Fetch API 提供了一个 JavaScript 接口，用于访问和操纵 HTTP 管道的一些具体部分，例如请求和响应。它还提供了一个全局 fetch() 方法，该方法提供了一种简单，合理的方式来跨网络异步获取资源。

## 官方 github

- [https://github.com/github/fetch](https://github.com/github/fetch)

## 使用

- 下载安装

  `npm install whatwg-fetch --save`

  - 用法 1

  ```js
  import 'whatwg-fetch'

      window.fetch(...)
  ```

  - 用法 2

  ```js
  import {fetch as fetchPolyfill} from 'whatwg-fetch'

  window.fetch(...)   // use native browser version
  fetchPolyfill(...)  // use polyfill implementation
  ```

- 使用 node-fetch

  github 地址: https://github.com/node-fetch/node-fetch

  下载安装 `npm install node-fetch`

  - 用法 1

  ```js
  // CommonJS
  const fetch = require("node-fetch");

  // ES Module
  import fetch from "node-fetch";
  ```

  - 用法 2 (全局)

  ```js
  const fetch = require("node-fetch");

  if (!globalThis.fetch) {
    globalThis.fetch = fetch;
  }
  ```

- 解析 json 的用法

  ```js
  const fetch = require("node-fetch");

  const response = await fetch("https://api.github.com/users/github");
  const data = await response.json();

  console.log(data);
  ```

- 解析单个接口数据

  请求接口时，结合浏览器中 F12 -> network -> 选则 XHR -> 在单个请求上右键单击 copy -> copy as fetch

  然后创建 `script.js` 脚本,复制 fetch 请求代码,然后 `node script.js` 执行即可查看接口返回数据

- script demo

  **注意: fetch()调用后数据解析需要调用两次 `then()` 函数**

  ```js
  const fetch = require("node-fetch");
  // 解析json
  fetch("http://example.com/movies.json")
    .then(function (response) {
      return response.json();
    })
    .then(function (myJson) {
      console.log(myJson);
    });
  // 异常处理
  fetch("http://example.com/movies.json").catch((error) => console.error(error));
  //文本处理
  fetch("http://http://example.com/movies.json")
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.log("error", error));
  ```
