transformer_def_load = """
{0} = AutoModelForCausalLM.from_pretrained("{1}", device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("{1}", use_fast=False, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
data = load_dataset('text', data_files='{2}')
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
def tokenize_function(examples):
    return tokenizer(examples["text"])
tokenized_data = data.map(tokenize_function, batched=True)
model.generation_config = GenerationConfig.from_pretrained("{1}")
print("模型加载成功")
"""

transformer_def_scratch = """
tokenizer = AutoTokenizer.from_pretrained("checkpoints/gpt2", use_fast=False, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
config = AutoConfig.from_pretrained(
    "checkpoints/gpt2",
    vocab_size=len(tokenizer),
    n_embd={1},
    n_head={2},
    n_layer={3},
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
)
{0} = GPT2LMHeadModel(config)
data = load_dataset('text', data_files='{4}')
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
def tokenize_function(examples):
    return tokenizer(examples["text"])
tokenized_data = data.map(tokenize_function, batched=True)
print("模型加载成功")
"""

transformer_import = """from transformers import AutoTokenizer, AutoModelForCausalLM, GPT2LMHeadModel, AutoConfig
from transformers import Trainer, TrainingArguments
from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling
from transformers.generation.utils import GenerationConfig
import torch
def generate(model,input):
    model_inputs = tokenizer([input], return_tensors="pt").to("cuda")
    generated_ids = model.generate(**model_inputs)
    output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(output)
"""

transformer_train = """training_args = TrainingArguments(
    output_dir='results',
    num_train_epochs={1},   
    per_device_train_batch_size={2},
    learning_rate={3}
)
trainer = Trainer(
    model={0},
    args=training_args,
    train_dataset=tokenized_data["train"],
    data_collator=data_collator,
)
trainer.train()
"""

transformer_pred = """generate({0},'{1}')
"""

transformer_chat = 'messages = [{"role": "user", "content": "{1}"}]\nresponse = {0}.chat(tokenizer, messages)'

transformer_save = """{0}.save_pretrained('{1}')
"""

mlp_import = """import json
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim

class TextClassifierMLP(nn.Module):
    def __init__(self, layers):
        super(TextClassifierMLP, self).__init__()
        self.layers = nn.ModuleList()
        for i in range(len(layers) - 1):
            self.layers.append(nn.Linear(layers[i], layers[i + 1]))
            if i < len(layers) - 2:  # 不在最后一层添加ReLU激活函数
                self.layers.append(nn.ReLU())

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    

def tokenize(text,input_size=100,):
    text_feat = torch.tensor([ord(c) for c in text], dtype=torch.float32)
    if len(text_feat) < input_size:
        text_feat = torch.cat([text_feat, torch.zeros(input_size - len(text_feat))])
    elif len(text_feat) > input_size:
        text_feat = text_feat[:input_size]
    return text_feat

class TextDataset(Dataset):
    def __init__(self, filename,input_size):
        with open(filename, 'r') as file:
            self.data = [json.loads(line) for line in file]
        self.input_size=input_size
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data[idx]['text']
        label = self.data[idx]['label']
        # 将文本转换为数字张量
        text_tensor = tokenize(text,input_size=self.input_size)
        return text_tensor, label
"""

mlp_def_load = """{0} = torch.load('{1}')
criterion = nn.CrossEntropyLoss()
input_size = {0}.layers[0].in_features
output_size = {0}.layers[-1].out_features
dataset = TextDataset('{2}',input_size)
"""

mlp_def_scratch="""{0} = TextClassifierMLP({1})
criterion = nn.CrossEntropyLoss()
input_size = {0}.layers[0].in_features
# 加载数据集
dataset = TextDataset('{2}',input_size)
"""

mlp_train = """optimizer = optim.Adam({0}.parameters(), lr={3})
batch_size={2}
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 训练模型
for epoch in range({1}):  # 举例训练10个epoch
    for text_feats, labels in dataloader:
        # 前向传播
        outputs = {0}(text_feats)
        loss = criterion(outputs, labels)

        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print('Epoch', (epoch+1)/{1}, 'Loss:', loss.item())
"""

mlp_pred="""text = '{1}'
input_size = {0}.layers[0].in_features
text_feat = tokenize(text,input_size)
output = {0}(text_feat)
pred_class = torch.argmax(output).item()
print("预测为第",pred_class,"类")
"""

mlp_save="""torch.save({0}, '{1}')
"""