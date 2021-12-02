import datetime
import json
from db_handler.add_attendance_func import AddAttendanceFunc
obj_add_att = AddAttendanceFunc()
from datetime import date
class AddAttendance:

 
    
    


    def add_attendance_func(self):

        

        data_file = obj_add_att.read_json()
        date_dict = obj_add_att.enter_date()
        list_of_details = obj_add_att.details_list(data_file)
        

        attendance_dict = {
            "date":date_dict,
            "details":list_of_details
        }

        

        obj_add_att.to_json(attendance_dict)

        

