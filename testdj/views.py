from django.shortcuts import render


# Create your views here.
def template_test(request):
    lis = [1, 2, 3,4,5]
    dic = {"name": "黑蛋"}
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def dream(self):
            return " 我 is {} age {}岁...".format(self.name,self.age)
    gangdan = Person(name="钢蛋", age=18)
    goudan = Person(name="狗蛋", age=17)
    tiedan  = Person(name="铁蛋", age=16)
    person_list = [gangdan, goudan, tiedan]
    return render(request, "test.html", {"lis": lis, "dic": dic, "person_list": person_list})

