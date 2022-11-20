import json
import xlwt

# 开发者工具-Network,刷新界面并加载所需购物车内容.
# 按文件类型排序后获得https://cart.taobao.com/json/asyncGetMyCart.doxxx
# 复制内容,创建cart.json,粘贴内容
# 删除开头"asyncGetMyCart(" 与末尾")"
FILE_NAME = './cart.json'
SAVE_FILE_NAME = './tb_cart'

excel = xlwt.Workbook()
sheet = excel.add_sheet('tb_cart')

headers = ['店铺', '名称', '型号', '单价', '数量', '总价', '链接']
for col in range(len(headers)):
    sheet.write(0, col, headers[col])

row = 1
json_file = open(FILE_NAME, 'r', encoding='UTF-8')
t = json.load(json_file)
json_file.close()

shops = t['list']
for shop in shops:

    orders = shop['bundles'][0]['orders']
    shop_name = shop['seller']
    sheet.write(row, 0, shop_name)
    for order in orders:
        url = 'https:' + order['url']
        title = order['title']
        amount = order['amount']['now']
        price = order['price']['now']/100
        total = order['price']['sum']/100
        if(order['skuStatus'] == 2):
            skuId = order['skuId']
            color = str(order['skus'])
            url = url + '&skuId=' + skuId
        else:
            color = '--'

        print('Get: ', url, title, amount, price, total, color)
        sheet.write(row, 1, title)
        sheet.write(row, 2, color)
        sheet.write(row, 3, price)
        sheet.write(row, 4, amount)
        sheet.write(row, 5, total)
        sheet.write(row, 6, url)
        row += 1

excel.save('tb_cart.xls')
