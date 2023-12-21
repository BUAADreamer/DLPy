# dlpy: 面向深度学习的Python

## 环境配置
```shell
pip3 install -r requirements.txt
alias dlpy='python3 main.py' #如果需要cli直接运行
```

## 模型下载

将模型下载到checkpoints目录下或者自定义目录下

## 代码示例

`example/`目录下有常见dlpy代码示例，下面以baichuan2的聊天机器人为例：
```python
model:transformer='checkpoints/baichuan2-7b-chat':'dataset/wiki.txt';
while True{
    print('User:');
    x=scan();
    print('Bot:');
    chat model x;
}
```

## 代码运行
```shell
python3 main.py example/sample.dlpy
#快捷运行
dlpy example/sample.dlpy
```

## 编译器完整运行结果
```shell
python3 test.py example/if.dlpy
```