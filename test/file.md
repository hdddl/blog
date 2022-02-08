---
title: 排序算法
date: 2021-12-19 19:10:00
tags:
- 算法学习
- 笔记
toc: true
categories:
- 算法
---

​		

这是我读《算法导论》(introduction to algorithms) 的排序部分做的一些笔记，排序算法是我正式开始学习算法的第一部分，作为一种基础算法其体现出来许多算法设计与分析的方法，同样也对我展现出了它具有的独特魅力。下面是我根据这是算法的实现方式不同给它们进行了一些分类，首先是根据算法实现是否需要比较分为了比较排序与非比较排序，对于比较排序它存在一个算法极限，并在笔记中进行分析。在比较排序中根据数据结构又可以分为简单排序与基于二叉树实现的排序，基于二叉树的排序的算法虽然复杂一些但是可以大大提升排序的时间复杂度，并且二叉树排序还体现出了算法设计中的常用的分而治之(Divide Conquer Combine)的思想。非比较排序非常巧妙的不需要比较就对一组数据进行了排序，非常有趣并且有启发意义。
<!-- more -->

![](https://dongliu-1301367244.cos.ap-shanghai.myqcloud.com/img/Sort algorithms.svg)

# 1、 比较排序

比较排序就是在排序过程中需要通过比较来确定元素的大小并根据元素的大小来排序，是我们常用的一种排序的方法。

## 1.1 简单排序

简单排序是日常生活中常用的排序方法，其逻辑比较简单，所依赖的数据结构就是顺序表，其平均算法复杂度为$\mathcal{O}(n^2)$。

### 1.1.1 冒泡排序(Bubble sort)

​		冒泡排序就是将索引置于最后一个位置，并将索引所对应的值与其前一个值进行比较，如果小于则交换这两个值，如果大于则比较，无论是大于还是小于都将索引向前移动一位，这个就像冒泡一样将较小值向首端移动所以被称为冒牌排序，这样就可以将最小的值移动到最首端。然后再次重复该操作就可以将第二小的值移动到首端的第二位，不断往复就可以完成数组的从小到大的排序了。

```c
/*
@function:
    实现冒泡排序
@para:
    SqList *L: 排序用的结构体，包含int型数组r与其长度length
@note:
    1. 冒泡排序就是将游标j从数组的底端像顶端移动，并将小的带上来，大的带下去
    2. 再加一个优化就是说没有数据交换了也就是已经排好了就退出，不要再继续进行下去了
*/
void bubble_sort(SqList *L){
    bool is_sorted = false;
    for(int i=0;i<L->length && !is_sorted;i++){
        is_sorted = true;
        for(int j=L->length-1;j>i;j--){
            if(L->r[j] < L->r[j-1]){
                // 交换两元素的位置
                swag(L,j,j-1);
                is_sorted = false;
            }    
        }
    }
}
```

### 1.1.2 选择排序(Select sort)

选择排序应该是排序算法中最简单的那个了，它就是遍历数组将最小的那个找出来将其与数组的第一个数组进行交换位置，然后再次遍历除第一个数组之外的其他数组元素找出第二小的放在数组第二位，如此循环直到数组元素按照从小到大的顺序完成排列。

```c
/*
@func:
    实现数组的选择排序
@para:
    SqList *L: 排序用的结构体，包含int型数组r与其长度length
@note:
    1. 选择排序就是将一个数组中最小的元素找出来放在最前面

*/
void select_sort(SqList *L){
    int min;
    for(int i=0; i<L->length; i++){
        // 默认将第一个数字设置为最小值
        min = i;
        for(int j=i+1;j<L->length;j++){
            if(L->r[j]<L->r[min])
                min = j;
        }
        swag(L,i,min); 
    }
}
```

### 1.1.3 插入排序(Insert sort)

插入排序就像我们打牌的时候整理牌一样，把第二个元素与第一个元素进行比较如果小于就插入到第一个元素前面（即交换两元素的位置），如果大于就不变，然后再将第三个元素插入的前面合适的位置，依此循环直到数组完成从小到大的排列。

```c
/*
@func:
    实现插入排序
@para:
    SqList *L: 排序用的结构体，包含int型数组r与其长度length
*/
void insert_sort(SqList *L){
    for(int i=0; i<L->length-1; i++){
        for(int j = i+1;j>0;j--){
            if(L->r[j] < L->r[j-1]){
                swag(L,j,j-1);
            }
        }
    }
}
```

### 1.1.4 希尔排序(Shell sort)

希尔排序是一插入排序的优化版，当插入排序中较小的元素在靠右的那边时，需要很多次比较才能将数组排列好。希尔排序就是按照一定的间隔(interval)将数组划分为几个子数组，对子数组进行插入排序，排序好之后再对组合成的完整数组进行选择排序，对于较大的数组也可以进行多次不同间隔的分割。

```c
/*
@func:
    实现希尔排序算法
@para:
    SqList *L: 排序用的结构体，包含int型数组r与其长度length
@note:
    1. 希尔排序是一种基于选择排序的排序算法，在选择排序中如果最小值在数组的最右边就会产出非常多的比较次数，
    希尔排序就把一个数组按照一个interval将数组分为几个sub-list，对每个子数组进行选择排序然后再把他们合并。
    2. 希尔排序使用分治策略(Divide Conquer Conbine)
    3. shell sort有使用increment型的也有使用interval型的，increment就是取出连续的increment构成子序列，而interval
    是每隔interval构成一组
*/
void shell_sort(SqList *L){
    // 这里interval是一个经验值，目前没有固定的算法
    // interval为几就是分为几份
    // 如果右式有小数点的话直接舍去
    int interval = L->length/3 + 1;
    for(int i=0;i < interval; i++){
        for(int j=0;j < L->length; j += interval){
            for(int k=j+interval; k > 0; k -= interval){
                if(L->r[k] < L->r[k-interval]){
                    swag(L, k, k-interval);
                }
            }
        }
    }
    // 在完成分组排序后直接调用插入排序
    insert_sort(L);
}
```

## 1.2 基于二叉树的排序

下面几种算法是基于二叉树的排序方法，核心思想就是分而治之，一般采用递归求解，因为递归一般使用树这这数据结构表示，树中的二叉树结构最为简单且可以非常方便的通过一维数组进行储存，所以他们一般基于二叉树进行求解。

### 1.2.1 堆排序(Heap sort)

​	堆排序是基于堆这种数据结构的一种排序方法，事实上堆这种数据结构是在堆排序这种算法提出的时候一齐提出来的，堆实际上是一种特殊的完全二叉树[^1]，堆包含最大堆与最小堆，最大堆要求父节点要比两个子节点都要大，所以堆的根节点应该是堆中所以元素的最大值，最小堆则刚好与之相反。下面以最大堆为例介绍堆排序的大致过程，堆排序的大致思想就是先形成一个最大堆，然后将最大堆的根节点拿走，再使得剩下的元素形成一个最大堆，再将其根节点拿走，依此循环直到只剩下最后一个元素。因为每次重新形成的最大堆的根节点都是是剩余元素中的最大值，所以依此将其排列即可完成数组的排序。所以根排序的核心就是如何将一组元素形成最大堆，这是相关的代码。

```python
/*
@func:
    维护一个最大堆
@note:
    1. 程序设计就是要减少嵌套
*/
void max_heapify(heap *L, int i){
    int l,r,maxium=i;
    // left chrild and right chrild
    l = 2*i;
    r = 2*i + 1;
    if(l < L->heap_size && L->r[l] > L->r[i]){
        maxium = l;
    }else{
        maxium = i;
    }
    if(r < L->heap_size && L->r[r] > L->r[maxium]){
        maxium = r;
    }
    if(maxium != i){
        swag(L->r,i,maxium);
        // 递归调用
        max_heapify(L,maxium);
    }
}
```

​	还有一个值得提一下的是最大堆的建立，这个它的代码

```python
void build_max_heap(heap *L){
    // 因为要保证根节点为最大值，所以这里采用自底向上构建
    for(int i=L->length/2;i>=1;i--){
        max_heapify(L,i);
    }
}
```

可以看到，最大堆的建立是采用自底向上进行建立的，并且是从$\lfloor{\frac{length}{2}}\rfloor$开始的，因为在往下面走就都是叶子节点了我们上面的`max_heapify`只需要堆非叶子节点进行维护就可以了。下面我们证明一下为什么再往下面走就是叶子节点了，对于节点$\lfloor{\frac{length}{2}}\rfloor$其左孩子节点为
$$
\begin{aligned}
\text{LEFT}(\lfloor n / 2 \rfloor + 1)
    & = 2(\lfloor n / 2 \rfloor + 1) \\\\
    & > 2(n / 2 - 1) + 2 \\\\
    & = n - 2 + 2 \\\\
    & = n.
\end{aligned}
$$
因为它的左孩子节点应该大于数组元素数量$n$所以它就是一个叶子节点，对于它后面的肯定也为叶子节点。

​	再实现堆排序的时候需要包含以下几个元素，一个是包含所有元素的数组，一个是数组长度还有一个是堆的大小，因为我们在抽离堆的根节点的时候要将堆的大小减一，但是堆的长度不变，下面是堆排序的主程序代码。

```python
/*
@func:
    实现堆排序
@para:
    SqList *L: 排序用的结构体，包含int型数组r与其长度length还是堆的大小heap_size
@note:

*/
void heap_sort(heap *L){
    // 首先建立一个最大堆
    build_max_heap(L);
    for(int i=L->length;i>1;i--){
        swag(L->r,1,i);
        L->heap_size -= 1;
        max_heapify(L,1);
    }
}
```

### 1.2.2 并归排序(Merge sort)

Merge sort是分而治之策略的典型体现，它首先将一个数组不断细分为不同的子数组，直到最终的子数组的长度为1，然后再将这些子数组按照顺序合并再一起就形成了一个排好序的数组了。首先来看合并部分

>将两个已经排好序的数组合并成一个数组，
>
>例如将`nums1=[2,4,5,6]`，`nums2=[1,2,3,6]`，合并成`ans=[1,2,3,5,6]`

通过C++编程的代码如下

```c++
vector<int>merge(vector<int>&nums1, vector<int>&nums2){
    vector<int>ans;
    // 将inf作为哨兵(sentinel)
    int inf = 1e6;
    nums1.push_back(inf);
    nums2.push_back(inf);
    unsigned int i=0;
    unsigned int j=0;
    while(ans.size() < nums1.size() + nums2.size() -2){
        if(nums1[i] <= nums2[j]){
            ans.push_back(nums1[i]);
            i++;
        }else{
            ans.push_back(nums2[j]);
            j++;
        }
    }
    return ans;
}
```









## 1.3 选择排序算法复杂度分析



# 2、非比较排序

## 2.1 计数排序

## 2.2 基数排序

## 2.3 桶排序



# 3、取值



[^1]: [完全二叉树 - 维基百科，自由的百科全书 (wikipedia.org)](https://zh.wikipedia.org/wiki/二叉树#完全二叉树)
