[English Version](README.md)

# CleanMCA

CleanMCA 是一个用于清理 Minecraft 存档 region、poi 和 entities 目录下多余文件的 Bash 脚本。通过提供一个白名单文件，脚本会自动删除不在白名单中的 .mca 文件，帮助你精简存档，释放空间。

## 功能简介
- 根据白名单文件，仅保留指定的 .mca 文件。
- 同时处理 region、poi、entities 三个目录。
- 操作前会进行参数和路径检查，防止误删。
- 操作不可逆，需提前备份存档。

## 使用方法

### 1. 准备白名单文件
白名单文件为纯文本文件，每行一个 .mca 文件名，例如：
```
r.0.0.mca
r.0.1.mca
r.1.0.mca
```

使用 [Dominion](https://dominion.lunadeer.cn/) 插件可以根据领地自动生成白名单列表。

### 2. 运行脚本
在终端中执行：

```bash
bash CleanMCA.sh --mca <白名单文件路径> --region <region目录路径>
```
或使用短参数：
```bash
bash CleanMCA.sh -m <白名单文件路径> -r <region目录路径>
```

参数说明：
- `--mca` 或 `-m`：指定白名单文件路径。
- `--region` 或 `-r`：指定 Minecraft 存档的 region 目录路径。

### 3. 示例
```bash
bash CleanMCA.sh -m whitelist.txt -r /path/to/world/region
```

脚本会自动处理 region、poi、entities 三个目录，并删除不在白名单中的文件。

## 注意事项
- **操作不可逆，请务必提前备份存档！**
- 需要在支持 Bash 的环境下运行（如 Linux、WSL、Git Bash 等）。
- 需要 `getopt`、`realpath`、`grep` 等常用命令行工具。

## 许可证

本项目采用 MIT License。
