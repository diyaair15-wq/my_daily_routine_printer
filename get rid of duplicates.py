student_data = {
    "id1": {"name": "sara", "class": "V", "subject": "english,science,maths"},
    "id2": {"name": "david", "class": "V", "subject": "english,science,maths"},
    "id3": {"name": "sara", "class": "V", "subject": "english,science,maths"},
    "id4": {"name": "surya", "class": "V", "subject": "english,science,maths"},
}

result = {}
seen_keys = []

for student_id, student_info in student_data.items():
    unique_key = (student_info["name"], student_info["class"], student_info["subject"])
    
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = student_info   
        
for k, v in result.items():
    print(k,":", v)
    
    
    