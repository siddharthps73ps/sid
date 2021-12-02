import json
from db_handler.delete_employee_func import DeleteEmployeeFunc

object_delete = DeleteEmployeeFunc()





class DeleteEmployee:
    

    def delete_emp_func(self):

        
        data_as_list = object_delete.read_from_json()
        employee_ids = object_delete.list_of_employees_id(data_as_list)
        print(f'Registered Employee IDs are: {employee_ids}')
        id_to_delete = input("Enter Employee ID to delete")

        if id_to_delete in employee_ids:

            position = object_delete.find_position(employee_ids,id_to_delete)
            to_remove = data_as_list['employee_details'][position]
            data_as_list['employee_details'].remove(to_remove)

            data = json.dumps(data_as_list,indent=4)
            with open('database/sample2.json','w') as outfile:
                outfile.write(data)
                outfile.close()






