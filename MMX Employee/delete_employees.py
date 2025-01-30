import subprocess

# Файл с идентификаторами
file_path = 'ids.txt'

# Шаблон команды cURL
curl_command_template = '''curl --location --request DELETE 'https://qa-backoffice-api-us-east-1.xenial.com/Staff/Employee/{id}' \
--header 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhwcnQifQ.eyJzdWIiOiJodHRwczovL3FhLXhwcnRiYWNrZW5kLnhlbmlhbC5jb20vcGVvcGxlLzVkZWJhOWUxNzg2YmQ0MDAwOGRhYThhZiIsInBlcnNvbl9pZCI6IjVkZWJhOWUxNzg2YmQ0MDAwOGRhYThhZiIsImNvbXBhbnlfaWQiOiI2MzYxYjQ4NjllODhhOGU4YTk4NjZiY2EiLCJhdWQiOlsiWEJPRiIsIlhQT1MiLCIxMjMxMjMiLCJYRE0iLCJUQTUxIiwiWExPRyIsIkd1ZXN0bGlzdCIsIlhQTCIsIlhNTSIsIlhEQSIsInRlc3RhcHAxIiwiUU0iLCJNTU1hcHM1ODg1IiwiWFBSVCIsIkNSTSIsIlhPTyIsInRvZGVsZXRlIiwiODg5IiwiMzMzIiwiV0ZIIiwiV0hTIiwiWFBPU0JvemhvayIsIlhNRSIsIkRDQVNURUxMQU5PX1ZFUlNJT04iLCJNTXRlc3Q1IiwiTU1NYXBzNzciLCJBbGV4MjFhcHM1NSIsIlNJR01VTkRTIiwiRE1XIiwibW1hcHBzNSIsIkFXWENGIiwiTU1NYXBzMDAxIiwiMTIzNDUiLCJLQVBTIiwiMTU1MTIyMjMiLCJNTU1hcHM1NWQiLCJYUFIxIiwiTU1NYXBzNTU1NTUiLCJYU0FDIiwiWFZPIiwiWENBVCIsIktGQzAwMSIsIjY2NiIsInh2aSIsIkZpeCIsIlhCTyIsImcxIiwiZzIiLCIxIiwiYXRfdGVzdCIsImdnMSIsIlRlc3RGb3JBbGV4IiwiMy45LjQ2IiwiWE1PIl0sInRva2VuX3R5cGUiOiJhY2Nlc3MiLCJpYXQiOjE3Mzc3MzE0MzQsImV4cCI6MTczNzgxNzgzNCwiaXNzIjoicWEteHBydGJhY2tlbmQueGVuaWFsLmNvbSJ9.DJ7_UiWTtILbctWSGV8UCT_AQ1BU8j4aQVOgJfa3OWk' \
--header 'content-type: application/json' \
--header 'x-company-id: 6361b4869e88a8e8a9866bca' '''

# --header 'x-company-id: 62e92d9a1dffdb1604e1c9db' '''


# Открываем файл и читаем идентификаторы
with open(file_path, 'r') as file:
    ids = file.readlines()

# Удаляем символы новой строки из идентификаторов
ids = [id.strip() for id in ids]

# Выполняем команду cURL для каждого идентификатора
for id in ids:
    curl_command = curl_command_template.format(id=id)
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    print(f"Request for ID {id} returned status code: {result.returncode}")
    print(f"Response: {result.stdout}")
    if result.stderr:
        print(f"Error: {result.stderr}")
