
## RSSHub 使用说明

### 一、Docker 配置

您的 `docker-compose.yml` 需要包含以下配置:<cite/>

```yaml
services:
  rsshub:
    image: diygod/rsshub
    restart: always
    ports:
      - '1200:1200'
    environment:
      # GitHub 路由必需
      GITHUB_ACCESS_TOKEN: 'your_github_token_here'
      # 可选:缓存时间(秒)
      CACHE_EXPIRE: '3600'
      # 可选:Puppeteer(某些站点需要)
      PUPPETEER_WS_ENDPOINT: 'ws://browserless:3000'
    depends_on:
      - browserless

  browserless:
    image: browserless/chrome
    restart: always
    environment:
      - "MAX_CONCURRENT_SESSIONS=10"
      - "MAX_QUEUE_LENGTH=10"
```

**重要提示**:
- `GITHUB_ACCESS_TOKEN` 是必需的,在 GitHub Settings → Developer settings → Personal access tokens 中生成
- 配置完成后运行 `docker-compose up -d` 启动服务<cite/>

### 二、各站点订阅 URL

#### 1. GitHub 日榜

**URL 格式**: `http://localhost:1200/github/trending/:since/:language/:spoken_language?` 

**参数说明**:
- `since`: `daily`(今日) | `weekly`(本周) | `monthly`(本月)
- `language`: 编程语言(如 `javascript`、`python`),不筛选用 `any`
- `spoken_language`: 自然语言(可选)

**示例**:
```
http://localhost:1200/github/trending/daily/any           # 今日全部语言
http://localhost:1200/github/trending/daily/javascript    # 今日 JavaScript
http://localhost:1200/github/trending/weekly/python       # 本周 Python
```

#### 2. CSDN

RSSHub 支持 CSDN 博客订阅,但需要查看具体路由。 根据代码库结构,CSDN 路由位于 `lib/routes/csdn/` 目录下。<cite/>

**常见路由**(需要在 RSSHub 文档中确认具体参数):
```
http://localhost:1200/csdn/blog/:username    # 用户博客
```

#### 3. 掘金(Juejin)

**热门文章**: `http://localhost:1200/juejin/trending/:category/:type`  

**分类选项**:
- `frontend`(前端)、`backend`(后端)、`android`、`ios`、`ai`(人工智能)、`all`(全部)等  

**时间范围**:
- `weekly`(本周最热)、`monthly`(本月最热)、`historical`(历史最热) 

**示例**:
```
http://localhost:1200/juejin/trending/frontend/weekly     # 前端本周最热
http://localhost:1200/juejin/trending/all/monthly         # 全部本月最热
http://localhost:1200/juejin/trending/ai/historical       # AI 历史最热
```

**其他掘金路由**:
```
http://localhost:1200/juejin/dynamic/:userId              # 用户动态
http://localhost:1200/juejin/collections/:userId          # 用户收藏集
```

#### 4. InfoQ

InfoQ 路由需要查看 RSSHub 文档确认是否支持及具体参数。<cite/>根据代码库,可能的路由格式为:
```
http://localhost:1200/infoq/:category    # 需确认具体分类参数
```

#### 5. 开源中国(OSChina)

**新闻资讯**: `http://localhost:1200/oschina/news/:category?` 

**分类选项**: 
- 不填或 `all`: 最新资讯(默认)
- `industry`: 综合资讯
- `project`: 软件更新资讯
- `industry-news`: 行业资讯
- `programming`: 编程语言资讯

**示例**:
```
http://localhost:1200/oschina/news                        # 最新资讯
http://localhost:1200/oschina/news/project                # 软件更新
http://localhost:1200/oschina/news/programming            # 编程语言
```

**专栏订阅**: `http://localhost:1200/oschina/column/:id` 

### 三、如何使用 RSS 订阅

RSS feed 返回的是 XML 格式,需要通过 **RSS 阅读器**订阅:<cite/>

**推荐阅读器**:
- **桌面端**: Fluent Reader、NetNewsWire (macOS)、Thunderbird
- **移动端**: Reeder (iOS)、NetNewsWire (iOS)、FeedMe (Android)
- **Web 端**: Feedly、Inoreader、The Old Reader

**订阅步骤**:
1. 安装 RSS 阅读器
2. 在阅读器中添加订阅源
3. 输入上述任意 URL
4. 阅读器会自动解析并展示文章列表

### 四、验证配置

**检查服务状态**:
```bash
docker-compose ps                    # 查看容器状态
docker-compose logs rsshub           # 查看日志
```

**测试路由**:
在浏览器访问任意 URL,如果看到包含 `<rss>` 标签的 XML 内容,说明配置成功。<cite/>

**快速测试列表**:
```
http://localhost:1200/github/trending/daily/any
http://localhost:1200/juejin/trending/all/weekly
http://localhost:1200/oschina/news
```

## Notes

- GitHub 路由**必须**配置 `GITHUB_ACCESS_TOKEN`,否则无法使用 
- 掘金和开源中国路由**无需额外配置**,开箱即用 
- CSDN 和 InfoQ 的具体路由参数建议访问 RSSHub 官方文档 (https://docs.rsshub.app) 查看最新支持情况
- 浏览器直接访问会显示 XML,这是正常的,需要用 RSS 阅读器订阅
- 如需在浏览器预览,可安装 RSS Preview (Chrome/Edge) 或 Feedbro (Firefox) 扩展
- 更多路由和详细文档请参考: 

