import os
import sys

'''传入相对路径获取文件绝对路径，用于打包后资源文件路径变更'''

def get_resource_path(relative_path):
    """获取打包后的资源文件路径"""
    try:
        # PyInstaller 打包后的临时目录
        base_path = sys._MEIPASS
    except AttributeError:
        # 开发环境
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
