#!/bin/bash

# 打印使用说明
usage() {
    echo "用法: $0 --mca <白名单文件> --region <region目录>"
    echo "参数:"
    echo "      --mca, -m: 指定 mca 文件白名单文件的路径"
    echo "      --region, -r: 指定存档的 region 目录路径"
    exit 1
}

# 使用 getopt 解析命令行参数
PARSED_ARGUMENTS=$(getopt -o m:r: --long mca:,region: -- "$@")
if [ $? -ne 0 ]; then
    usage
fi

eval set -- "$PARSED_ARGUMENTS"

# 初始化变量
WHITELIST_PATH=""
REGION_PATH=""

# 读取参数
while true; do
    case "$1" in
        -m|--mca)
            WHITELIST_PATH="$2"
            shift 2
            ;;
        -r|--region)
            REGION_PATH="$2"
            shift 2
            ;;
        --)
            shift
            break
            ;;
        *)
            usage
            ;;
    esac
done

# 检查必需的参数是否已提供
if [ -z "$WHITELIST_PATH" ] || [ -z "$REGION_PATH" ]; then
    usage
fi

# 检查白名单文件是否存在
if [ ! -f "$WHITELIST_PATH" ]; then
    echo "白名单文件不存在: $WHITELIST_PATH"
    exit 1
else
    WHITELIST_PATH=$(realpath "$WHITELIST_PATH")
fi

# 替换为绝对路径
REGION_PATH=$(realpath "$REGION_PATH")
POI_PATH=$(realpath "$REGION_PATH/../poi")
ENTITIES_PATH=$(realpath "$REGION_PATH/../entities")

# 检查 REGION_PATH, POI_PATH 和 ENTITIES_PATH 是否存在
if [ ! -d "$REGION_PATH" ]; then
    echo "Region 目录不存在: $REGION_PATH"
    exit 1
fi
if [ ! -d "$POI_PATH" ]; then
    echo "POI 目录不存在: $POI_PATH"
    exit 1
fi
if [ ! -d "$ENTITIES_PATH" ]; then
    echo "Entities 目录不存在: $ENTITIES_PATH"
    exit 1
fi


# 定义一个函数来处理文件夹
process_directory() {
    DIR_PATH=$1
    if [ ! -d "$DIR_PATH" ]; then
        echo "目录不存在: $DIR_PATH"
        return
    fi

    cd "$DIR_PATH" || exit 1

    # 遍历文件，删除不在白名单中的文件
    for FILE in *; do
        if ! grep -qx "$FILE" "$WHITELIST_PATH"; then
            R_PATH=$(realpath "$FILE")
            echo "删除文件: $R_PATH"
            rm -f "$FILE"
        fi
    done
}

echo ">>> 处理内容预览 <<<"
echo "白名单文件: $WHITELIST_PATH，共计 $(wc -l < "$WHITELIST_PATH") 个文件"
echo "区块文件路径: $REGION_PATH"
echo "POI 文件路径: $POI_PATH"
echo "实体文件路径: $ENTITIES_PATH"
read -p "此操作不可逆，请确认已备份好存档。是否继续？(y/n) " -n 1 -r

# 处理三个目录
process_directory "$REGION_PATH"
process_directory "$POI_PATH"
process_directory "$ENTITIES_PATH"

echo "处理完成"
