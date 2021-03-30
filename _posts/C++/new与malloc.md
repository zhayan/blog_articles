---
title: 【C++】new与malloc
date: 2020-12-22 21:08:07
toc: true
tags:
- C++
categories:
- C++
---
new和malloc的内存分配在堆上。也有说new是分配在自由存储区而malloc分配在堆上，自由存储区可以是堆也可以不是，具体要看new内部的实现。
操作系统在堆上维护一个空闲内存链表，当需要分配内存的时候，就查找这个表，找到一块内存大于所需内存的区域，分配内存并将剩余的内存空间返还到空闲链表上（如果有剩余的话）。

<!-- more -->

## new/delete和malloc/free的区别
1. malloc和free是库函数，而new和delete是C++操作符；
2. new自己计算需要的空间大小，比如`int * a = new，malloc`需要指定大小，例如`int * a = malloc(sizeof(int))`；
3. new在动态分配内存的时候可以初始化对象，调用其构造函数，delete在释放内存时调用对象的析构函数。而malloc只分配一段给定大小的内存，并返回该内存首地址指针，如果失败，返回NULL。
4. new是C++操作符，是关键字，而operate new是C++库函数
5. opeartor new /operator delete可以重载，而malloc不行
6. new可以调用malloc来实现，但是malloc不能调用new来实现
7. 对于数据C++定义new[] 专门进行动态数组分配，用delete [] 进行销毁。new[] 会一次分配内存，数量一般存储在返回地址前的四个字节，然后多次调用构造函数；delete[]会先多次调用析构函数，然后一次性释放。

分配数组不同之处
```C++
int char* pa = new char[100];
int char* pb = malloc(sizeof(char) * 100);

```
8. malloc能够直观地重新分配内存
9. 
使用malloc分配的内存后，如果在使用过程中发现内存不足，可以使用realloc函数进行内存重新分配实现内存的扩充。realloc先判断当前的指针所指内存是否有足够的连续空间，如果有，原地扩大可分配的内存地址，并且返回原来的地址指针；如果空间不够，先按照新指定的大小分配空间，将原有数据从头到尾拷贝到新分配的内存区域，而后释放原来的内存区域。

new没有这样直观的配套设施来扩充内存。