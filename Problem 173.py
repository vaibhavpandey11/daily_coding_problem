'''
This problem was asked by Stripe.
Write a function to flatten a nested dictionary.
Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

#______________________________________________

# It is assumed that the input is in the format -
# {"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}
# The function given below enters the inner dictionaries and flattens them until no inner dictionary is found
def nested_to_flat(key, value, pre_key):  # 'pre_key' is the outer key which is concatenated with inner keys    
    if not type(value) == dict:  # item simply added in 'result_dic' dictionary       
        if pre_key == "": result_dic[str(key)] = value
        else: result_dic[pre_key + "." + str(key)] = value        
    else:  # when 'value' is dictionary, pre_key is updated and inner items (i.e key: value) are passed to the function itself, i.e recursion
        if pre_key == "": pre_key = str(key)
        else: pre_key = pre_key + "." + str(key)
        for inner_key, inner_value in value.items(): nested_to_flat(inner_key, inner_value, pre_key)  # recursion

dic, result_dic = eval(input()), dict()
for item_key, item_value in dic.items():  # items (i.e key: value) of input dictionary
    nested_to_flat(item_key, item_value, "") # empty string passed in 'pre_key' argument when the item (i.e key: value) of input dictionary changes
    
print(result_dic)
