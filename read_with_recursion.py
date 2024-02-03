import json


# на самом деле, не знаю насколько корректно я написал рекурсивную функцию.
# обычно подобный перебор я выполняю иначе. Пример есть в соседнем файле
def recursive_function(curr_element: list | dict) -> list:
    global resultList
    if isinstance(curr_element, list):
        for elem in curr_element:
            if isinstance(elem, dict):
                resultList.append((elem['title'], elem['id']))
            if isinstance(elem, dict) and 'children' in elem:
                recursive_function(elem['children'])

    elif isinstance(curr_element, dict):
        if 'id' in curr_element and 'title' in curr_element:
            resultList.append((curr_element['title'], curr_element['id']))
        if 'children' in curr_element and isinstance(curr_element['children'], list):
            recursive_function(curr_element['children'])

    return resultList


with open('new_test_hw.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

resultList = []
res = recursive_function(curr_element=data)

# при желании можно сохранить итоговый список в файл без стартовой вложенности (еще и с сортировкой=)
with open('result_file_with_recursion.json', 'w', encoding='utf-8') as file_obj:
    json.dump(sorted(resultList, key=lambda comp: comp[1]), file_obj, ensure_ascii=False, indent=4)
