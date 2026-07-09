import pickle
def addfood():
     print('''
------------------------
  NEW FOOD INTRODUCING
------------------------
''')
     with open('food.dat','ab') as file:
          while 1:
               name=input('Enter food name:')
               price=int(input('Enter price of the food in Rs:'))
               lst=[name,price]
               pickle.dump(lst,file)
               print('')
               ch=input('Do you want to add more (YES/NO):')
               if ch.lower()=='yes':
                    continue
               elif ch.lower()=='no':
                    print('\nSuccessfully added')
                    break
               else:
                    print('\nInvalid selection add one more food')
addfood()

               
