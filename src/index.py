#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '


__author__ = 'Steven Rain'


class Animal(object):
    count = 1

    def run(self):
        print('Animal is running!')


class Cat(Animal):
    def __init__(self):
        Animal.count = Animal.count + 1

    def run(self):
        print('Cat is running')


class Dog(Animal):
    def __init__(self):
        Animal.count = Animal.count + 1

    def run(self):
        print('Dog is running')


def run(animal):
    animal.run()


someKingOfAnimal = Animal()
dog = Dog()
cat = Cat()

dog.run()
cat.run()
someKingOfAnimal.run()

print
run(dog)
run(cat)
run(someKingOfAnimal)

print(cat.count)

