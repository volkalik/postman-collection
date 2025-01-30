from pathlib import Path

test_path = "https://cicd.xenial.com/job/INTEGRATION-TESTS/job/TEST-INTEGRATION-API/15390/"
console_log = "/Users/oleksandr.volk/Documents/consoleText.txt"
res = ""
tests = []
status = "Failed"

with open(console_log) as f:
    for line in f:
        if f"Result: {status}" in line:
            tests.append(line.split("Finish test")[1].split("'")[1])

for test in tests:
    test = test.replace("-", "_")
    for path in Path(test_path).rglob('*py'):
        try:
            if str(path).endswith(f"test_{test}.py") or str(path).endswith(test):
                a = str(path).split("tea-pos-app/")[1]
                res += a + " "
                break
        except IndexError:
            pass


print(f"{len(tests)} {status} tests\n{res}")
print('\n'.join(tests))
#
# test_path - путь к общей папке с тестами
# на 4 строке путь к файлу лога дженкинса, просто скачать его
# скрипт принтонет строку на реран