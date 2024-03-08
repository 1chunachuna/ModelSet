# 模型库

## 路径说明
```
.
├───data        # 存放模型需要的测试数据
│   ├───CNN         # CNN测试数据    
│   └───KNN         # KNN测试数据
└───ModelSet    # 存放模型代码和训练数据
    ├───ANN         # ANN模型代码
    ├───CNN         # CNN模型代码
    ├───KNN         # KNN模型代码
    └───data        # 模型训练数据
```
## 模型定义
每个模型都有对应的入口函数，入口函数接受**字符串**类型的参数并返回**json**字典字符串

> 编程风格推荐使用强类型

例如：
```python
# 仅供演示说明，请自行查看详细代码
def cnn(test_data_path: str) -> str:
    # 获取训练数据
    train_data_path, column_to_delete = get_cnn_data()

    # 数据读取并处理
    ...
    # 进行模型训练
    ...
    
    return str(result)
```

其中``result``为
```json
{
  "mse": [4.4654, 4.5412, ...],
  "loss": [40.4654, 41.5412, ...],
  "val_mse": [4.5654, 4.6412, ...],
  "val_loss": [39.4654, 40.5412, ...],
  "mean_mse": 4.4655,
  "total_score": 235.4561,
}
```