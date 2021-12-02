

import json

class EditEmployee:

    def edit_emp_func(self):


    

        def read_json():

            with open('database/sample2.json') as access_json:
                data = json.load(access_json)
                
            return data


        def search_for_employee(file_data):
            data_as_list=file_data



            def edit_now(file,position):

                new_name = input("Enter name")
                new_department = input("Enter Department")
                new_job = input("Enter Job")

                file['employee_details'][position]['Name']=new_name
                file['employee_details'][position]['Department']=new_department
                file['employee_details'][position]['Job']=new_job
                
                return file



            def list_of_employees(data_as_list):
                employee_ids = []
                length = len(data_as_list['employee_details'])

                for i in range(length):
                    employee_ids.append(data_as_list['employee_details'][i]['Employee_ID'])

                return employee_ids
            
            
            
            employee_id_list = list_of_employees(data_as_list)
            print(f'Registered IDs are : {employee_id_list} Choose the Employee to EDIT')

            input_id_to_search = input("Enter Employee ID to edit")


            if input_id_to_search in employee_id_list:

                position = (employee_id_list.index(input_id_to_search))
                y = edit_now(data_as_list,position)


            else:
                print("Employee ID not found")
                pass
            
            
            data = json.dumps(y,indent=4)
            with open('database/sample2.json','w') as outfile:
                outfile.write(data)
                outfile.close()
                
            return y


        file_data = read_json()
        final_file_after_edit = search_for_employee(file_data)
        print(final_file_after_edit)
        return 
        






    


