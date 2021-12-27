# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def chinese2num(n):
    num_dict = {'一': 1, '两': 2, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
                '百': 100,
                '千': 1000,
                '万': 10000}
    ret = 0
    n = n.replace('零', '')
    for item in reversed(num_dict):
        val = n.split(item)
        if len(val) > 1:
            if val[0] != '' and val[1] != '':
                ret = (chinese2num(val[0]) * num_dict.get(item)) + chinese2num(val[1])
                break
            elif val[0] != '':
                ret = chinese2num(val[0]) * num_dict.get(item)
                break
            elif val[1] != '':
                ret = chinese2num(val[1]) * num_dict.get(item)
                break
            else:
                ret = num_dict.get(item)
                break
    return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    val = input('请输入要转换的中文数字：')
    print(chinese2num(val))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
