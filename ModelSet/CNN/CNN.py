from ModelSet.data import *
from ModelSet.CNN.model_process import process

def cnn(test_data_path: str) -> str:
    # 获取训练数据
    train_data_path, column_to_delete = get_cnn_data()

    # 数据读取并处理
    test_data = drop_column(load_data(test_data_path, ' ', None), column_to_delete)
    train_data = drop_column(load_data(train_data_path, ' ', None), column_to_delete)

    # 进行模型训练
    result = process(train_data, test_data)

    ''' 
    process返回的是一个以字符串为键的python字典类型对象
    python和json字典中字符串的区别是：python使用单引号(')，而json使用双引号(")
    '''
    # 将python的dict类型转换为json字符串并返回
    return str(result).replace('\'', '\"')
