#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
from pathlib import Path


def usage():
    """打印使用说明"""
    print("用法: python CleanMCA.py --mca <白名单文件> --region <region目录>")
    print("参数:")
    print("      --mca, -m: 指定 mca 文件白名单文件的路径")
    print("      --region, -r: 指定存档的 region 目录路径")
    sys.exit(1)


def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="Minecraft 存档 MCA 文件清理工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python CleanMCA.py -m whitelist.txt -r /path/to/world/region
  python CleanMCA.py --mca whitelist.txt --region /path/to/world/region
        """
    )
    
    parser.add_argument(
        '-m', '--mca',
        dest='whitelist_path',
        required=True,
        help='指定 mca 文件白名单文件的路径'
    )
    
    parser.add_argument(
        '-r', '--region',
        dest='region_path',
        required=True,
        help='指定存档的 region 目录路径'
    )
    
    return parser.parse_args()


def load_whitelist(whitelist_path):
    """加载白名单文件"""
    try:
        with open(whitelist_path, 'r', encoding='utf-8') as f:
            # 读取所有行并去除空白字符
            whitelist = set(line.strip() for line in f if line.strip())
        return whitelist
    except FileNotFoundError:
        print(f"白名单文件不存在: {whitelist_path}")
        sys.exit(1)
    except Exception as e:
        print(f"读取白名单文件时出错: {e}")
        sys.exit(1)


def process_directory(dir_path, whitelist):
    """处理目录，删除不在白名单中的文件"""
    if not dir_path.is_dir():
        print(f"目录不存在: {dir_path}")
        return
    
    print(f"正在处理目录: {dir_path}")
    
    deleted_count = 0
    for file_path in dir_path.iterdir():
        if file_path.is_file():
            filename = file_path.name
            if filename not in whitelist:
                try:
                    print(f"删除文件: {file_path.absolute()}")
                    file_path.unlink()
                    deleted_count += 1
                except Exception as e:
                    print(f"删除文件失败 {file_path}: {e}")
    
    print(f"目录 {dir_path} 处理完成，删除了 {deleted_count} 个文件")


def main():
    """主函数"""
    args = parse_arguments()
    
    # 转换为 Path 对象并获取绝对路径
    whitelist_path = Path(args.whitelist_path).resolve()
    region_path = Path(args.region_path).resolve()
    
    # 检查白名单文件是否存在
    if not whitelist_path.is_file():
        print(f"白名单文件不存在: {whitelist_path}")
        sys.exit(1)
    
    # 计算相关路径
    poi_path = region_path.parent / "poi"
    entities_path = region_path.parent / "entities"
    
    # 检查目录是否存在
    directories_to_check = [
        ("Region", region_path),
        ("POI", poi_path),
        ("Entities", entities_path)
    ]
    
    for name, path in directories_to_check:
        if not path.is_dir():
            print(f"{name} 目录不存在: {path}")
            sys.exit(1)
    
    # 加载白名单
    whitelist = load_whitelist(whitelist_path)
    
    # 显示处理内容预览
    print(">>> 处理内容预览 <<<")
    print(f"白名单文件: {whitelist_path}，共计 {len(whitelist)} 个文件")
    print(f"区块文件路径: {region_path}")
    print(f"POI 文件路径: {poi_path}")
    print(f"实体文件路径: {entities_path}")
    
    # 确认操作
    try:
        response = input("此操作不可逆，请确认已备份好存档。是否继续？(y/n) ").lower().strip()
        if response not in ['y', 'yes', '是']:
            print("操作已取消")
            sys.exit(0)
    except KeyboardInterrupt:
        print("\n操作已取消")
        sys.exit(0)
    
    print("\n开始处理...")
    
    # 处理三个目录
    directories_to_process = [region_path, poi_path, entities_path]
    
    for directory in directories_to_process:
        process_directory(directory, whitelist)
        print()  # 添加空行分隔
    
    print("处理完成")


if __name__ == "__main__":
    main()
