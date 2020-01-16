# str_-increase
灵感来源于itertools.cycle，使用python解决对自定义6位字符串的增长问题

适用于短链生成服务，邀请码，主键等字符串短且去重的场景

本项目中六位字符串可得到56800235584位自增的数据，如果需要扩容或缩容只需将项目内all_str改成自定义的字符串即可

#### 使用方式：
``` python
order_str = OrderStr(diy_str='000000', ret_num=10)
order_str_list = order_str.get_order_str()
print(order_str_list)
```
