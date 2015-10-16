#!/usr/bin/env python3
import random,os

class Question:
    def __init__(self,content,answers):
        self.content=content
        self.answers=answers
    def show(self):
        print('問：')
        print(self.content)
        random.shuffle(self.answers)
        rest=self.answers
        correct=0
        for i in range(0,len(self.answers)):
            curr,is_correct=rest.pop()
            if is_correct:
                correct=i+1
            print('%d. %s' %(i+1,curr))
        x=input()
        if x.strip() != str(correct):
            print('錯！正確答案是：%d' % correct)
            return False
        else:
            return True
    def __repr__(self):
        return '{Q:'+self.content+',\nA:'.join(
                                 [x for x,y in self.answers])+'}\n'

import pickle as serialise

def save(obj,fname='data.txt'):
    f=open(fname,'wb')
    serialise.dump(obj,f)
    f.close()

def load(fname='data.txt'):
    f=open(fname,'rb')
    b=serialise.load(f)
    f.close()
    return b

Q=Question
def O(s,b=False):
    return (s,b)

the_questions = [
  Q('John raises a lot of ___ including two ___.', [O('cattles; cows'),O('cows;cattle'),O('cattle; cows',True),O('cow;cattles')]),
  Q("What would you like to drink? We'd like two black ___. ", [O('coffee'),O('coffees',True),O('cup of coffees'),O('coffee cups')]),
  Q("The little girl asked her mother to buy her a nice pair of ___, so her mother went to some ___ stores.",[O('shoes; shoes'),O('shoes; shoe',True),O('shoe;shoes'),O('shoe;shoe')]),
  Q("We can go there on foot. It is only ___ walk.",[O('twenty minute'),O('twuenty minutes'),O('a twenty-minute',True),O('twenty minutes of')]),
  Q("Please pass us ___.",[O('two glasses of milks'),O('two glass of milks'),O('two glasses of milk',True),O('two glass of milk')]),
  Q("What __ we had yesterday!",[O('a wonderful time',True),O('wonderful times'),O('wonderful a time'),O('wonderful time')]),
  Q("We have only a sofa, a table and a bed in our new apartment. We need to buy many ___",[O('furniture'),O('furnitures'),O('pieces of furniture',True),O('equipments')]),
  Q("___ box cannot be lifted by a boy of five.",[O('So a heavy'),O('So heavy a',True),O('A such heavy'),O('Such heavy a')]),
  Q("Would you be ___ do it for me,please? Ofcourse, with pleasure.",[O('kind enough'),O('as kind to'),O('so kind as to',True),O('so kind to')]),
  Q("The food on the table looks ___ and smells ___, too.",[O('nice,good',True),O('well,nice'),O('good,nicely'),O('nicely,well')]),
  #Q("",[O(),O(),O(),O()]),
]

def do_ask(questions):
    random.shuffle(questions)
    return [i for i in questions if not i.show()]

def add_question(q):
    s=input('請輸入問題:\n')
    a=[O(input('Please input the right answer for the question.'),True),]
    while True:
        sa=input('Please input an wrong answer for the question, input %EXIT to end.')
        if sa.strip()=='%EXIT':
            break
        a.append(O(sa))
    return Q(s,a)
