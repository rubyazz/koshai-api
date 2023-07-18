"""
Test of sorting algorithms
"""


import copy



import random
import sys
import time
import traceback


class SortTest:
    N = 100    # Number of data
    M = 10000  # Maximum value ( < M )
    L = 10000  # Count of sort trying

    def __init__(self):
        self.base = [random.randrange(self.N) + 1 for _ in range(self.N)]
        print("#### Base list")
        self.__display_list(self.base)

    def exec(self):
        """ Execution of test """
        try:
            self.__sort_bubble()
            self.__sort_selection()
            self.__sort_insertion()
            self.__sort_quick()
            self.__sort_heap_up()
            self.__sort_heap_down()
            self.__sort_shell()
        except Exception as e:
            raise

    def __sort_bubble(self):
        """ Basic exchange method (Bubble sort) """
        print("1  : Bubble Sort      ", end="")
        try:
            t1 = time.time()
            for l in range(self.L):
                self.a = copy.deepcopy(self.base)
                for i in range(self.N - 1):
                    for j in reversed(range(i + 1, self.N)):
                        if self.a[j] < self.a[j - 1]:
                            self.a[j - 1], self.a[j] \
                                    = self.a[j], self.a[j - 1]
            t2 = time.time()
            self.__display(self.a, t2 - t1)
        except Exception as e:
            raise

    def __sort_selection(self):
        """ Basic exchange method (Selection sort) """
        print("2  : Selection Sort   ", end="")
        try:
            t1 = time.time()
            for l in range(self.L):
                self.a = copy.deepcopy(self.base)
                for i in range(self.N - 1):
                    min, s = self.a[i], i
                    for j in range(i + 1, self.N):
                        if self.a[j] < min:
                            min, s = self.a[j], j
                    self.a[i], self.a[s] = self.a[s], self.a[i]
            t2 = time.time()
            self.__display(self.a, t2 - t1)
        except Exception as e:
            raise

    def __sort_insertion(self):
        """ Insertion sort """
        print("3  : Insertion Sort   ", end="")
        try:
            t1 = time.time()
            for l in range(self.L):
                self.a = copy.deepcopy(self.base)
                for i in range(1, self.N):
                    for j in reversed(range(i)):
                        if self.a[j] > self.a[j + 1]:
                            self.a[j], self.a[j + 1] \
                                = self.a[j + 1], self.a[j]
                        else:
                            break
            t2 = time.time()
            self.__display(self.a, t2 - t1)
        except Exception as e:
            raise

    def __sort_quick(self):
        """ Improved exchange method (Quick sort) """
        print("4  : Quick Sort       ", end="")
        try:
            t1 = time.time()
            for l in range(self.L):
                self.a = copy.deepcopy(self.base)
                self.__quick(0, self.N - 1)
            t2 = time.time()
            self.__display(self.a, t2 - t1)
        except Exception as e:
            raise

    def __sort_heap_up(self):
        """ Improved exchange method (Heap sort with upward method) """
        print("5-1: Heap Sort(Up)    ", end="")
        try:
            t1 = time.time()
            self.h = [0 for _ in range(self.N + 1)]
            for l in range(self.L):
                self.__generate_heap_up()
                n, m = self.N, self.N
                while n > 1:
                    self.h[1], self.h[n] = self.h[n], self.h[1]
                    n -= 1
                    p = 1
                    s = 2 * p
                    while s <= n:
                        if s < n and self.h[s + 1] > self.h[s]:
                            s += 1
                        if self.h[p] >= self.h[s]:
                            break
                        self.h[p], self.h[s] = self.h[s], self.h[p]
                        p = s
                        s = 2 * p
            del(self.h[0])
            t2 = time.time()
            self.__display(self.h, t2 - t1)
        except Exception as e:
            raise

    def __sort_heap_down(self):
        """ Improved exchange method (Heap sort with downward method) """
        print("5-2: Heap Sort(Down)  ", end="")
        try:
            t1 = time.time()
            self.h = [0 for _ in range(self.N + 1)]
            for l in range(self.L):
                for i in range(1, self.N + 1):
                    self.h[i] = self.base[i - 1]
                self.__generate_heap_down()
                n, m = self.N, self.N
                while n > 1:
                    self.h[1], self.h[n] = self.h[n], self.h[1]
                    n -= 1
                    p = 1
                    s = 2 * p
                    while s <= n:
                        if s < n and self.h[s + 1] > self.h[s]:
                            s += 1
                        if self.h[p] >= self.h[s]:
                            break
                        self.h[p], self.h[s] = self.h[s], self.h[p]
                        p = s
                        s = 2 * p
            del(self.h[0])
            t2 = time.time()
            self.__display(self.h, t2 - t1)
        except Exception as e:
            raise

    def __sort_shell(self):
        """ Improved insertion method (Shell sort) """
        print("6  : Shell Sort       ", end="")
        try:
            t1 = time.time()
            for l in range(self.L):
              self.a = copy.deepcopy(self.base)
              gap = self.N // 2
              while gap > 0:
                  for k in range(gap):
                      i = k + gap
                      while i < self.N:
                          j = i - gap
                          while j >= k:
                              if self.a[j] > self.a[j + gap]:
                                  self.a[j], self.a[j + gap] \
                                      = self.a[j + gap], self.a[j]
                              else:
                                  break
                              j -= gap
                          i += gap
                  gap = gap // 2
            t2 = time.time()
            self.__display(self.a, t2 - t1)
        except Exception as e:
            raise

    def __quick(self, left, right):
        """ Recursive function for quick sort
        :param int  left:  index of left-side list
        :param int right: index of right-side list
        """
        try:
            if left >= right:
                return
            s, i, j = self.a[left], left, right + 1
            while True:
                i += 1
                while i < self.N and self.a[i] < s:
                    i += 1
                j -= 1
                while j < self.N and self.a[j] > s:
                    j -= 1
                if i >= j:
                    break
                self.a[i], self.a[j] = self.a[j], self.a[i]
            self.a[left], self.a[j] = self.a[j], s
            self.__quick(left, j - 1)
            self.__quick(j + 1, right)
        except Exception as e:
            raise

    def __generate_heap_up(self):
        """ Function for heap(upward) generation """
        try:
            for i in range(1, self.N + 1):
                self.h[i] = self.base[i - 1]
                s = i
                p = s // 2
                while s >= 2 and self.h[p] < self.h[s]:
                    self.h[p], self.h[s] = self.h[s], self.h[p]
                    s = p
                    p = s // 2
        except Exception as e:
            raise

    def __generate_heap_down(self):
        """ Function for heap(downward) generation """
        try:
            n = self.N
            for i in reversed(range(1, n // 2 + 1)):
                p = i
                s = 2 * p
                while s <= n:
                    if s < n and self.h[s + 1] > self.h[s]:
                        s += 1
                    if self.h[p] >= self.h[s]:
                        break
                    self.h[p], self.h[s] = self.h[s], self.h[p]
                    p = s
                    s = 2 * p
        except Exception as e:
            raise

    def __display_list(self, l):
        """ Display of list
        :param list l: target list for display
        """
        try:
            for i in range(self.N):
                print("{:5d} ".format(l[i]), end="")
                if (i + 1)  % 10 == 0 or i == self.N - 1:
                    print()
            print()
        except Exception as e:
            raise

    def __display(self, l, tt):
        """ Display of result
        :param list   l: target list for display
        :param float tt: elapsed time
        """
        try:
            # ソート結果を確認したければ、以下2行をコメント解除
            #print("\n#### Sorted list")
            #self.__display_list(l)
            print("Time: {:6.2f} sec.".format(tt))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = SortTest()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
