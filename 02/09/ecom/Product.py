#ID, name , description , category , tags , stock , price

class Product :
    def __init__(self, ID, name , description , category , tags , stock , price):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price 
    def __str__(self):
        return f'[id= {self.id}, name = {self.name} , description = {self.description} , category = {self.category} , tags = {self.tags} , stock = {self.stock} , price ={self.tags}]'
    def __repr__(self):
        return self.__str__()
    
mobile_vivo = Product(1001,'vivo Y21','good camera quality. bad call quailty.' , 'mobile' , 'mobile,electronics , smart phone, android phone',10,21000)
print(mobile_vivo)

mobile_samsung = Product(1002,'Sammsung','good camera quality. bad performance after 1 year.' , 'mobile' , 'mobile,electronics , smart phone, android phone',10,121000)
print(mobile_samsung)

mobile_iphone = Product(1003,'iphone','good camera quality. bad performance in battery.' , 'mobile' , 'mobile,electronics , I-phone, IOS phone',10,150000)
print(mobile_iphone)

