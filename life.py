from random import randint
class Person:
  #this is an instance of fa person that has a name, salary , rent and other things in life.
  def __init__(self,name,salary,rent,food,luxuary,supplies,misc):
    self.name = name
    self.salary = salary
    self.rent = rent
    self.food = food
    self.luxuary = luxuary
    self.supplies = supplies
    self.misc = misc
    self.followers = 1
    self.life = 100
  #this prints out all the statistics of a person
def stats(self):
  print "******************************************"
  print "Name: " + self.name + "\n"
  print "Salary: " + str(self.salary) +"\n"
  print "Rent: " + str(self.rent) +"\n"
  print "Food: "+ str(self.food) + "\n"
  print "Luxuary: " + str(self.luxuary) + "\n"
  print "Supplies: " + str(self.supplies)+ "\n"
  print "Miscellaneous: " + str(self.misc) 
  print "******************************************"
  #picks a random number from 1 to any number
def random(num):
  return randint(1,num)
#makes people with different salary , rent and other things you buy.
entertainer = Person("ACTOR",1000000,10000,5000,10000,500,1000)
programmer = Person("Programmer",randint(50000,90000),5000,500,random(300),random(1000),random(100))
academic = Person("Teacher",randint(18000,24000),0,100,0,random(200),random(100))
#gives the player a promotion
def promotion(it):
  reducedsal = it.salary/100
  more(it,randint(reducedsal/2,reducedsal)*100)
  return married(it)
#person gets married
def married(it):
  if random(2)==2:
    less(it,randint(0,it.salary/2))
    more(it,it.salary)
    return repair(it)
  else:
    return repair(it)
#person has to repair something
def repair(it):
  if random(2)==2:
    less(it,1000)
    return robbed(it)
  else:
    return robbed(it)
#person gets robbed
def robbed(it):
  if random(10)==10:  
    more(it,it.salary/2)
    return baby(it)
  else:
    return baby(it)
#person has a baby
def baby(it):
  if random(3)==3:
    less(it,randint(it.luxuary/2,it.luxuary))
    return writebook(it)
  else:
    return writebook(it)
#person writes a famous book
def writebook(it):
  if random(5)==5:
    more(it,50000)
    it.followers += 100000
    return it
  return it
#adds to salary
def more(it,num):
  it.salary += num
#subtracts from salary
def less(it,num):
  it.salary -= num
#runs all players through sequence
promotion(entertainer)
stats(entertainer)
