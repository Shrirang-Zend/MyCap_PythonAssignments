import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer =csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Email ID"])
        writer.writerow(info_list)

ques= input("Do you wish to submit information about a Student? (yes/no) ")

if ques=="yes" :

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

def calculate_fees(months_pending):
    fee_per_month = 12000
    total_fees = fee_per_month * months_pending
    return total_fees

def calculate_grade(maths, science, english, language, ssc):
    average_marks = (maths + science + english + language + ssc) / 5
    if average_marks >= 90:
        return "A+"
    elif average_marks >= 80:
        return "A"
    elif average_marks >= 70:
        return "B+"
    elif average_marks >= 60:
        return "B"
    elif average_marks >= 50:
        return "C+"
    elif average_marks >= 40:
        return "C"
    else:
        return "F"

pay_fees = input("Do you want to pay fees? (yes/no) ")
if pay_fees.lower() == "yes":
    months_pending = int(input("Enter the number of months of fees pending: "))
    total_fees = calculate_fees(months_pending)
    print("Total fees to be paid: {}" .format(total_fees))
else:
    print("No fees will be paid.")
    
calculate_grade_flag = input("Do you want to calculate your grade? (yes/no) ")
if calculate_grade_flag.lower() == "yes":
    maths = int(input("Enter marks for Maths: "))
    science = int(input("Enter marks for Science: "))
    english = int(input("Enter marks for English: "))
    language = int(input("Enter marks for Language: "))
    ssc = int(input("Enter marks for SSC: "))

    grade = calculate_grade(maths, science, english, language, ssc)
    print("Grade: {}" .format(grade))
else:
    print("No grade will be calculated.")
