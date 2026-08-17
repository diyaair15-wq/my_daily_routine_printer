import array as arr

aray_num = arr.array('i', [1,3,5,3,7,9,3])
print('Original array: '+ str(aray_num))

print('number of occurrences of the mentioned value: '+ str(aray_num.count(3)))

aray_num.reverse()
print('reverse the order of the items:')
print(str(aray_num))