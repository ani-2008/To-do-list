import json

with open("list.json") as f:
    data = f.read()

todo_dict = json.loads(data)

count = 0
def check_through_taskes(count,task,label,status):
    for i in range(count):
        if str(i) not in todo_dict[label]:
            continue
        elif task == todo_dict[label][str(i)][0] and status != todo_dict[label][str(i)][1]:
            return True
        else:
            return False

def delete_task(choice):
    del_task = False
    del_status = False
    
    string_count = "0"
    if choice == "y":
        
        if todo_dict=={}:
            print("List is empty")
            return False
        else:
            ask_label = input("Label:").strip()
            if ask_label in todo_dict:
                ask_task = input("Task:").strip()
                for i in todo_dict[ask_label].keys():
                    
                    if ask_task in todo_dict[ask_label][i]:
                        string_count = i
                        del_task = todo_dict[ask_label][i][0]
                        del_status =  todo_dict[ask_label][i][1]
                        
                        break
                    else:
                        continue

            else:
                print("Label not found")
                return False


    if del_task and del_status and string_count:
        
        del todo_dict[ask_label][string_count][0]
        del todo_dict[ask_label][string_count][0]
    
    
    if todo_dict[ask_label][string_count] == []:
        del todo_dict[ask_label][string_count]
    if todo_dict[ask_label] == {}:
        del todo_dict[ask_label]
    
    new_dict = {}
    list_c = []
    for str_c in todo_dict[ask_label].keys():
        list_c.append(int(str_c))
    

    return todo_dict,string_count

def change_dict_json(obj):
    return ((((((json.dumps(obj,indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",","")

def main():
    global todo_dict
    global count
    global string_count
    string_count = "0"
    while True:
        
        print("To exit type exit")
        print("To display type display")
        choice = input("Do you want to delete any task ? (y/n)").lower()
        if choice == "y":
            try:
                todo_dict,string_count = delete_task('y')
            except TypeError:
                todo_dict = todo_dict
                string_count = "0"
            print(change_dict_json(todo_dict))
            jsonTodo_dict = json.dumps(todo_dict)
            
            with open("list.json","w") as f:
                data = f.write(jsonTodo_dict)
            with open("list.json") as f:
                data = f.read()
            todo_dict = json.loads(data)

        elif choice == "n":
            choice = input("Do you want to add any task ?\nIf no then you can see your current tasks (y/n)").lower()
            if choice == "y":
                label = input("Label: ").strip()
                if label.lower() == "exit":
                    break
                elif label.lower() == "display":
                    print(change_dict_json(todo_dict))
                    continue
                task = input("Task: ").strip()
                if task.lower() == "exit":
                    break
                elif task.lower() == "display":
                    print(change_dict_json(todo_dict))
                    continue
                status = input("Status: ").strip()
                if status.lower() == "exit":
                    break
                elif status.lower() == "display":
                    print(change_dict_json(todo_dict))
                    continue
                if label not in todo_dict:
                    count = 0
                    todo_dict.update({label:{str(count):[task,status]}})
                    count +=1
                
                else:
                    count = int(string_count)
                    if count != 0:
                        
                        if check_through_taskes(count,task,label,status):
                            todo_dict[label].update({str(count-1):[task,status]})
                            
                        else:
                            todo_dict[label].update({str(count):[task,status]})
                            count+=1
                            
                    else:
                        if str(count) not in todo_dict[label]:
                            todo_dict[label].update({str(count):[task,status]})
                        elif task in todo_dict[label][str(count)]:
                            todo_dict[label].update({str(count):[task,status]})
                            count+=1
                        else:
                            count+=1
                            todo_dict[label].update({str(count):[task,status]})
            elif choice == "n":
                print(change_dict_json(todo_dict))
                continue
            elif choice == "exit":
                break
            elif choice == "display":
                print(change_dict_json(todo_dict))
                continue
        elif choice == "exit":
            break
        elif choice == "display":
            print(change_dict_json(todo_dict))
            break        

main()
jsonTodo_dict = json.dumps(todo_dict)
with open("list.json","w") as f:
    data = f.write(jsonTodo_dict)
