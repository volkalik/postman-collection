file_path = '/Users/oleksandr.volk/Documents/PPL/Pipeline_logs/qa-fiscal-transactions-logs-4.gz'

import gzip

input_file_path = '/Users/oleksandr.volk/Downloads/devlab-fiscal-transactions-logs-19-24.gz'
output_file_path = '/Users/oleksandr.volk/Documents/PPL/Pipeline_logs/fl-1.json'

try:
    # Попытка открыть как gzip файл
    with gzip.open(input_file_path, 'rt') as input_file:
        content = input_file.read()
except gzip.BadGzipFile:
    print("Файл не является gzip архивом. Читаю как обычный файл...")
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

# Сохранение содержимого в новый файл
with open(output_file_path, 'w') as output_file:
    output_file.write(content)

print(f"Содержимое успешно сохранено в {output_file_path}")

