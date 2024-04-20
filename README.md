**使用说明：**
- chrome里安装一个cookie-Editor插件，找一下自己账号_session_id的值，将这个值保存在# List of tokens

-TOKENS = [
-    "_session_id_sample001",
-    "_session_id_sample001",
-    "_session_id_sample001"
-]

**代码运行流程：**
-	根据操作系统类型，设置Chrome浏览器的二进制文件位置。
-	使用selenium的webdriver打开Chrome浏览器，并访问"https://www.coingecko.com/zh/candy"这个网址。
-	检查是否提供了Google的认证令牌，如果没有提供或者令牌是默认值，则抛出错误。
-	设置浏览器的"_session_id" cookie为提供的认证令牌。
-	等待网页加载完成，然后刷新网页。
-	再次等待网页加载完成。
-	获取网页的源代码。
-	使用BeautifulSoup解析网页的HTML内容。
-	查找并获取页面上ID为"collectButton"的按钮元素。
