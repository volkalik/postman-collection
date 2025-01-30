import xml.etree.ElementTree as ET
import random
import string

# Исходный XML-шаблон
xml_template = '''<Employee>
    <SystemEmployeeId>{system_employee_id}</SystemEmployeeId>
    <EmployeeNumber>89</EmployeeNumber>
    <FirstName>{first_name}</FirstName>
    <LastName>{last_name}</LastName>
    <UserName>{user_name}</UserName>
    <PosId>{pos_id}</PosId>
    <PosClockId>258</PosClockId>
    <GlobalPayRate xsi:nil="true" />
    <DefaultPayGroup>fc88f5e7-de33-4449-919c-e2bc5512f559</DefaultPayGroup>
    <HolidayPayGroup>fc88f5e7-de33-4449-919c-e2bc5512f559</HolidayPayGroup>
    <AnnualSalary xsi:nil="true" />
    <BaseHours xsi:nil="true" />
    <Status>Active</Status>
    <ShortName />
    <Type>Permanent</Type>
    <DateInserted xsi:nil="true" />
    <EmployeeClassificationID>5</EmployeeClassificationID>
    <DateOfBirth xsi:nil="true" />
    <IsMealWaivered>false</IsMealWaivered>
    <DateUpdated>2020-07-26T14:13:42</DateUpdated>
    <MiddleName />
    <Title>Mr</Title>
    <Since xsi:nil="true" />
    <City />
    <Address1 />
    <Address2 />
    <State />
    <PostCode />
    <Country>0</Country>
    <User_Email />
    <Telephone />
    <Mobile />
    <EmergencyContact />
    <EmergencyPhone />
    <UserId>134441</UserId>
    <EntityId>1100</EntityId>
    <StatusDateUpdated>2020-07-20T15:57:59</StatusDateUpdated>
    <POSOperatorModeCode />
    <POSSecurityRoleCode>XPOS Cashier</POSSecurityRoleCode>
    <PayrollId />
    <HasBenefits>false</HasBenefits>
    <IsMinor>false</IsMinor>
    <ExcludeFromPayCalculation>false</ExcludeFromPayCalculation>
    <EmployeeJob>
      <Id>118518</Id>
      <SystemEmployeeId>134441</SystemEmployeeId>
      <EmployeeJobPayRate>0.00</EmployeeJobPayRate>
      <IsPrimary>true</IsPrimary>
      <HourlyPayRateRuleOverride xsi:nil="true" />
      <OvertimePayRateRuleOverride>0.00</OvertimePayRateRuleOverride>
      <LabourJobType>
        <JobRoleList>
          <RoleId>2</RoleId>
          <Name>Front Counter Cashier</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#CC00CC</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>4</RoleId>
          <Name>Front Counter Packer</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#6600FF</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>10</RoleId>
          <Name>A &amp; W Builder</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#996600</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>11</RoleId>
          <Name>Coordinator</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#CCFF00</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>13</RoleId>
          <Name>Dining Room</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#CC0066</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>16</RoleId>
          <Name>Drive Thru Cashier</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#33FF00</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>17</RoleId>
          <Name>Drive Thru Packer</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#339999</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>18</RoleId>
          <Name>Drinks/Sweets &amp; Treats</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#FF0066</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>20</RoleId>
          <Name>Meeting</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#0099CC</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>true</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>24</RoleId>
          <Name>Food Preparation</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#66CCFF</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobRoleList>
          <RoleId>30</RoleId>
          <Name>Delivery/Stock Room</Name>
          <LeadInBuffer>0</LeadInBuffer>
          <ForegroundColour>#000000</ForegroundColour>
          <BackgroundColour>#339999</BackgroundColour>
          <IsEnabled>true</IsEnabled>
          <IsMultiResource>false</IsMultiResource>
          <IsIndirect>false</IsIndirect>
          <IsAutoClock>false</IsAutoClock>
          <NoTrainingNeeded>false</NoTrainingNeeded>
        </JobRoleList>
        <JobId>1</JobId>
        <Name>Cashier</Name>
        <PayRate>0.00</PayRate>
        <IsEnabled>true</IsEnabled>
        <POSJobId>2</POSJobId>
        <IsDefault>true</IsDefault>
        <IsManagement>false</IsManagement>
        <ExcludePay>false</ExcludePay>
        <JobClassId xsi:nil="true" />
        <LabourTypeID xsi:nil="true" />
      </LabourJobType>
      <LegacyJobID>0</LegacyJobID>
    </EmployeeJob>
    <EmployeeRole>
      <Role>
        <RoleId>27</RoleId>
        <Name>Restaurant Manager</Name>
        <LeadInBuffer>0</LeadInBuffer>
        <ForegroundColour>#000000</ForegroundColour>
        <BackgroundColour>#9966CC</BackgroundColour>
        <IsEnabled>true</IsEnabled>
        <IsMultiResource>false</IsMultiResource>
        <IsIndirect>false</IsIndirect>
        <IsAutoClock>false</IsAutoClock>
        <NoTrainingNeeded>false</NoTrainingNeeded>
      </Role>
      <Id>958359</Id>
      <IsPreferred>true</IsPreferred>
      <IsTrained>false</IsTrained>
      <IsEnabled>true</IsEnabled>
      <Priority>0</Priority>
    </EmployeeRole>
    <EmployeeStore>
      <EmployeeStoreId>143255</EmployeeStoreId>
      <EntityId>1100</EntityId>
      <UserId>134441</UserId>
      <IsDefault>true</IsDefault>
      <IsTemporary>false</IsTemporary>
      <HasTemporaryAccess>false</HasTemporaryAccess>
      <StoreNumber>12345</StoreNumber>
    </EmployeeStore>
    <WorkWeeksPerYear>52</WorkWeeksPerYear>
    <WorkHoursPerWeek>40</WorkHoursPerWeek>
    <EmployeeOnCost />
    <PayAllBreaks>false</PayAllBreaks>
  </Employee>'''

# Функция для генерации случайного имени
def random_string(length=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Создание 20 копий XML-файла с уникальными значениями
for i in range(1, 101):
    system_employee_id = 634441 + i
    first_name = f"FirstName{i}"
    last_name = f"LastName{i}"
    user_name = f"UserName{i}"
    pos_id = 1258 + i

    # Формирование XML-данных
    xml_data = xml_template.format(
        system_employee_id=system_employee_id,
        first_name=first_name,
        last_name=last_name,
        user_name=user_name,
        pos_id=pos_id
    )

    # Запись XML-файла
    with open(f'employee_{i}.xml', 'w') as file:
        file.write(xml_data)

print("20 XML файлов созданы успешно.")
