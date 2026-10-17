import json


json_string = '{"name" : "Alice"}'
data = json.loads(json_string)
print(type(data))
print(data['name'])

# 파이썬 객체를 json 문자열로 변환

python_dict = {'name':'bob','age':30}
# json_output = json.dumps(python_dict,indent= 4) #indent 들여쓰기하는것
# print(json_output)

path = r'ch21\json_file\json\data.json'
with open(path,'w') as file:
    json.dump(python_dict,file,indent=4)

with open(path,'r')as file:
    load_data = json.load(file)
print(load_data)