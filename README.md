从开始写博客到现在也用过了不少博客应用，有的太过臃肿，有的则是太过配置太过繁杂或者是显示不尽人意，所以我就想自己写一个试一试。前端是tailwind CSS和VUE写的，后端准备先用Python的Django写后面再用go进行重写。





## API design

|                 URL                  | Method |          description           |
| :----------------------------------: | :----: | :----------------------------: |
| api/content?type=<string>&page=<int> |  GET   | 获取文章目录，默认一页为10条。 |
|      api/article?title=<string>      |  GET   |          获取文章正文          |
|               api/tags               |  GET   |          获取标签列表          |
|            api/categories            |  GET   |          获取分类列表          |

### Struct

1. api/content?type=<string>&page=<int>

   ```json
   {
       status: {true, false},
       msg: "string",
       data: [
           {
               title: "string",
               date: "string",
               text: "string",
           }
       ]
   }
   ```

2. 