import xml.etree.ElementTree as ET
import random
import string


# Функция для генерации случайного имени
def random_string(length=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


# Создание корневого элемента
root = ET.Element("ArrayOfEmployee")

# Создание 20 уникальных элементов Employee
for i in range(1, 351):
    employee = ET.SubElement(root, "Employee")

    system_employee_id = 72001 + i
    EmployeeNumber = 25001 + i
    first_name = f"Anny{i}"
    last_name = f"Torry{i}"
    user_name = f"AT{i}"
    pos_id = 46000 + i
    userid = str(66501 + i)
    employeestoreid = str(282255 + i)
    entityid = str(71501 + i)

    ET.SubElement(employee, "SystemEmployeeId").text = str(system_employee_id)
    ET.SubElement(employee, "EmployeeNumber").text = str(EmployeeNumber)
    ET.SubElement(employee, "FirstName").text = first_name
    ET.SubElement(employee, "LastName").text = last_name
    ET.SubElement(employee, "UserName").text = user_name
    ET.SubElement(employee, "PosId").text = str(pos_id)
    ET.SubElement(employee, "PosClockId").text = "258"
    ET.SubElement(employee, "GlobalPayRate", {"xsi:nil": "true"})
    ET.SubElement(employee, "DefaultPayGroup").text = "fc88f5e7-de33-4449-919c-e2bc5512f559"
    ET.SubElement(employee, "HolidayPayGroup").text = "fc88f5e7-de33-4449-919c-e2bc5512f559"
    ET.SubElement(employee, "AnnualSalary", {"xsi:nil": "true"})
    ET.SubElement(employee, "BaseHours", {"xsi:nil": "true"})
    ET.SubElement(employee, "Status").text = "Active"
    ET.SubElement(employee, "ShortName")
    ET.SubElement(employee, "Type").text = "Permanent"
    ET.SubElement(employee, "DateInserted", {"xsi:nil": "true"})
    ET.SubElement(employee, "EmployeeClassificationID").text = "5"
    ET.SubElement(employee, "DateOfBirth", {"xsi:nil": "true"})
    ET.SubElement(employee, "IsMealWaivered").text = "false"
    ET.SubElement(employee, "DateUpdated").text = "2024-05-26T14:13:42"
    ET.SubElement(employee, "MiddleName")
    ET.SubElement(employee, "Title").text = "Mr"
    ET.SubElement(employee, "Since", {"xsi:nil": "true"})
    ET.SubElement(employee, "City")
    ET.SubElement(employee, "Address1")
    ET.SubElement(employee, "Address2")
    ET.SubElement(employee, "State")
    ET.SubElement(employee, "PostCode")
    ET.SubElement(employee, "Country").text = "0"
    ET.SubElement(employee, "User_Email")
    ET.SubElement(employee, "Telephone")
    ET.SubElement(employee, "Mobile")
    ET.SubElement(employee, "EmergencyContact")
    ET.SubElement(employee, "EmergencyPhone")
    ET.SubElement(employee, "UserId").text = userid
    ET.SubElement(employee, "EntityId").text = entityid
    ET.SubElement(employee, "StatusDateUpdated").text = "2024-05-20T15:57:59"
    ET.SubElement(employee, "POSOperatorModeCode")
    ET.SubElement(employee, "POSSecurityRoleCode").text = "XPOS Cashier"
    ET.SubElement(employee, "PayrollId")
    ET.SubElement(employee, "HasBenefits").text = "false"
    ET.SubElement(employee, "IsMinor").text = "false"
    ET.SubElement(employee, "ExcludeFromPayCalculation").text = "false"

    # EmployeeJob элемент
    employee_job = ET.SubElement(employee, "EmployeeJob")
    ET.SubElement(employee_job, "Id").text = str(139518 + i)
    ET.SubElement(employee_job, "SystemEmployeeId").text = str(system_employee_id)
    ET.SubElement(employee_job, "EmployeeJobPayRate").text = "0.00"
    ET.SubElement(employee_job, "IsPrimary").text = "true"
    ET.SubElement(employee_job, "HourlyPayRateRuleOverride", {"xsi:nil": "true"})
    ET.SubElement(employee_job, "OvertimePayRateRuleOverride").text = "0.00"

    labour_job_type = ET.SubElement(employee_job, "LabourJobType")

    job_roles = [
        {"RoleId": 2, "Name": "Front Counter Cashier", "BackgroundColour": "#CC00CC"},
        {"RoleId": 4, "Name": "Front Counter Packer", "BackgroundColour": "#6600FF"},
        {"RoleId": 10, "Name": "A & W Builder", "BackgroundColour": "#996600"},
        {"RoleId": 11, "Name": "Coordinator", "BackgroundColour": "#CCFF00"},
        {"RoleId": 13, "Name": "Dining Room", "BackgroundColour": "#CC0066"},
        {"RoleId": 16, "Name": "Drive Thru Cashier", "BackgroundColour": "#33FF00"},
        {"RoleId": 17, "Name": "Drive Thru Packer", "BackgroundColour": "#339999"},
        {"RoleId": 18, "Name": "Drinks/Sweets & Treats", "BackgroundColour": "#FF0066"},
        {"RoleId": 20, "Name": "Meeting", "BackgroundColour": "#0099CC"},
        {"RoleId": 24, "Name": "Food Preparation", "BackgroundColour": "#66CCFF"},
        {"RoleId": 30, "Name": "Delivery/Stock Room", "BackgroundColour": "#339999"},
    ]

    for job in job_roles:
        job_role_list = ET.SubElement(labour_job_type, "JobRoleList")
        ET.SubElement(job_role_list, "RoleId").text = str(job["RoleId"])
        ET.SubElement(job_role_list, "Name").text = job["Name"]
        ET.SubElement(job_role_list, "LeadInBuffer").text = "0"
        ET.SubElement(job_role_list, "ForegroundColour").text = "#000000"
        ET.SubElement(job_role_list, "BackgroundColour").text = job["BackgroundColour"]
        ET.SubElement(job_role_list, "IsEnabled").text = "true"
        ET.SubElement(job_role_list, "IsMultiResource").text = "false"
        ET.SubElement(job_role_list, "IsIndirect").text = "false"
        ET.SubElement(job_role_list, "IsAutoClock").text = "false"
        ET.SubElement(job_role_list, "NoTrainingNeeded").text = "false"

    ET.SubElement(labour_job_type, "JobId").text = "1"
    ET.SubElement(labour_job_type, "Name").text = "Cashier"
    ET.SubElement(labour_job_type, "PayRate").text = "0.00"
    ET.SubElement(labour_job_type, "IsEnabled").text = "true"
    ET.SubElement(labour_job_type, "POSJobId").text = "2"
    ET.SubElement(labour_job_type, "IsDefault").text = "true"
    ET.SubElement(labour_job_type, "IsManagement").text = "false"
    ET.SubElement(labour_job_type, "ExcludePay").text = "false"
    ET.SubElement(labour_job_type, "JobClassId", {"xsi:nil": "true"})
    ET.SubElement(labour_job_type, "LabourTypeID", {"xsi:nil": "true"})
    ET.SubElement(employee_job, "LegacyJobID").text = "0"

    # EmployeeRole элемент
    employee_role = ET.SubElement(employee, "EmployeeRole")
    role = ET.SubElement(employee_role, "Role")
    ET.SubElement(role, "RoleId").text = "27"
    ET.SubElement(role, "Name").text = "Restaurant Manager"
    ET.SubElement(role, "LeadInBuffer").text = "0"
    ET.SubElement(role, "ForegroundColour").text = "#000000"
    ET.SubElement(role, "BackgroundColour").text = "#9966CC"
    ET.SubElement(role, "IsEnabled").text = "true"
    ET.SubElement(role, "IsMultiResource").text = "false"
    ET.SubElement(role, "IsIndirect").text = "false"
    ET.SubElement(role, "IsAutoClock").text = "false"
    ET.SubElement(role, "NoTrainingNeeded").text = "false"
    ET.SubElement(employee_role, "Id").text = str(959359 + i)
    ET.SubElement(employee_role, "IsPreferred").text = "true"
    ET.SubElement(employee_role, "IsTrained").text = "false"
    ET.SubElement(employee_role, "IsEnabled").text = "true"
    ET.SubElement(employee_role, "Priority").text = "0"

    # EmployeeStore элемент
    employee_store = ET.SubElement(employee, "EmployeeStore")
    ET.SubElement(employee_store, "EmployeeStoreId").text = employeestoreid
    ET.SubElement(employee_store, "EntityId").text = "1100"
    ET.SubElement(employee_store, "UserId").text = userid
    ET.SubElement(employee_store, "IsDefault").text = "true"
    ET.SubElement(employee_store, "IsTemporary").text = "false"
    ET.SubElement(employee_store, "HasTemporaryAccess").text = "false"
    ET.SubElement(employee_store, "StoreNumber").text = "6789"

    ET.SubElement(employee, "WorkWeeksPerYear").text = "52"
    ET.SubElement(employee, "WorkHoursPerWeek").text = "40"
    ET.SubElement(employee, "EmployeeOnCost")
    ET.SubElement(employee, "PayAllBreaks").text = "false"

# Создание дерева и запись в файл
tree = ET.ElementTree(root)
tree.write("12345_employees12.xml", encoding="utf-8", xml_declaration=True)

print("350 employees have been created.")
