import json


# получение финального списка всех компаний без использования рекурсии
with open('new_test_hw.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

startList = data['children']
resultList = []

while startList:
    curr_el = startList.pop()
    if isinstance(curr_el, dict):
        if 'id' in curr_el and 'title' in curr_el:
            resultList.append((curr_el['title'], curr_el['id']))

        if 'children' in curr_el and isinstance(curr_el['children'], list):
            startList.extend(curr_el['children'])

    elif isinstance(curr_el, list):
        startList.extend(curr_el)

resultList.sort(key=lambda company: company[1])

with open('result_file_without_recursion.json', 'w', encoding='utf-8') as file_obj:
    json.dump(resultList, file_obj, ensure_ascii=False, indent=4)
