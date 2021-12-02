import json

from os import access


class Create_Employee:

    
    
    def new_employee(self,employee_id,name,department,job):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.job = job

        employees = {
            'Employee_ID':self.employee_id,
            'Name':self.name,
            'Department':self.department,
            'Job':self.job
            }

        employees1 = json.dumps(employees,indent=4)
        with open('database/sample2.json','r') as access_json:
            data = json.load(access_json)
            access_json.close()

        
        data['employee_details'].append(employees)

        with open('database/sample2.json','w') as outfile:
            data = json.dumps(data,indent=4)
            outfile.write(data)
            outfile.close()
            

        







    



 