#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author:
@file: obj1.py
@time: 2021/1/21 14:47
@desc:
"""
from abc import ABCMeta, abstractmethod


class IAnimal(metaclass=ABCMeta):
    @abstractmethod
    def drink(self, *args):
        pass

    @abstractmethod
    def reproduction(self, *args):
        pass


class Bird(IAnimal):
    def __init__(self, name, age, home):
        self.name = name
        self.age = age
        self.home = home

    def ate(self, someFood):
        print(f'{self.name} 正在吃 {someFood}.')

    def drink(self, water):
        print(f'{self.name} 正在喝水 和 {water}.')

    def reproduction(self, withWho):
        print(f'{self.name} 与 {withWho} 剩下了baby.')


class FlyableMixin(IAnimal):
    def fly(self):
        print('Flying...')


class RunableMixIN(IAnimal):
    def run(self):
        print('Running...')


class Xique(Bird, FlyableMixin):  # 不必要时，不要用多重继承！直接将需要的类实例化，放到其他类里，这就叫组合！
    def __init__(self):
        super(Bird, self).__init__()  # 这里为什么一定要指定 Bird？否则就会出错

    @property
    def tizhong(self):
        return '15kg'


class A(object):
    def test(self):
        print(' A test')


class B(A):
    def test(self):
        super().test()
        print(' B test')


class C(A):
    def test(self):
        super().test()
        print(' C test')


class D(B, C):
    def test(self):
        super().test()
        print(' D test')


if __name__ == '__main__':
    xq = Xique()
    xq.name = 'xiao xi'
    xq.age = 3.2
    xq.home = 'beijing'
    xq.fly()
    xq.drink('农夫山泉')
    print(Xique.mro())


    # 查看继承的执行顺序
    # d = D()
    # d.test()
    # print(D.mro())

