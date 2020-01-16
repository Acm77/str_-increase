# coding: utf-8
"""
==========================================
            转换工具
==========================================
"""


class StrTools(object):
    """
    字符串转换工具
    """
    char_set = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", 'z',
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", 'Z'
                )

    @classmethod
    def convert_10_to_62(cls, i):
        """
        10进制整数转成包含大小写字母的62进制
        :param i:
        :return:
        """
        result = ""
        i = int(i)
        while i >= 62:
            result = cls.char_set[i % 62] + result
            i = int(i / 62)
        result = cls.char_set[i] + result
        return result

    @classmethod
    def convert_62_to_10(cls, s):
        """
        包含大小写字母的62进制转成10进制整数
        :param i:
        :return:
        """
        result = 0
        for i, k in enumerate(s[::-1]):
            result += cls.char_set.index(k) * pow(62, i)
        return result


print(StrTools.convert_10_to_62(2222), StrTools.convert_62_to_10("zQ"))
