# CleanMCA Python 版本

这是原始 Shell 脚本的 Python 版本，用于清理 Minecraft 存档中不需要的 MCA 文件。

## 功能

- 根据白名单文件保留指定的 MCA 文件
- 自动处理 `region`、`poi`、`entities` 三个目录
- 支持中文路径和文件名
- 提供详细的操作反馈
- 包含安全确认机制

## 使用方法

### 基本用法

```bash
python CleanMCA.py --mca <白名单文件> --region <region目录>
```

### 参数说明

- `--mca`, `-m`: 指定 MCA 文件白名单文件的路径
- `--region`, `-r`: 指定存档的 region 目录路径

### 使用示例

```bash
# 使用完整参数名
python CleanMCA.py --mca whitelist.txt --region "C:\Users\Username\AppData\Roaming\.minecraft\saves\MyWorld\region"

# 使用简短参数名
python CleanMCA.py -m whitelist.txt -r "C:\path\to\world\region"

# 在 Windows 下也可以使用批处理文件
CleanMCA.bat -m whitelist.txt -r "C:\path\to\world\region"
```

## 白名单文件格式

白名单文件应该是一个文本文件，每行包含一个要保留的文件名：

```
r.0.0.mca
r.0.1.mca
r.1.0.mca
r.1.1.mca
r.-1.-1.mca
```

- 支持以 `#` 开头的注释行
- 空行会被自动忽略
- 文件名大小写敏感

## 安全特性

1. **路径验证**: 自动检查所有必需的目录是否存在
2. **确认机制**: 执行删除操作前会要求用户确认
3. **详细日志**: 显示每个被删除文件的完整路径
4. **错误处理**: 对文件读取和删除操作进行异常处理

## 注意事项

⚠️ **重要警告**: 此操作不可逆，请务必在使用前备份您的存档！

1. 脚本会删除不在白名单中的所有文件
2. 建议先在测试存档上验证白名单文件的正确性
3. 确保白名单文件编码为 UTF-8
4. 路径中包含空格时请使用引号包围

## 系统要求

- Python 3.6 或更高版本
- Windows/Linux/macOS 系统

## 与原始 Shell 脚本的差异

1. **更好的错误处理**: 提供了更详细的错误信息
2. **跨平台支持**: 可在 Windows、Linux、macOS 上运行
3. **UTF-8 支持**: 更好地处理中文路径和文件名
4. **统计信息**: 显示处理的文件数量
5. **灵活的确认**: 支持多种确认输入方式

## 故障排除

### 常见问题

1. **编码错误**: 确保白名单文件使用 UTF-8 编码
2. **权限问题**: 确保对目标目录有写权限
3. **路径问题**: 使用绝对路径或正确的相对路径

### 调试模式

如需查看详细的执行信息，可以修改脚本添加调试输出，或者在出现问题时检查错误信息。
