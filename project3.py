import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root"
)

dbcursor = db.cursor()

try:
    dbcursor.execute("CREATE DATABASE dept_store")
except:
    dbcursor.execute("DROP DATABASE dept_store")
    dbcursor.execute("CREATE DATABASE dept_store")

dbcursor.execute("USE dept_store")

dbcursor.execute("CREATE TABLE department (dept_id varchar(4), name varchar(20), location varchar(15), primary key (dept_id))")
dbcursor.execute("CREATE TABLE employee (employee_id int, first_name varchar(30), last_name varchar(30), ssn varchar(11), start_date varchar(10), dept_id varchar(4), manager_id int, primary key (employee_id), foreign key (manager_id) references employee (employee_id) on delete cascade)")
dbcursor.execute("CREATE TABLE sale (transaction_id int, amount numeric(6,2), date varchar(10), time varchar(6), employee_id int, primary key(transaction_id), foreign key (employee_id) references employee (employee_id) on delete cascade)")
dbcursor.execute("CREATE TABLE wages (employee_id int, paycheck_no int, wage_reg numeric(6,2), wage_overtime numeric(6,2), hours_tot numeric(6,2), primary key (employee_id, paycheck_no), foreign key (employee_id) references employee (employee_id) on delete cascade)")
dbcursor.execute("CREATE TABLE customer (customer_id int, transaction_id int, primary key (customer_id), foreign key (transaction_id) references sale (transaction_id) on delete cascade)")
dbcursor.execute("CREATE TABLE inventory (product_id int, name varchar(40), color varchar(10), size varchar(3), quantity int, price numeric(6,2), primary key (product_id))")
dbcursor.execute("CREATE TABLE items_sold (transaction_id int, product_id int, primary key (transaction_id, product_id), foreign key (transaction_id) references sale (transaction_id) on delete cascade, foreign key (product_id) references inventory (product_id) on delete cascade)")
dbcursor.execute("CREATE TABLE pay_method (transaction_id int, pay_method varchar(20), primary key (transaction_id, pay_method), foreign key (transaction_id) references sale (transaction_id) on delete cascade)")

add_employee1 = ("INSERT INTO employee (employee_id, first_name, last_name, ssn, start_date, dept_id) VALUES (%s,%s,%s,%s,%s,%s)")
add_employee2 = ("INSERT INTO employee (employee_id, first_name, last_name, ssn, start_date, dept_id, manager_id) VALUES (%s,%s,%s,%s,%s,%s,%s)")
add_dept = ("INSERT INTO department (dept_id, name, location) VALUES (%s,%s,%s)")
add_sale = ("INSERT INTO sale (transaction_id, amount, date, time, employee_id) VALUES (%s,%s,%s,%s,%s)")
add_wage = ("INSERT INTO wages (employee_id, paycheck_no, wage_reg, wage_overtime, hours_tot) VALUES (%s,%s,%s,%s,%s)")
add_customer = ("INSERT INTO customer (customer_id, transaction_id) VALUES (%s,%s)")
add_inventory = ("INSERT INTO inventory (product_id, name, color, size, quantity, price) VALUES (%s,%s,%s,%s,%s,%s)")
add_sold = ("INSERT INTO items_sold (transaction_id, product_id) VALUES (%s,%s)")
add_pay = ("INSERT INTO pay_method (transaction_id, pay_method) VALUES (%s,%s)")

dept1 = ('WMNS','Women\'s','1st Floor')
dept2 = ('MENS','Men\'s','1st Floor')
dept3 = ('CHLD','Children\'s','2nd Floor')
dept4 = ('HOME','Home Goods','Basement')
dept5 = ('BATH','Bath','Basement')
dept6 = ('TOYS','Toys','2nd Floor')
dept7 = ('PFUM','Perfum','1st Floor')
dept8 = ('KTCN','Kitchen','Basement')
dept9 = ('TEEN','Teen\'s','2nd Floor')
dept10 = ('JWRY','Jewelry & Watches','1st Floor')

dbcursor.execute(add_dept,dept1)
dbcursor.execute(add_dept,dept2)
dbcursor.execute(add_dept,dept3)
dbcursor.execute(add_dept,dept4)
dbcursor.execute(add_dept,dept5)
dbcursor.execute(add_dept,dept6)
dbcursor.execute(add_dept,dept7)
dbcursor.execute(add_dept,dept8)
dbcursor.execute(add_dept,dept9)
dbcursor.execute(add_dept,dept10)

add_emp1 = (100012,'Linda','Davis','379-13-9504','03/22/2013','WMNS')
add_emp2 = (100046,'Edie','Carmona','531-17-1943','12/24/2014','PFUM')
add_emp3 = (100053,'Audrey','Scott','238-85-5367','06/26/2012','CHLD')
add_emp4 = (100076,'James','Gonzales','420-60-5264','03/27/2014','MENS')
add_emp5 = (100089,'Veronica','Wright','499-94-6087','03/27/2014','TEEN')
add_emp6 = (100035,'Deborah','Stein','483-32-3901','11/11/2011','JWRY')
add_emp7 = (100027,'Jessica','Tanner','361-04-7061','06/01/2013','HOME')
add_emp8 = (100081,'Lincoln','Hill','150-52-6696','09/02/2013','KTCN')
add_emp9 = (100068,'David','Jackson','037-30-7263','01/15/2013','TOYS')
add_emp10 = (100094,'Clarence','Renich','509-14-3743','08/03/2013','BATH')
add_emp11 = (100037,'Anna','Byrd','145-80-6698','12/12/2013','WMNS',100012)
add_emp12 = (100026,'Ruth','Spears','656-05-0333','03/24/2014','PFUM',100046)
add_emp13 = (100098,'Lisa','Barth','263-99-5244','08/09/2014','CHLD',100053)
add_emp14 = (100042,'Don','Rowland','103-32-7170','06/19/2014','MENS',100076)
add_emp15 = (100051,'Melinda','Beniavides','301-58-2705','03/18/2014','TEEN',100089)
add_emp16 = (100074,'Bethany','Ackermann','459-22-9198','04/05/2012','JWRY',100035)
add_emp17 = (100063,'Jerry','Gooding','039-26-3931','08/25/2014','HOME',100027)
add_emp18 = (100019,'Leona','Rodgers','601-70-9255','04/22/2014','KTCN',100081)
add_emp19 = (100085,'Barton','Moran','626-66-4858','12/27/2014','TOYS',100068)
add_emp20 = (100023,'Thelma','Gordon','158-14-9164','07/03/2014','BATH',100094)

dbcursor.execute(add_employee1,add_emp1)
dbcursor.execute(add_employee1,add_emp2)
dbcursor.execute(add_employee1,add_emp3)
dbcursor.execute(add_employee1,add_emp4)
dbcursor.execute(add_employee1,add_emp5)
dbcursor.execute(add_employee1,add_emp6)
dbcursor.execute(add_employee1,add_emp7)
dbcursor.execute(add_employee1,add_emp8)
dbcursor.execute(add_employee1,add_emp9)
dbcursor.execute(add_employee1,add_emp10)
dbcursor.execute(add_employee2,add_emp11)
dbcursor.execute(add_employee2,add_emp12)
dbcursor.execute(add_employee2,add_emp13)
dbcursor.execute(add_employee2,add_emp14)
dbcursor.execute(add_employee2,add_emp15)
dbcursor.execute(add_employee2,add_emp16)
dbcursor.execute(add_employee2,add_emp17)
dbcursor.execute(add_employee2,add_emp18)
dbcursor.execute(add_employee2,add_emp19)
dbcursor.execute(add_employee2,add_emp20)

inventory1 = (200001,'Cropped Sweater','Orange','S',14,19.99)
inventory2 = (200002,'Seamless Leggings','Gray','M',23,9.99)
inventory3 = (200003,'Denim Jacket','Blue','M',12,24.99)
inventory4 = (200004,'Varsity Jacket','Green','XL',15,29.99)
inventory5 = (200005,'Graphic T-Shirt','Black','L',27,14.99)
inventory6 = (200006,'Sweatpants','Gray','M',16,9.99)
inventory7 = (200007,'Winter Coat','Green','M',30,27.99)
inventory8 = (200008,'Knitted Beanie','Pink','OS',5,9.99)
inventory9 = (200009,'Drawstring Hoodie','Black','S',14,14.99)
inventory10 = (200010,'Dinning Room Set','Black',None,5,99.99)
inventory11 = (200011,'Spring Matress','White',None,17,199.99)
inventory12 = (200012,'Leather Recliner','Brown',None,12,49.99)
inventory13 = (200013,'Butterfly Shower Curtain','Pink',None,5,19.99)
inventory14 = (200014,'Wastebasket','White',None,2,7.99)
inventory15 = (200015,'Plush Teddy Bear','Pink',None,6,12.99)
inventory16 = (200016,'Frying Pan Set','Multi',None,20,49.99)
inventory17 = (200017,'Floral Perfum',None,None,5,79.99)
inventory18 = (200018,'Charm Bracelet','Silver',None,7,74.99)
inventory19 = (200019,'Sport Watch','Black',None,3,99.99)
inventory20 = (200020,'Diamond Earrings',None,None,2,499.99)

dbcursor.execute(add_inventory,inventory1)
dbcursor.execute(add_inventory,inventory2)
dbcursor.execute(add_inventory,inventory3)
dbcursor.execute(add_inventory,inventory4)
dbcursor.execute(add_inventory,inventory5)
dbcursor.execute(add_inventory,inventory6)
dbcursor.execute(add_inventory,inventory7)
dbcursor.execute(add_inventory,inventory8)
dbcursor.execute(add_inventory,inventory9)
dbcursor.execute(add_inventory,inventory10)
dbcursor.execute(add_inventory,inventory11)
dbcursor.execute(add_inventory,inventory12)
dbcursor.execute(add_inventory,inventory13)
dbcursor.execute(add_inventory,inventory14)
dbcursor.execute(add_inventory,inventory15)
dbcursor.execute(add_inventory,inventory16)
dbcursor.execute(add_inventory,inventory17)
dbcursor.execute(add_inventory,inventory18)
dbcursor.execute(add_inventory,inventory19)
dbcursor.execute(add_inventory,inventory20)

sale1 = (300001,199.87,'05/06/2015','13:02',100098)
sale2 = (300002,34.50,'09/07/2015','09:34',100063)
sale3 = (300003,78.99,'08/11/2016','14:25',100037)
sale4 = (300004,67.99,'09/23/2015','8:56',100042)
sale5 = (300005,23.89,'07/12/2017','16:07',100063)
sale6 = (300006,56.80,'02/11/2017','12:06',100085)
sale7 = (300007,44.44,'04/04/2014','16:44',100074)
sale8 = (300008,347.00,'07/06/2015','13:00',100023)
sale9 = (300009,90.57,'03/05/2016','20:30',100094)
sale10 = (300010,230.45,'08/25/2017','12:45',100051)
sale11 = (300011,80.99,'01/13/2016','13:46',100019)
sale12 = (300012,34.95,'05/21/2016','17:36',100085)
sale13 = (300013,69.42,'10/14/2015','18:02',100098)
sale14 = (300014,45.99,'08/15/2016','10:25',100037)
sale15 = (300015,80.45,'07/13/2017','10:45',100019)

dbcursor.execute(add_sale,sale1)
dbcursor.execute(add_sale,sale2)
dbcursor.execute(add_sale,sale3)
dbcursor.execute(add_sale,sale4)
dbcursor.execute(add_sale,sale5)
dbcursor.execute(add_sale,sale6)
dbcursor.execute(add_sale,sale7)
dbcursor.execute(add_sale,sale8)
dbcursor.execute(add_sale,sale9)
dbcursor.execute(add_sale,sale10)
dbcursor.execute(add_sale,sale11)
dbcursor.execute(add_sale,sale12)
dbcursor.execute(add_sale,sale13)
dbcursor.execute(add_sale,sale14)
dbcursor.execute(add_sale,sale15)

customer1 = (400001,300007)
customer2 = (400002,300009)
customer3 = (400003,300015)
customer4 = (400004,300010)
customer5 = (400005,300012)
customer6 = (400006,300001)
customer7 = (400007,300002)
customer8 = (400008,300003)
customer9 = (400009,300013)
customer10 = (400010,300006)
customer11 = (400011,300004)
customer12 = (400012,300005)
customer13 = (400013,300008)
customer14 = (400014,300011)
customer15 = (400015,300014)

dbcursor.execute(add_customer,customer1)
dbcursor.execute(add_customer,customer2)
dbcursor.execute(add_customer,customer3)
dbcursor.execute(add_customer,customer4)
dbcursor.execute(add_customer,customer5)
dbcursor.execute(add_customer,customer6)
dbcursor.execute(add_customer,customer7)
dbcursor.execute(add_customer,customer8)
dbcursor.execute(add_customer,customer9)
dbcursor.execute(add_customer,customer10)
dbcursor.execute(add_customer,customer11)
dbcursor.execute(add_customer,customer12)
dbcursor.execute(add_customer,customer13)
dbcursor.execute(add_customer,customer14)
dbcursor.execute(add_customer,customer15)

wage1 = (100012,1,28.00,42.00,38)
wage2 = (100046,1,27.00,40.50,37.50)
wage3 = (100053,1,28.00,42.00,36.33)
wage4 = (100076,1,26.00,39.00,37.50)
wage5 = (100089,1,26.00,39.00,38.50)
wage6 = (100035,1,27.00,40.50,39.00)
wage7 = (100027,1,28.00,42.00,32.00)
wage8 = (100081,1,29.00,43.50,31.50)
wage9 = (100068,1,28.00,42.00,36.00)
wage10 = (100094,1,27.00,40.50,37.00)
wage11 = (100037,1,10.00,15.00,20.00)
wage12 = (100026,1,9.00,13.50,17.50)
wage13 = (100098,1,8.00,12.00,14.00)
wage14 = (100042,1,9.50,14.25,18.00)
wage15 = (100051,1,10.50,15.75,16.33)
wage16 = (100074,1,9.00,13.50,18.50)
wage17 = (100063,1,10.00,15.00,19.40)
wage18 = (100019,1,11.00,16.50,20.50)
wage19 = (100085,1,10.00,15.00,17.00)
wage20 = (100023,1,10.00,15.00,18.00)

dbcursor.execute(add_wage,wage1)
dbcursor.execute(add_wage,wage2)
dbcursor.execute(add_wage,wage3)
dbcursor.execute(add_wage,wage4)
dbcursor.execute(add_wage,wage5)
dbcursor.execute(add_wage,wage6)
dbcursor.execute(add_wage,wage7)
dbcursor.execute(add_wage,wage8)
dbcursor.execute(add_wage,wage9)
dbcursor.execute(add_wage,wage10)
dbcursor.execute(add_wage,wage11)
dbcursor.execute(add_wage,wage12)
dbcursor.execute(add_wage,wage13)
dbcursor.execute(add_wage,wage14)
dbcursor.execute(add_wage,wage15)
dbcursor.execute(add_wage,wage16)
dbcursor.execute(add_wage,wage17)
dbcursor.execute(add_wage,wage18)
dbcursor.execute(add_wage,wage19)
dbcursor.execute(add_wage,wage20)

sold1 = (300001,200020)
sold2 = (300001,200001)
sold3 = (300002,200004)
sold4 = (300003,200011)
sold5 = (300003,200007)
sold6 = (300003,200002)
sold7 = (300004,200010)
sold8 = (300005,200012)
sold9 = (300005,200003)
sold10 = (300006,200009)
sold11 = (300007,200005)
sold12 = (300008,200008)
sold13 = (300009,200013)
sold14 = (300010,200006)
sold15 = (300011,200014)
sold16 = (300012,200015)
sold17 = (300013,200016)
sold18 = (300014,200017)
sold19 = (300015,200018)
sold20 = (300015,200019)
sold21 = (300013,200008)
sold22 = (300008,200004)
sold23 = (300011,200015)

dbcursor.execute(add_sold,sold1)
dbcursor.execute(add_sold,sold2)
dbcursor.execute(add_sold,sold3)
dbcursor.execute(add_sold,sold4)
dbcursor.execute(add_sold,sold5)
dbcursor.execute(add_sold,sold6)
dbcursor.execute(add_sold,sold7)
dbcursor.execute(add_sold,sold8)
dbcursor.execute(add_sold,sold9)
dbcursor.execute(add_sold,sold10)
dbcursor.execute(add_sold,sold11)
dbcursor.execute(add_sold,sold12)
dbcursor.execute(add_sold,sold13)
dbcursor.execute(add_sold,sold14)
dbcursor.execute(add_sold,sold15)
dbcursor.execute(add_sold,sold16)
dbcursor.execute(add_sold,sold17)
dbcursor.execute(add_sold,sold18)
dbcursor.execute(add_sold,sold19)
dbcursor.execute(add_sold,sold20)
dbcursor.execute(add_sold,sold21)
dbcursor.execute(add_sold,sold22)
dbcursor.execute(add_sold,sold23)

pay1 = (300001,'Visa Debit')
pay2 = (300002,'Gift Card')
pay3 = (300002,'Cash')
pay4 = (300003,'Amex')
pay5 = (300004,'Cash')
pay6 = (300005,'Cash')
pay7 = (300006,'Mastercard Debit')
pay8 = (300007,'Amex')
pay9 = (300008,'Cash')
pay10 = (300009,'Cash')
pay11 = (300009,'Gift Card')
pay12 = (300010,'Visa Debit')
pay13 = (300011,'Amex')
pay14 = (300012,'Cash')
pay15 = (300013,'Cash')
pay16 = (300014,'Visa Debit')
pay17 = (300015,'Amex')

dbcursor.execute(add_pay,pay1)
dbcursor.execute(add_pay,pay2)
dbcursor.execute(add_pay,pay3)
dbcursor.execute(add_pay,pay4)
dbcursor.execute(add_pay,pay5)
dbcursor.execute(add_pay,pay6)
dbcursor.execute(add_pay,pay7)
dbcursor.execute(add_pay,pay8)
dbcursor.execute(add_pay,pay9)
dbcursor.execute(add_pay,pay10)
dbcursor.execute(add_pay,pay11)
dbcursor.execute(add_pay,pay12)
dbcursor.execute(add_pay,pay13)
dbcursor.execute(add_pay,pay14)
dbcursor.execute(add_pay,pay15)
dbcursor.execute(add_pay,pay16)
dbcursor.execute(add_pay,pay17)

db.commit()

def menu1(login): #add employee paycheck
    emp = eval(input('Enter employee id: '))
    dbcursor.execute("select employee_id from employee where manager_id = %s", (login,)) #only employees of logged in manager
    result = dbcursor.fetchall()
    emp_flag = 0
    for x in result:
        if emp == x[0]:
            emp_flag = 1
            break
            
    if emp_flag == 0:
        print("You have either entered an incorrect id or an id of an employee you do not manage.")
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            menu1(login)
    else:
        check_no = eval(input('Enter paycheck no: '))
        dbcursor.execute("select paycheck_no from wages where employee_id = %s",(emp,))
        check_flag = 0
        result = dbcursor.fetchall()
        for x in result:
            if check_no == x[0]:
                check_flag = 1
                break

        if check_flag == 1:
            print('This paycheck already exists.')
            again = input('Try again (Y or N)? ')
            if again == 'Y':
                menu1(login)
        else:
            reg = eval(input('Enter employee\'s regular wage: '))
            while reg <= 0:
                print('Wage must be greater than 0.')
                reg = eval(input('Enter employee\'s regular wage: '))
                
            overtime = eval(input('Enter employee\'s overtime wage: '))
            while overtime <= 0:
                print('Wage must be greater than 0.')
                overtime = eval(input('Enter employee\'s overtime wage: '))
                
            hours = eval(input('Enter employee\'s hours: '))
            while hours < 0:
                print('Hours cannot be negative.')
                hours = eval(input('Enter employee\'s hours: '))
                
            check = (emp,check_no,reg,overtime,hours)
            dbcursor.execute(add_wage,check)
            db.commit()
            print('Paycheck added.')

def menu2(login): #modify department information
    modify = input('Enter id of department to be modified: ')
    dbcursor.execute("select dept_id from department")
    dept_flag = 0
    result = dbcursor.fetchall()
    for x in result:
        if modify == x[0]:
            dept_flag = 1
            break

    if dept_flag == 0:
        print('Department not found.')
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            menu2(login)
    else:
        d_id = input('Enter department id: ')
        while len(d_id) > 4:
            print('Department id cannot exceed 4 characters.')
            d_id = input('Enter department id: ')
        
        d_name = input('Enter department name: ')
        d_location = input('Enter department location: ')
        dbcursor.execute("update department set dept_id = %s where dept_id = %s",(d_id,modify))
        dbcursor.execute("update department set name = %s where dept_id = %s",(d_name,d_id))
        dbcursor.execute("update department set location = %s where dept_id = %s",(d_location,d_id))
        db.commit()
        print("Department modified.")

def menu3(login): #terminate employee
    emp = eval(input('Enter employee id: '))
    dbcursor.execute("select employee_id from employee where manager_id = %s", (login,)) #only employees of logged in manager
    result = dbcursor.fetchall()
    emp_flag = 0
    for x in result:
        if emp == x[0]:
            emp_flag = 1
            break
            
    if emp_flag == 0:
        print("You have either entered an incorrect id or an id of an employee you do not manage.")
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            menu3(login)
    else:
        dbcursor.execute("delete from employee where employee_id = %s",(emp,))
        db.commit()
        print('Employee terminated.')

def menu4(login): #process transaction
    trans = eval(input('Enter transaction id: '))
    date = input('Enter date: ')
    time = input('Enter time: ')
    dbcursor.execute("select transaction_id from sale")
    result = dbcursor.fetchall()
    trans_flag = 0
    for x in result:
        if trans == x[0]:
            trans_flag = 1
            break

    if trans_flag == 1:
        print('This transaction id already exists.')
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            menu4(login)
    else:
        dbcursor.execute("insert into sale (transaction_id) values (%s)",(trans,)) #transaction id added to sale table
        db.commit()
        cust = eval(input('Enter customer id: '))
        cust_info = (cust,trans)
        dbcursor.execute(add_customer,cust_info) #customer id and transaction id added to customer table
        add_item = 'Y'
        sale_total = 0
        while add_item == 'Y':
            item = eval(input('Enter product id: '))
            dbcursor.execute("select product_id from inventory") #check if product id exists
            result = dbcursor.fetchall()
            item_flag = 0
            for x in result:
                if item == x[0]:
                    item_flag = 1
                    break

            if item_flag == 0:
                print('Product id not found.')
            else:
                sold_info = (trans,item)
                dbcursor.execute(add_sold,sold_info) #add transaction id and product id to items_sold table
                dbcursor.execute("update inventory set quantity = (quantity - 1) where product_id = %s",(item,))
                db.commit()
                dbcursor.execute("select price from inventory where product_id = %s",(item,))
                result = dbcursor.fetchall()
                for x in result:
                    sale_total = sale_total + x[0] #collects total sale amount

                add_item = input('Add more items (Y or N)? ')

        dbcursor.execute("update sale set amount = %s where transaction_id = %s",(sale_total,trans)) #add amount to sale table
        dbcursor.execute("update sale set date = %s where transaction_id = %s",(date,trans)) #add date to sale table
        dbcursor.execute("update sale set time = %s where transaction_id = %s",(time,trans)) #add time to sale table
        dbcursor.execute("update sale set employee_id = %s where transaction_id = %s",(login,trans)) #add employee id to sale table
        db.commit()

        payment_num = eval(input('How many payment methods is the customer using (Cash, Credit, Debit, Gift Card)? '))
        while payment_num < 1:
            print('Number of payment methods must be greater than 0.')
            payment_num = eval(input('Try agagin: '))

        while payment_num != 0:
            payment = input('Enter payment method: ')
            payment_info = (trans,payment)
            dbcursor.execute(add_pay,payment_info)
            db.commit()
            payment_num = payment_num - 1

        print('Transaction complete.')

def menu5(): #sale history of item
    item = eval(input('Enter product id: '))
    dbcursor.execute("select product_id from inventory")
    result = dbcursor.fetchall()
    item_flag = 0
    for x in result:
        if item == x[0]:
            item_flag = 1
            break

    if item_flag == 0:
        print('Product id not found.')
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            menu5()
    else:
        dbcursor.execute("select date, time from sale natural join items_sold natural join inventory where product_id = %s",(item,))
        result = dbcursor.fetchall()
        print('Item sale history:')
        for x in result:
            print('Date: ',x[0],' Time: ',x[1])

def menu6(login): #sale history of employee
    emp = eval(input('Enter employee id: '))
    dbcursor.execute("select employee_id from employee where manager_id = %s", (login,))
    result = dbcursor.fetchall()
    emp_flag = 0
    for x in result:
        if emp == x[0]:
            emp_flag = 1
            break
            
    if emp_flag == 0:
        print("You have either entered an incorrect id or an id of an employee you do not manage.")
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            menu6(login)
    else:
        dbcursor.execute("select transaction_id, date, time from sale where employee_id = %s",(emp,))
        result = dbcursor.fetchall()
        print('Employee sale history:')
        for x in result:
            print('Transaction: ',x[0],' Date: ',x[1],' Time: ',x[2])

def manager_verify(choice): #manager login
    login = eval(input('Enter manager id: '))
    dbcursor.execute("select manager_id from employee")
    result = dbcursor.fetchall()
    login_flag = 0
    for x in result:
        if login == x[0]:
            login_flag = 1
            break

    if login_flag == 0:
        print('Manager id not found.')
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            manager_verify(choice)
    else:
        verify = input('Enter ssn to verify (xxx-xx-xxxx): ')
        dbcursor.execute("select ssn from employee where employee_id = %s",(login,))
        result = dbcursor.fetchall()
        verify_flag = 0
        for x in result:
            if verify == x[0]:
                verify_flag = 1
                break

        if verify_flag == 0:
            print('Verification failed.')
            again = input('Try again (Y or N)? ')
            if again == 'Y':
                manager_verify(choice)
        else:
            if choice == 1:
                menu1(login)
            elif choice == 2:
                menu2(login)
            elif choice == 3:
                menu3(login)
            else:
                menu6(login)

def emp_verify(choice): #employee login
    login = eval(input('Enter employee id: '))
    dbcursor.execute("select employee_id from employee")
    result = dbcursor.fetchall()
    login_flag = 0
    for x in result:
        if login == x[0]:
            login_flag = 1
            break

    if login_flag == 0:
        print('Employee id not found.')
        again = input('Try again (Y or N)? ')
        if again == 'Y':
            emp_verify(choice)
    else:
        if choice == 4:
            menu4(login)
        else:
            menu5()

print('1. Add employee paycheck (Manager only)')
print('2. Modify department information (Manager only)')
print('3. Terminate employee (Manager only)')
print('4. Process transaction')
print('5. View sale history of an item')
print('6. View employee sale history (Manager only)')
print('7. Exit program')
choice = eval(input('Enter choice: '))

while choice != 7:
    if choice == 1:
        manager_verify(choice)
    elif choice == 2:
        manager_verify(choice)
    elif choice == 3:
        manager_verify(choice)
    elif choice == 4:
        emp_verify(choice)
    elif choice == 5:
        emp_verify(choice)
    elif choice == 6:
        manager_verify(choice)
    else:
        print('You have entered an invalid choice.')
        choice = eval(input('Enter choice: '))

    choice = eval(input('Enter choice: '))

print('Program ended.') 
