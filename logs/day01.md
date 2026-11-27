# Day01

做了：建仓库、开机器、装 cu128 的 torch、存镜像
数字：torch 2.7.0 / cuda True / 显存 24G / 算力 (8, 9)
卡在哪：pip 先装了 CPU 版，torch.cuda.is_available() 返回 False，卸载重装才对
