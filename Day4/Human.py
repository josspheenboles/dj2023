class Employee:
    def __init__(self,name,salar):
        self.name=name
        self.__salary=salar
    def speek(self):
        print(self.__salary)
    def getsalary(self):
        return self.__salary
    def setsalary(self,newsalary):
        if(newsalary>3000):
            self.__salary=newsalary
        else:
            print('salary must > 3000')
    def __str__(self):
        return 'my name '+self.name+' my salary ='+str(self.__salary)

'''
class Human:
    def __init__(self,nationalnum,name):
        self.nationalnum=nationalnum
        self.name=name
    def speek(self):
        print('my name is ',self.name)
    def __str__(self):
        return 'my name is '+self.name
    def __len__(self):
        return 0
class Employee():
    #child constr
    def __init__(self,nationalnum,name,salary):
        #super(Employee, self).__init__(nationalnum,name)
        self.__salary=salary
    #instance method
    #overide speek in parent class
    def speek(self):
        print('my name is ',self.name,'my salary=',self.__salary)
    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self,newsalary):
        if(newsalary>3000):
            self.__salary=newsalary
        else:
            print('salary musyt > 2000')
    """
    def getsalary(self):
        return self.__salary
    def setsalary(self,newsalary):
        if(newsalary>=self.__salary or newsalary>3000):
            self.__salary=newsalary
        else:
            print('review new salary')
    """
class Engineer(Employee):
    pass

class Mamel():
    def __init__(self):
        print('amamel constr')
    def speek(self):
        print('iam amamel')
class Employee:
    def __init__(self,nationalnum,name,salary):
        self.nationalnum=nationalnum
        self.name=name
        self.salary=salary
class Enginerring:
    def __init__(self,nationalnum,name,salary,location):
        self.nationalnum=nationalnum
        self.name=name
        self.salary=salary
        self.location=location


#defination class of human
class Human:
    #class variable
    counter=0
    Faluts=0
    #constructor
    def __init__(self,id,name):
        #instance variable
        self.id=id
        self.name=name
        self.track='django'
        Human.counter+=1
        print('iam constructor')

    #instance method
    def speak(self):
        print('iam ',self.name)
        print('object counter',Human.counter)
    #class method
    @classmethod
    def makefault(cls):#cls is Human datatype
        #Human.Faluts+=1
        cls.Faluts+=1
    @staticmethod
    def mesuretemp(temp):
        if(temp>37):
            print('too hot')
        elif(temp<37):
            print('too cold')
        else:
            print('normal')
'''