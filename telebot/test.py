import json
import requests

res = requests.get('https://api.telegram.org/bottok/getMe')

# Если вы работаете с данными в формате JSON, воспользуйтесь встроенным JSON декодером:
print(res.json())


# python test.py 
# {'ok': True, 'result': {'id': 1909564749, 'is_bot': True, 'first_name': 'januspy', 'username': 'januspybot', 'can_join_groups': True, 'can_read_all_group_messages': False, 'supports_inline_queries': False}}
