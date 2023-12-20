# dlpy: 面向深度学习的程序设计语言

## 环境配置
```shell
pip3 install -r requirements.txt
alias dlpy='python3 main.py'
```

## 代码示例

`example/`目录下有常见dlpy代码示例，下面以MLP为例：
```python
mlp_model:mlp=100,50,2:'dataset/class.txt'; #定义模型
train mlp_model 10,2,0.0001; #训练模型
pred mlp_model 'I love you'; #预测类别
```

## 代码运行
```shell
dlpy example/sample.dlpy
```