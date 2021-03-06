# coding=utf-8
# author: san shui
import string


class OrderStr:

    def __init__(self, diy_str='000000', ret_num=10):
        """
        结果共计56800235584位
        :param diy_str: 自定义起始值(不含)
        :param ret_num: 从起始值之后返回多少个数据
        """
        if len(diy_str) != 6 or not isinstance(diy_str, str):
            raise Exception('diy_str must be string and length 6')
        if ret_num > 100000:  # 防止内存占用过大
            raise Exception('ret_num must be less than 100000')
        self.all_str = string.digits + string.ascii_letters  # 数字 + 小写字母 + 大写字母
        self.diy_str = diy_str
        self.ret_num = ret_num
        self.end_char = self.all_str[-1]

    def __get_args(self):
        str_char_list = [i for i in self.diy_str]
        try:
            str_char_index_list = [self.all_str.index(j) for j in str_char_list]
        except Exception as e:
            raise Exception('every diy_str must be in all_str, error info: %s' % e)
        return str_char_list, str_char_index_list

    def __incr_iter(self):
        month, month_index = self.__get_args()
        diy_jan, diy_feb, diy_mar, diy_apr, diy_may, diy_jun = month  # 随便起了个变量名，对应的六位字符串
        diy_jan_index, diy_feb_index, diy_mar_index, diy_apr_index, diy_may_index, diy_jun_index = month_index
        jan_iter = self.all_str[diy_jan_index:]
        jan, feb, mar, apr, may, jun = '', '', '', '', '', '',

        for jan in jan_iter:

            for feb_index, feb in enumerate(self.all_str):
                if jan == diy_jan:
                    if feb_index < diy_feb_index:
                        continue

                for mar_index, mar in enumerate(self.all_str):
                    if jan == diy_jan and feb == diy_feb:
                        if mar_index < diy_mar_index:
                            continue

                    for apr_index, apr in enumerate(self.all_str):
                        if jan == diy_jan and feb == diy_feb and mar == diy_mar:
                            if apr_index < diy_apr_index:
                                continue

                        for may_index, may in enumerate(self.all_str):
                            if jan == diy_jan and feb == diy_feb and mar == diy_mar and apr == diy_apr:
                                if may_index < diy_may_index:
                                    continue

                            for jun_index, jun in enumerate(self.all_str):
                                if jan == diy_jan and feb == diy_feb and mar == diy_mar and apr == diy_apr and \
                                        may == diy_may:
                                    if jun_index <= diy_jun_index:
                                        continue

                                yield jan + feb + mar + apr + may + jun

        if jan == self.end_char and \
                feb == self.end_char and \
                mar == self.end_char and \
                apr == self.end_char and \
                may == self.end_char and \
                jun == self.end_char:
            raise Exception('There Is No Data !!!')

    def get_order_str(self):
        num = 0
        order_str_list = []
        for i in self.__incr_iter():
            order_str_list.append(i)
            num += 1
            if num >= self.ret_num:
                return order_str_list


if __name__ == '__main__':
    order_str = OrderStr(diy_str='abcDE1', ret_num=100)
    order_str_list = order_str.get_order_str()
    print(order_str_list)
