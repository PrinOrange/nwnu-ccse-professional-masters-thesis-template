# 西北师范大学 专业硕士学位论文模板



本模板遵循计算机科学与工程学院论文格式标准。**适用于计算机科学与工程学院专业硕士学位论文。**

本模板是根据[官方下载](https://jsj.nwnu.edu.cn/2454/list.htm)中提供的 LaTeX 模板进行的改良版。在开始之前，请确保你的计算机上已经安装了 TeX 相关的编译工具，以及 Python 3.7 以上版本。

## 用法

开始之前你还需要安装 [ImageMagick](https://imagemagick.org/script/download.php)，它是把插图同义转换为 eps 格式的工具。

编译文档可以执行命令，在本项目下可生成 `Main.pdf` 文件

```bash
python make.py
```

清除编译中间产物可以执行命令

```bash
python clean.py
```

格式化所有的文档工程文件，可以执行

```bash
python format.py
```
