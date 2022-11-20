# taobao_card_export

 导出淘宝购物车到csv文件

#### 使用方法：

1. 打开浏览器，进入淘宝购物车页面。
2. 右键-检查，选择上面的Network ![1668959496879](image/README/1668959496879.png)
3. 刷新页面，然后滚动到你需要的内容，等待加载完成
4. 点击Type排序，点击type是xhr，文件名大概是*asyncGetMyCart.do? xxxxx 的文件，然后复制文件内容*
5. 从本目录下新建cart.json文件，粘贴，删除*asyncGetMyCart(* 及末尾右括号，只保留{}及其内容（json文件）
6. VScode点击运行，或者从本目录打开cmd之后运行 *python.exe extract.py* 具体运行方式自行查找

Note: 当加载下一页后，会生成下一份json文件，两份内容不同，需自行合并

#### 未做

* [ ] ！第一页预加载的无法被提取！
* [ ] 商店名shopName，卖家seller，目前导出为卖家
* [ ] 商品类型可以提取关键字保存
* [ ] 导出商店url
* [ ] 导出发货时间
* [ ] 导出商品id
* [ ] 自动合并多份json文件

###### 后话

有json文件，比想的简单很多，是某个项目采购要用于是叫上Copilot写的。 商店名和卖家用户名emmmm。
