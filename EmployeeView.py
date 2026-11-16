from mysql import connector
from datetime import datetime

class EmployeeManager:
    def __init__(self):
        self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Navneetha@2005",
            database = "company_db"
        )
        
        print("Connection successfull..")
        
    def get_object(self, id = None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from employee where id = %s"
            value = (id,)
            self.cursor.execute(query,value)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
            
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = """insert into employee(emp_name, 
                        age, gender, mobile, email, departement,
                        designation, salary, experience, joining_date, status) 
                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values = [v for v in kwargs.values()]
            
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Data inserted successfully..")
        except Exception as e:
            print(e)
            
    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            for i in records:
                print(i)
        except Exception as e:
            print(e)
            
    def retrieve(self, id = None):
        try:
            record = self.get_object(id = id)
            if record == None:
                print("No employees found..")
            else:
                print(record)
        except Exception as e:
            print(e)
            
    def delete(self, id = None):
        try:
            record = self.get_object(id = id)
            if record != None:
                query = "delete from employee where id = %s"
                self.cursor.execute(query, (id,))
                self.connection.commit()
                print("Employee Deleted Successfully..")
            else:
                print("No employees found..")
        except Exception as e:
            print(e)
    def put(self ,id =None,**kwargs):
        try:
            record =self.get_object(id=id)
            if record !=  None:
                self.cursor =self.connection.cursor()
                placeholder =""
                for k in kwargs.keys():
                    placeholder +=k + "=%s, "
                placeholder =placeholder.rstrip(" , ")
                query =f"update employee set {placeholder}  where id=%s"
                values =[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Employee update sucessfully....!")
            else:
                print("No employee found....!")
        except Exception as e:
            print(e)             
            
employee_instance = EmployeeManager()
# employee_instance.post(
#     emp_name="Amritha",
#     age=20,
#     gender="Female",
#     mobile="9876543265",
#     email="Ammu@gmail.com",
#     departement="IT",
#     designation="Software testing",
#     salary=35000.50,
#     experience=2,
#     joining_date = datetime.today(),
#     status="Active"
# )
employee_instance.get()
#employee_instance.retrieve(id = 5)
#employee_instance.delete(id = 5)
# employee_instance.put(id=1,emp_name="Anu",
#     age=25,
#      gender="Female",
#      mobile="9876543299",
#      email="Anu@gmail.com",
#      departement="IT",
#      designation="Software testing",
#      salary=75000.50,
#      experience=3,
#      joining_date = datetime.today(),
#      status="Active"
#  )