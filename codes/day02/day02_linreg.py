#任务A
#1.造数据：
import torch
torch.manual_seed(0)
X = torch.randn(200,2)
w_true,b_true = torch.tensor([2.0,-3.4]),torch.tensor(4.2)
y = X @ w_true + b_true + 0.01 * torch.randn(200) #5对照实验 torch.randn(200, 1)
print(X.shape)
print(y.shape)

#2.待学参数：
w = torch.zeros(2, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
print(w.shape)
print(w.requires_grad)

#3.损失函数：
def loss_fn():
    return 0.5 * ((X @ w + b - y) ** 2).mean()
print(loss_fn())

#4.训练循环
lr = 0.1
for step in range(1,201):
    loss = loss_fn()
    loss.backward()#反向传播求梯度
    with torch.no_grad():#更新参数
        w -= lr * w.grad
        b -= lr * b.grad
    w.grad.zero_()#清零梯度
    b.grad.zero_()
    if step % 20 == 0:
        print(step, round(loss.item(),6), w.tolist(), b.item())

#检测
assert torch.allclose(w.detach(), w_true, atol=0.05)
assert abs(b.item() - b_true.item()) < 0.05
assert loss.item() < 0.01
print("PASS A")