---
title: 【每日一题_基础】TCP分段和IP分片
date: 2021-03-17 20:52:55
toc: true
tags:
- 面试 
- 计算机网络
categories:
- 每日一题_基础
---
TCP报文段如果很长的话，会在发送时发生分段(Segmentation)，在接收时进行重组，同样IP数据报在长度超过一定值时也会发生分片(Fragmentation)，在接收端再将分片重组。
https://cloud.tencent.com/developer/article/1173790

<!-- more -->

## 要点
最大传输单元(Maximum Transmission Unit)，即MTU，为数据链路层的最大载荷上限(即IP数据报最大长度)，每段链路的MTU可能都不相同，一条端到端路径的MTU由这条路径上MTU最小的那段链路的MTU决定。以以太网为例，MTU通常为1500字节，采用巨帧(Jumbo Frame)时可以达到9000字节。所谓的MTU，

最大报文段长度(Maximum Segment Size)，即MSS，为TCP传输层的最大载荷上限(即应用层数据最大长度)，TCP三次握手期间通过TCP首部选项中的MSS字段通知对端，通常一条TCP连接的MSS取通信双方较小的那一个MSS值，

MSS与MTU的换算关系为：MTU = MSS + TCP首部长度 + IP首部长度

以太网中(网络层以IPv4为例)：MSS = 以太网MTU - TCP首部长度 - IPv4首部长度 = 1500 - 20 - 20 = 1460字节

UDP不会分段，就由IP来分片。TCP会分段，当然就不用IP来分了。

在分片的数据中，传输层的首部只会出现在第一个分片中，IP数据报分片后，只有第一片带有传输层首部(UDP或ICMP等)，而TCP报文段的每个分段中都有TCP首部，到了目的地后根据TCP首部的信息在传输层进行重组。

TCP分段技术被提出后，在一定程度上减少了IP分片，但是却不能保证在整个端到端通信路径上不会发生IP分片。

IP首部中有三个标志位，第一位预留，第二位DF(Don’t Fragment)，第三位MF(More Fragments)。DF置1，通过是否丢包，ICMP通知MTU，
