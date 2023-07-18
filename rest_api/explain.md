这段代码是一个简单的 Python 网页爬虫，专门用于爬取 http://127.0.0.1:7001/console/console.portal 开头的网页并把爬取到的 URL 写入到一个文本文件中。

下面是这段代码的基本运行逻辑：

导入所需的库：requests库用于处理 HTTP 请求，BeautifulSoup库用于解析 HTML，urljoin用于处理相对 URL。

定义了一个名为cookies的字典，该字典包含了一个特定的 cookie：ADMINCONSOLESESSION，这可能是用于某种身份认证的。

crawl函数接受一个网址 URL 作为参数，然后使用requests.get函数发送 GET 请求到该 URL（同时携带上面定义的 cookies）。使用 BeautifulSoup 解析返回的 HTML 内容，并提取出所有的链接（a标签的href属性）。然后，将这些链接进行处理，如果它们不是以#开头，则通过urljoin函数处理成完整的 URL。最后返回这些链接的列表。

recursive_crawl函数接受两个参数：一个网址 URL 和一个 visited 集合（记录已经访问过的 URL，避免重复访问）。它首先检查该 URL 是否已经访问过以及是否以 http://127.0.0.1:7001/console/console.portal 开头，如果都满足，则将 URL 加入到 visited 集合中，并将 URL 写入到 output.txt 文件中。然后，使用crawl函数获取 URL 对应的网页中所有的链接，对于每一个链接，使用recursive_crawl函数递归地爬取。这样，就可以爬取到所有从初始 URL 出发可以达到的网页。

末尾部分指定了初始的 URL，然后调用recursive_crawl函数开始爬取。

总的来说，这是一个递归的深度优先搜索（DFS）爬虫，用于爬取一个特定的网站的所有页面。它可能被用于网站的爬取，数据抓取，或者安全测试等场景中。

----------------------------------

这段代码主要用于从 HTML 中抽取 GET 和 POST 请求，并以特定格式输出。

以下是代码的主要功能：

extract_post_requests(html)：该函数从输入的 HTML 中解析出所有的 POST 请求。它首先用 BeautifulSoup 解析 HTML，然后寻找所有的表单（form标签）。对于每一个表单，它检查其 method 属性是否为 POST，如果是，那么它会抽取出该表单所有的 input 标签的 name 和 value 属性，并且把它们以 (name, value) 的形式加入到一个列表中。最后，它将该表单的 action 属性和 input 列表一起作为一个元组加入到结果列表中。结果列表的每一项就代表一个 POST 请求，其中包含请求的 URL（form的action属性）和请求的数据（input的name和value属性）。

extract_post_requests_b64(html)：该函数的功能和 extract_post_requests(html) 类似，但是它会将 POST 数据编码为 base64 格式，并将 POST 请求信息保存为一个字典，其中包含 Method（请求方法），URL（请求 URL），b64_body（请求体的base64编码）。

extract_get_requests(html)：该函数从输入的 HTML 中解析出所有的 GET 请求。它首先用 BeautifulSoup 解析 HTML，然后寻找所有的链接（a标签）。对于每一个链接，它抽取出 href 属性，如果这个属性存在，那么它将其解析为一个 URL，并且抽取出其中的 scheme 和 netloc 部分。如果这两部分都存在，那么它会认为这是一个完整的 URL，然后将其以一个包含 Method（请求方法）和 URL（请求 URL）的字典的形式加入到结果列表中。

最后的部分是主程序。首先，它定义了一些 cookies，这些 cookies 可能用于身份认证。然后，它从 output.txt 文件中读取 URL 列表，对于每一个 URL，它发送 GET 请求，并且将返回的 HTML 页面传入 extract_post_requests_b64() 函数中，输出抽取的 POST 请求信息。

在代码的注释部分，还包含了一些使用 extract_get_requests() 函数抽取 GET 请求的示例。

总的来说，这段代码可以用于抽取 HTML 中的 GET 和 POST 请求，它可以用于网络爬虫，或者网络安全测试等场景中。


---------------------------


这段代码和之前的代码主要执行的功能相同，都是对网页进行爬取并提取出所有的 POST 请求，但是有几个主要的区别：

这段代码在处理完 POST 请求后，将其转换为 JSON 格式并存储到一个 set 中以消除重复的请求。在之前的代码中，所有的 POST 请求都会被收集，没有处理重复的请求。

在每次找到新的 POST 请求时，这段代码将 JSON 格式的 POST 请求写入到一个名为 'output_post_requests.json' 的文件中，而不是简单地打印出来。

在这段代码中，存储 POST 请求的是一个 set（集合），这样可以有效地去除重复的请求（因为集合中的元素是唯一的，不能有重复）。在之前的代码中，所有的请求都被存储在一个列表中，即使有重复。

这段代码使用了 'json.dumps()' 函数将请求数据转换为 JSON 格式进行存储，而之前的代码没有这一步骤。

总的来说，这段代码在提取 POST 请求的基础上，增加了对重复请求的处理，并且将结果以 JSON 格式写入到文件中，使得结果更方便后续处理和分析。
