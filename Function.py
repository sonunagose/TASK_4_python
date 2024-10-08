# EXAMPLE_1
 
def productinfo(Name,brand,price,MgdDate,Expirydate,type):
    print(f'product_Name={Name}')
    print(f'product_Brand={brand}')
    print(f'product_price={price}')
    print(f'product_MgdDate = {MgdDate}')
    print(f'product_Expirydate={Expirydate}')
    print(f'product_type={type}')

    return{
        'product-name':Name,
        'product-Brand':brand,
        'product-price':price,
        'product-mgdDate': MgdDate,
        'product-Expirydate':Expirydate,
        'product-type':type,
    }
print('---')
product1=productinfo('Soap','Santoor',30,'01-01-2024','02-03-2025','Daily')
print('---')
product2=productinfo('Biscuit','ParleG',20,'01-01-2024','04-05-2025','Daily')
print('---')

# EXAMPLE_2

def StudentData(Name,Id,age,Class,subject,marks,mob):
    print(f's_Name={Name}')
    print(f's_Id={Id}')
    print(f's_age={age}')
    print(f's_class={Class}')
    print(f's_subject={subject}')
    print(f's_marks={marks}')
    print(f's_mob = {mob}')
    return'---studentData'

print('----')
print(f'studentData_1{('Ram',1,25,11,'Science',50,'12345')}')
print('---')
print(f'studentData_2{('Shyam',2,30,12,'Maths',60,'76543')}')
print('----')
