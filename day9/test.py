class Car:
    brand = '奔驰'
    name = 'Car'    #* 类定义

    def __init__(self):
        # 可以通过实例访问到类属性
        print(self.brand)

        # 定义实例属性和类属性重名
        self.name = 'benz car' #* 实例定义

    def name(self):
        print(f'通过方法名访问：{self.name}')

c1 = Car()

print(f'通过实例名访问name：{c1.name}')
print(f'通过类名  访问name：{Car.name}')
# Car.name(c1) #! 错误 ∵py会先找这个类是否有此属性 存在的话便会隐藏具有相同名字的方法名
Car.name(c1) #* ∵通过实例访问方法时 实例对象作为自我参数传递给 self参数 ∴当想从类中调用一个方法 就可以明确传递一个实例作为参数 这样py就知道你在调用方法