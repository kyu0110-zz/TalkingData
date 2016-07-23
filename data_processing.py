import numpy as np

def translate_brand_names(phone_data):
    chinese_brands = ['三星','天语', '海信', '联想', '欧比', '爱派尔', '努比亚', '优米', '朵唯', '黑米', '锤子', '酷比魔方', '美图',
                 '尼比鲁', '一加', '优购', '诺基亚', '糖葫芦', '中国移动', '语信', '基伍', '青橙', '华硕', '夏新', '维图', 
                  '艾优尼', '摩托罗拉', '乡米', '米奇', '大可乐', '沃普丰', '神舟','摩乐', '飞秒', '米歌', '富可视', '德赛',
                  '梦米', '乐视', '小杨树', '纽曼', '邦华', 'E派', '易派', '普耐尔', '欧新', '西米', '海尔', '波导', '糯米', 
                  '唯米', '酷珀', '谷歌', '昂达', '聆韵', '小米']
    english_brands = ['samsung', 'Ktouch', 'hisense', 'lenovo', 'obi', 'ipair', 'nubia', 'youmi', 'dowe', 'heymi', 
                  'hammer', 'koobee', 'meitu', 'nibilu', 'oneplus', 'yougo', 'nokia', 'candy', 'ccmc', 'yuxin', 
                  'kiwu', 'greeno', 'asus', 'panasonic', 'weitu', 'aiyouni', 'motorola', 'xiangmi', 'micky', 
                  'bigcola', 'wpf', 'hasse', 'mole', 'fs', 'mige', 'fks', 'desci', 'mengmi', 'Ishi', 'smallt',
                  'newman', 'banghua', 'epai', 'epai', 'pner', 'ouxin', 'ximi', 'haier', 'bodao', 'nuomi', 'weimi', 
                  'kupo', 'google', 'ada', 'lingyun', 'xiaomi']

    if (len(chinese_brands) != len(english_brands)):
        print('ERROR, brand names do not match')

    for i in range(0, len(chinese_brands)):
        phone_data.loc[phone_data['phone_brand'] == chinese_brands[i], 'phone_brand'] = english_brands[i]

    return phone_data


def filter_minor_categories(data, category_name, index_name, min_users):
    # add additional clumn for phone brand index
    data[index_name] = 0

    data_unique = data.groupby(category_name).first()
    categories = data_unique.index.unique()

    minor_categories = np.where(data.groupby(category_name).size() < min_users)
    ind = 1

    for i in range(0, len(categories)):
        if i in minor_categories[0]:
            data.loc[data[category_name] == categories[i], index_name] = 0
        else:
            data.loc[data[category_name] == categories[i], index_name] = ind
            ind += 1

    return data


def assign_index(data, column_name, index_name):

    # add additional column
    data[index_name] = 0

    groups = data[column_name].unique()
    groups.sort()

    ind = 0
    for group in groups:
        data.loc[data[column_name] == group, index_name] = ind
        ind += 1

    return data
