---
title: 【基础】ARP和ARP攻击
date: 2021-03-17 21:42:52
toc: true
tags:
- 面试 
- 计算机网络
categories:
- 基础
---

在 OSI 参考模型中 ARP 协议位于链路层，但在 TCP/IP 中，它位于网络层。负责将某个IP地址解析成对应的MAC地址。

<!-- more -->
## 如何知道IP对应的MAC地址
1. 每台主机都会在自己的ARP缓冲区建立一个ARP列表（生命周期二十分钟），用于表示IP地址和MAC地址的对应关系。
2. 主机A若想和主机B通信，首先主机A会查询Arp缓存表（后面称ip-mac缓存表）是否有B主机对应的ip-mac，有的话就将B主机的mac地址封装到数据包发送。若没有的话，主机A会向以太网发送一个Arp广播包，告诉以太网内的所有主机自己的ip-mac，并请求B主机（以ip来表示B主机）的mac地址。当B主机收到Arp广播包后，确认A主机是想找自己的mac地址，就会对A主机进行回应一个自己的mac地址。A主机就会更新自己的ip-mac缓存表，同时B主机也会接收A主机的ip-mac对应关系到自己的ip-mac缓存表。

## ARP攻击
ARP协议信任以太网所有的节点，只要它就收到的arp广播包，他就会把对应的ip-mac更新到自己的缓存表，根据以上说的arp协议缺陷，如果我们冒充网关主机C，不停的向以太网发送自己的ARP广播包，告知自己的ip-mac，此时其它主机就会被欺骗，更新我们C的ip-mac为网关主机的ip-mac，那么其它主机的数据包就会发送到C主机上，因为没有发给真正的网关，就会造成其它主机的网络中断。
