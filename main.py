import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer =csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Email ID"])
        writer.writerow(info_list)

if __name__== '__main__' :
    condition = True
    student_num=1

    while(condition):
        student_info=input("Enter the information for student #{} in following format (Name Age Email_Id): ".format(student_num))
        
        student_info_list =student_info.split(' ')
        
        print("The entered information is -\nName :{} \nAge :{} \nEmail ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2]))
        
        choice_check = input("Is the entered data correct? (yes/no) :")
        
        if choice_check== "yes" :
        
            write_into_csv(student_info_list)
            
            
            condition_check=input("Do you wish to submit more information?(yes/no): ")
            if condition_check=="yes" :
                condition=True
                student_num+=1
            elif condition_check=="no" :
                condition=False
        elif choice_check=="no" :
            print("\n Please re-enter the values!")