import json
import random
import uuid

# Количество записей
num_records = 3000

# Шаблон данных с полем "closed"
data = {
    "business_date": "2024-10-04T00:00:00.000Z",
    "closed": [
        {
            "_id": str(uuid.uuid4()),
            "order_number": f"{200000 + i}",
            "net_sales": round(random.uniform(20, 50), 2),
            "gross_sales": round(random.uniform(30, 60), 2)
        } for i in range(num_records)
    ],
    "deleted": [
        {
            "_id": str(uuid.uuid4()),
            "order_number": "200082",
            "net_sales": 0.00,
            "gross_sales": 0.00
        }
    ],
    "saved": [
        {
            "_id": str(uuid.uuid4()),
            "order_number": "200077",
            "net_sales": 0.00,
            "gross_sales": 0.00
        },
        {
            "_id": str(uuid.uuid4()),
            "order_number": "200078",
            "net_sales": 0.00,
            "gross_sales": 0.00
        }
    ]
}

# Преобразование данных в JSON-строку с экранированными кавычками
json_data = json.dumps(data)
json_data_escaped = json_data.replace('"', r'\"')

# Вывод результата
print(json_data_escaped)

with open('business_date_update.json', 'w') as file:
    file.write(json_data_escaped)