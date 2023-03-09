#object oriented programming

# class----- blue print of program
# object ------real world entity
# reference------ store object(operations)


# eg:
#   class  ---vechicle               laptop
#  object-----car,bike,bus....       hp,acer.....


class Perscon:                  #  Person---cls name ---cls name should be in capital letter
    def read(self):             # function in clss called  method
        print("reading")
    def walk(self):
        print("walking")
p=Perscon()                    #  object creating
p.read()
p.walk()