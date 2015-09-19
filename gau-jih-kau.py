#!/usr/bin/env python3
import random

class Question:
    def __init__(self,content,answers):
        self.content=content
        self.answers=answers
        random.shuffle(self.answers)
    def show(self):
        print('問：')
        print(self.content)
        rest=self.answers
        correct=0
        for i in range(0,len(self.answers)):
            curr=rest.pop()
            if curr.is_correct:
                correct=i+1
            print('%d. %s' %(i+1,curr))
        x=input()
        if x.strip() != str(correct):
            print('錯！正確答案是：%d' % correct)

class Option:
    def __init__(self,a,b=False):
        self.a=a
        self.is_correct=b
    def __str__(self):
        return self.a

Q=Question
O=Option

the_questions = [
  Q('John raises a lot of ___ including two ___.', [O('cattles; cows'),O('cows;cattle'),O('cattle; cows',True),O('cow;cattles')]),
  Q("What would you like to drink? We'd like two black ___. ", [O('coffee'),O('coffees',True),O('cup of coffees'),O('coffee cups')]),
  Q("The little girl asked her mother to buy her a nice pair of ___, so her mother went to some ___ stores.",[O('shoes; shoes'),O('shoes; shoe',True),O('shoe;shoes'),O('shoe;shoe')]),
  Q("We can go there on foot. It is only ___ walk.",[O('twenty minute'),O('twuenty minutes'),O('a twenty-minute',True),O('twenty minutes of')]),
  Q("Please pass us ___.",[O('two glasses of milks'),O('two glass of milks'),O('two glasses of milk',True),O('two glass of milk')]),
  Q("What __ we had yesterday!",[O('a wonderful time',True),O('wonderful times'),O('wonderful a time'),O('wonderful time')]),
  Q("We have only a sofa, a table and a bed in our new apartment. We need to buy many ___",[O('furniture'),O('furnitures'),O('pieces of furniture',True),O('equipments')]),
  #Q("",[O(),O(),O(),O()]),
]

random.shuffle(the_questions)
for i in the_questions:
    i.show()
