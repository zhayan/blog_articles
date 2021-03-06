---
title: 知识总结-Linux
date: 2021-01-30 14:52:57
toc: true
tags:
- 面试 
- Linux
categories:
- 招聘
---

记录Linux学习中相对重要的点和常用知识、技能
参考了[Linux Tool Quick Tutorial](https://linuxtools-rst.readthedocs.io/zh_CN/latest/index.html)

<!-- more -->

# Linux基础及常用命令

## 帮助型命令

### whatis
简要说明命令的作用
参数 `-w` 正则匹配 

### info 
更加详细的命令说明，（测试无法使用）

### man
查询命令的说明文档
九个类别

### which 
查看程序的路径

### whereis
查看命令多个可能的位置（多个版本等）

## 文件管理命令

### 创建和删除
+ 创建：mkdir
+ 删除：rm (删除非空目录 `-rf`) 
+ 移动：mv
+ 复制：cp (复制目录：cp -r )

### 目录切换
+ 找到文件/目录位置：cd
+ 切换到上一个工作目录： cd -
+ 切换到home目录： *cd* or cd ~
+ 显示当前路径: pwd
+ 更改当前工作路径为path: $cd path

### 列出目录项
+ 显示当前目录下的文件 ls
+ 按时间排序，以列表的方式显示目录项 ls -lrt
+ 给每项文件前面增加一个id编号(看上去更加整洁) ls | cat -n
+ 按页查看 more 

### 查找目录及文件
+ 实时查找 find
+ 更快的查询 locate，locate会为文件系统建立索引数据库，如果有文件更新，需要定期执行更新命令 updatedb 来更新索引库

### 查看文件内容
+ 查看文件: cat vi head tail more
+ 显示时同时显示行号: cat -n
+ 按页显示列表内容: ls -al | more
+ 显示文件第一行: head -1 filename
+ 显示文件倒数第五行: tail -5 filename
+ 查看两个文件间的差别: diff file1 file2
+ 动态显示文本最新信息: tail -f crawler.log

### 查找文件内容
egrep查询文件内容:
+ egrep '03.1\/CO\/AE' TSF_STAT_111130.log.012
+ egrep 'A_LMCA777:C' TSF_STAT_111130.log.035 > co.out2

### 文件与目录权限修改
+ 改变文件的拥有者 chown
+ 改变文件读、写、执行等属性 chmod
+ 递归子目录修改： chown -R tuxapp source/
+ 增加脚本可执行权限： chmod a+x myscript

### 命令间
+ 批处理命令连接执行，使用 |
+ 串联: 使用分号 ;
+ 前面成功，则执行后面一条，否则，不执行:&&
+ 前面失败，则后一条执行: ||
*todo* [Shell 输入/输出重定向](https://www.runoob.com/linux/linux-shell-io-redirections.html)


## 文本处理

### find 文件查找
+ 查找txt和pdf文件: find . \( -name "*.txt" -o -name "*.pdf" \) -print
+ 否定参数 `!`,查找所有非txt文本: find . ! -name "*.txt" -print
+ 指定搜索深度`-maxdepth`,同时有`depth`,打印出当前目录的文件（深度为1）: find . -maxdepth 1 -type f
+ 按类型搜索: `-type` f 文件 / l 符号链接 / d 目录
+ 按时间搜索
    - atime 访问时间 (单位是天，分钟单位则是-amin，以下类似）
    - mtime 修改时间 （内容被修改）
    - ctime 变化时间 （元数据或权限变化）
+ 找到后的后续动作
    - 参数`-delete`删除
    - 执行动作,参数`-exec`
    - `-print`使用‘\n’作为文件定界符，`-print0`使用‘\0’作为定界符，用于搜索包含空格的文件

### grep 文本搜索
```
grep match_patten file // 默认访问匹配行
```
+ `-o` 只输出匹配的文本行 VS `-v` 只输出没有匹配的文本行
+ `-c` 统计文件中包含文本的次数
+ `-n` 打印匹配的行号
+ `-i` 搜索时忽略大小写
+ `-l` 只打印文件名
+ 在多级目录中对文本递归搜索(程序员搜代码的最爱）: grep "class" . -R -n
+ 匹配多个模式: grep -e "class" -e "vitural" file
+ grep输出以0作为结尾符的文件名（-z）: grep "test" file* -lZ| xargs -0 rm

### xargs 命令行参数转换
+ `-d` 定义定界符 （默认为空格 多行的定界符为 n）
+ `-n` 指定输出为多行
+ `-I {}` 指定替换字符串，这个字符串在xargs扩展时会被替换掉,用于待执行的命令需要多个参数时
+ `-0`：指定0为输入定界符
+ `-P 10` 十线程执行
*更多参考[xargs 命令教程(阮一峰)](https://www.ruanyifeng.com/blog/2019/08/xargs-tutorial.html)*

### sort 排序
+ `-n` 按数字进行排序 VS `-d` 按字典序进行排序
+ `-r` 逆序排序
+ `-k` N 指定按第N列排序
+ 忽略像空格之类的前导空白字符: sort -bd data  

### uniq 消除重复行
默认消除重复行
+ `-c` 统计各行在文件中出现的次数
+ `-d` 找出重复行
+ `-s` 开始位置 
+ `-w` 比较字符数

### tr 进行转换字符
```
echo 12345 | tr '0-9' '9876543210' //加解密转换，替换对应字符
cat text| tr '\t' ' '  //制表符转空格
```
+ `-d` 删除字符
+ `-c` 使用给定字符串的补集
+ `-s` 压缩文本中出现的重复字符；最常用于压缩多余的空格
+ tr中可用各种字符类：
    - alnum：字母和数字
    - alpha：字母
    - digit：数字
    - space：空白字符
    - lower：小写
    - upper：大写
    - cntrl：控制（非可打印）字符
    - print：可打印字符

```
tr '[:lower:]' '[:upper:]'
```

### cut 按列切分文本
+ 截取文件的第2列和第4列 cut -f2,4 filename
+ 去文件除第3列的所有列 cut -f3 --complement filename
+ `-d` 指定定界符 cat -f2 -d";" filename
+ cut 取的范围
    - N- 第N个字段到结尾
    - -M 第1个字段到M
    - N-M N到M个字段
+ cut 取的单位
    - `-b` 以字节为单位
    - `-c` 以字符为单位
    - `-f` 以字段为单位（使用定界符）

**paste 按列拼接文本 `-d`指明定界符**

### wc 统计行和字符的工具
+ wc -l file // 统计行数
+ wc -w file // 统计单词数
+ wc -c file // 统计字符数

### sed 文本替换利器
+ 首处替换: sed 's/text/replace_text/' file   //替换每一行的第一处匹配的text
+ 全局替换: sed 's/text/replace_text/g' file
+ 默认替换后，输出替换后的内容，如果需要直接替换原文件,使用`-i`: sed -i 's/text/repalce_text/g' file

### awk 数据流处理工具
awk脚本结构
```
awk ' BEGIN{ statements } statements2 END{ statements } '
```
1. 执行begin中语句块；
2. 从文件或stdin中读入一行，然后执行statements2，重复这个过程，直到文件全部被读取完毕；
3. 执行end语句块；
###  其他
查看文件类型: file filename
以ASCII字符显示文件: od -c filename

## 系统状态

### 磁盘文件
+ df -h 查看磁盘空间利用 -h: human缩写，以易读的方式显示结果
+ du -sh -h 人性化显示 `-s` 递归整个目录的大小

### 打包压缩
打包是将多个文件归并到一个文件: tar -cvf etc.tar /etc <==仅打包，不压缩！
+ -c :打包选项
+ -v :显示打包进度
+ -f :使用档案文件
+ 解包: tar -xvf demo.tar, -x 解包选项

tar解压参数说明：
+ -z 解压gz文件
+ -j 解压bz2文件
+ -J 解压xz文件

压缩: gzip demo.txt,生成 demo.txt.gz
解压缩：gunzip demo.tar.gz, 生成demo.tar
同理bz2等

### CPU监控
+ 查看CPU使用率：sar -u 1 2，每1秒采样一次，总共采样2次；
+ 查看CPU平均负载：sar -q 1 2

### 内存监控
+ 内存使用状况：sar -r 1 2
+ 查看内存使用量：free -m
+ 查看页面交换发生状况 页面发生交换时，服务器的吞吐量会大幅下降；服务器状况不良时，如果怀疑因为内存不足而导致了页面交换的发生，可以使用sar -W这个命令来确认是否发生了大量的交换
+ 当系统中sar不可用时，可以使用以下工具替代：linux下有 vmstat、Unix系统有prstat
    - 查看cpu、内存、使用情况： vmstat n m （n 为监控频率、m为监控次数）
    - 使用watch 工具监控变化 当需要持续的监控应用的某个数据变化时，watch工具能满足要求；

## 进程管理

### 进程查询
+ 查询正在运行的进程信息 ps -ef
+ 查询归属于用户colin115的进程 ps -ef | grep colin115 或 ps -lu colin115
+ 查询进程ID（适合只记得部分进程字段） pgrep 查找进程 eg:查询进程名中含有re的进程 pgrep -l re
+ 以完整的格式显示所有的进程 ps -ajx
+ 显示进程信息，并实时更新: top，输入字符命令后显示相应的进程状态
    - P：根据CPU使用百分比大小进行排序。
    - M：根据驻留内存大小进行排序。
    - i：使top不显示任何闲置或者僵死进程。
+ lsof命令查看文件使用：
    - 查看端口占用的进程状态：lsof -i:3306
    - 查看用户username的进程所打开的文件:lsof -u username
    - 查询init进程当前打开的文件:lsof -c init
    - 查询指定的进程ID(23295)打开的文件：lsof -p 23295
    - 查询指定目录下被进程开启的文件（使用+D 递归目录）：lsof +d mydir1/
+ lsof（list open files）是一个列出当前系统打开文件的工具。在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。
+ 查询7902端口现在运行什么程序:
    - 第一步，查询使用该端口的进程的PID；lsof -i:7902
    - 使用ps工具查询进程详情：ps -fe | grep 30294
+ 使用命令pmap，来输出进程内存的状况，可以用来分析线程堆栈。

### 终止进程
+ 杀死指定PID的进程 (PID为Process ID)：kill PID
+ 杀死相关进程：kill -9 3434
+ 杀死job工作 (job为job number)：kill %job(job可以理解为shell的命令)

```bash
#将用户colin115下的所有进程名以av_开头的进程终止:
ps -u colin115 |  awk '/av_/ {print "kill -9 " $1}' | sh
#将用户colin115下所有进程名中包含HOST的进程终止:
ps -fe| grep colin115|grep HOST |awk '{print $2}' | xargs kill -9;
```

## 网络相关

### 查询网络服务和端口
+ 列出所有端口 (包括监听和未监听的): netstat -a
+ 列出所有 tcp 端口: netstat -at
+ 列出所有有监听的服务状态: netstat -l

### 网络路由
+ 查看路由状态: route -n
+ 发送ping包到地址IP: ping IP
+ 探测前往地址IP的路由路径: traceroute IP
+ DNS查询，寻找域名domain对应的IP: host domain
+ 反向DNS查询: host IP

### 镜像下载
直接下载文件或者网页:
wget url
常用选项:
+ `–limit-rate` :下载限速
+ `-o`：指定日志文件；输出都写入日志；
+ `-c`：断点续传

## 用户管理

## 系统

### 版本、时间、硬件

### IPC资源（Inter-Process Communication）
+ 查看系统使用的IPC共享内存资源: ipcs -m
+ 查看系统使用的IPC队列资源: ipcs -q
+ 查看系统使用的IPC信号量资源: ipcs -s
+ 应用示例：查看IPC资源被谁占用有个IPCKEY：51036 ，需要查询其是否被占用；
    - 首先通过计算器将其转为十六进制:51036 -> c75c
    - 如果知道是被共享内存占用: ipcs -m | grep c75c
    - 如果不确定，则直接查找: ipcs | grep c75c