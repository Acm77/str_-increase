# str_-increase
灵感来源于itertools.cycle，使用python解决对自定义6位字符串的增长问题

适用于短链生成服务，邀请码，主键等字符串短且去重的场景，若需分布式使用，请将diy_str放置一个位置(例:redis,mysql)，并使用分布式锁(例:zk, redis等)对其进行改动过程控制。

这段代码应该有更优的写法，请不吝赐教。

本项目中六位字符串可得到56800235584位自增的数据，如果需要扩容或缩容只需将项目内all_str改成自定义的字符串即可

#### 使用方式：
``` python
order_str = OrderStr(diy_str='abcDE1', ret_num=100)
order_str_list = order_str.get_order_str()
print(order_str_list)
```

#### 得到的结果:
``` python
['abcDE2', 'abcDE3', 'abcDE4', 'abcDE5', 'abcDE6', 'abcDE7', 'abcDE8', 'abcDE9', 'abcDEa', 'abcDEb', 'abcDEc', 'abcDEd', 'abcDEe', 'abcDEf', 'abcDEg', 'abcDEh', 'abcDEi', 'abcDEj', 'abcDEk', 'abcDEl', 'abcDEm', 'abcDEn', 'abcDEo', 'abcDEp', 'abcDEq', 'abcDEr', 'abcDEs', 'abcDEt', 'abcDEu', 'abcDEv', 'abcDEw', 'abcDEx', 'abcDEy', 'abcDEz', 'abcDEA', 'abcDEB', 'abcDEC', 'abcDED', 'abcDEE', 'abcDEF', 'abcDEG', 'abcDEH', 'abcDEI', 'abcDEJ', 'abcDEK', 'abcDEL', 'abcDEM', 'abcDEN', 'abcDEO', 'abcDEP', 'abcDEQ', 'abcDER', 'abcDES', 'abcDET', 'abcDEU', 'abcDEV', 'abcDEW', 'abcDEX', 'abcDEY', 'abcDEZ', 'abcDF0', 'abcDF1', 'abcDF2', 'abcDF3', 'abcDF4', 'abcDF5', 'abcDF6', 'abcDF7', 'abcDF8', 'abcDF9', 'abcDFa', 'abcDFb', 'abcDFc', 'abcDFd', 'abcDFe', 'abcDFf', 'abcDFg', 'abcDFh', 'abcDFi', 'abcDFj', 'abcDFk', 'abcDFl', 'abcDFm', 'abcDFn', 'abcDFo', 'abcDFp', 'abcDFq', 'abcDFr', 'abcDFs', 'abcDFt', 'abcDFu', 'abcDFv', 'abcDFw', 'abcDFx', 'abcDFy', 'abcDFz', 'abcDFA', 'abcDFB', 'abcDFC', 'abcDFD']
```
