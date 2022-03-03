# fastcmd

`fastcmd` 能够的建立快捷命令来替代一些输入繁琐的常见命令。这只需要使用 `set` 命令即可实现。 `set` 命令能够将任何命令前缀替换为快捷命令。语法如下：

```sh
fastcmd set [-g] <shortcut> <command prefix>
```

- `-g` 若带此参数，则将此改动应用到全局。
- `shortcut` 快捷命令名。请使用一个连续的字符串。
- `command prefix` 命令前缀。请用双引号括起。若命令内包含双引号，则需将这些双引号替换为单引号。

使用示例：

```sh
fastcmd set -g gitm "git commit -m"
```

键入后，将全局注册 `gitm` 命令。现在 `git commit -m <any message>` 将与下方命令等价：

```shell
gitm <any message>
```

`fastcmd` 甚至可以为自己的命令注册快捷命令，例如：

```shell
fastcmd set -g define "fastcmd set -g"
```

使用后，就可以使用 `define` 关键字来定义任意命令行语句了。



## 安装

安装前，确保已经安装有python 3（建议3.8+）

1. 自行选择一个你的应用安装位置，例如 `C:\Program Files` , 将代码仓库拷贝至此处；
2. 运行文件夹内的 `install.bat` 脚本；
3. 完成后，重启电脑（可能需要）即可。



## 完整命令集

