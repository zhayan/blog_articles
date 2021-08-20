## 使用numpy
尽量不要单独访问单个像素进行修改

## numpy 快的原因
1. 底层是C，部分是Fortran
2. 使用了BLAS，Basic Linear Algebra Subprograms，基础线性代数程序集
3. 采用向量化编程

## cv.add 与 numpy + 不同
OpenCV 加法是饱和运算，而 Numpy 加法是模运算

## cv.addWeighted 按权重混合图片

## 图像位运算产生覆盖效果
创建mask bitwise_not
mask覆盖 bitwise_and
原图与添加 bitwise_or

## 原则
尽可能避免在 Python 中使用循环，尤其是双/三循环等。它们本质上很慢。
尽可能对算法/代码进行矢量化，因为 Numpy 和 OpenCV 已针对矢量操作进行了优化。
利用缓存一致性。
除非必要，否则不要复制数组。尝试改用视图。数组复制是一项代价高昂的操作