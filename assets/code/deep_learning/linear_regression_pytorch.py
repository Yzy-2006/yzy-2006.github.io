import torch
from torch import nn
from torch.utils import data
from d2l import torch as d2l


def load_array(data_arrays, batch_size, is_train=True):
    """构造一个 PyTorch 数据迭代器"""
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=is_train
    )


def main():
    # =========================
    # 1. 生成模拟数据
    # =========================
    true_w = torch.tensor([2.0, -3.4])
    true_b = 4.2

    # 生成 1000 个样本
    features, labels = d2l.synthetic_data(
        true_w,
        true_b,
        1000
    )

    # =========================
    # 2. 构造数据迭代器
    # =========================
    batch_size = 10
    data_iter = load_array(
        (features, labels),
        batch_size
    )

    # =========================
    # 3. 定义线性回归模型
    # =========================
    # 输入特征数为 2，输出数为 1
    net = nn.Sequential(
        nn.Linear(2, 1)
    )

    # 初始化权重：均值 0，标准差 0.01
    net[0].weight.data.normal_(0, 0.01)

    # 初始化偏置为 0
    net[0].bias.data.fill_(0)

    # =========================
    # 4. 定义损失函数
    # =========================
    loss = nn.MSELoss()

    # =========================
    # 5. 定义优化器
    # =========================
    trainer = torch.optim.SGD(
        net.parameters(),
        lr=0.03
    )

    # =========================
    # 6. 训练模型
    # =========================
    num_epochs = 3

    for epoch in range(num_epochs):
        for X, y in data_iter:
            # 前向传播并计算损失
            l = loss(net(X), y)

            # 清空上一次计算得到的梯度
            trainer.zero_grad()

            # 反向传播，计算梯度
            l.backward()

            # 根据梯度更新参数
            trainer.step()

        # 每个 epoch 结束后计算全部训练数据的损失
        with torch.no_grad():
            epoch_loss = loss(net(features), labels)

        print(
            f"epoch {epoch + 1}, "
            f"loss {epoch_loss.item():.6f}"
        )

    # =========================
    # 7. 查看最终学习结果
    # =========================
    learned_w = net[0].weight.data.reshape(true_w.shape)
    learned_b = net[0].bias.data

    print("\n训练完成")
    print(f"真实权重 true_w: {true_w}")
    print(f"学习权重 learned_w: {learned_w}")
    print(f"权重误差: {true_w - learned_w}")

    print(f"\n真实偏置 true_b: {true_b}")
    print(f"学习偏置 learned_b: {learned_b.item():.6f}")
    print(f"偏置误差: {true_b - learned_b.item():.6f}")


if __name__ == "__main__":
    main()
