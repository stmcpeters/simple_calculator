# -*- coding: utf-8 -*-
from functools import reduce
import operator

class SimpleCalculator:
    def add(self, *args):
      return sum(args)

    def sub(self, *args):
      # def sub2(a, b):
      #   return a - b
      
      return reduce(operator.sub, args)

    def mul(self, *args):
      # def mul2(a, b):
      #   return a * b

      return reduce(operator.mul, args)

    def div(self, a, b):
      return a / b