import json

with open("list.json") as f:
    data = f.read()

todoDict = json.loads(data)

c = 0
def check_through_taskes(c,task,label,status):
    for i in range(c):
        
        if task == todoDict[label][str(i)][0] and status != todoDict[label][str(i)][1]:
            return True
        else:
            return False

def delete_task(choice):
    t = False
    s = False
    mc = False
    mlbl = False
    sc = False
    if choice == "y":
        ask_label = input("Label:").strip()
        if ask_label in todoDict:
            ask_task = input("Task:").strip()
            for i in todoDict[ask_label].keys():
                
                if ask_task in todoDict[ask_label][i]:
                    sc = i
                    t = todoDict[ask_label][i][0]
                    s =  todoDict[ask_label][i][1]
                    
                    break
                else:
                    continue
                    
        else:
            print("Label not found")
            return False
    if t and s and sc:
        
        del todoDict[ask_label][sc][0]
        del todoDict[ask_label][sc][0]
    if mc and sc:
        del todoDict[ask_label][sc]
    if mlbl:
        del todoDict[ask_label]
    
    if todoDict[ask_label][sc] == []:
        del todoDict[ask_label][sc]
    if todoDict[ask_label] == {}:
        del todoDict[ask_label]
    return todoDict


def main():
    global todoDict
    while True:
        print("To exit type exit")
        print("To display type display")
        print("To update your task you need to exit or display")
        choice = input("Do you want to delete any task ? (y/n)").lower()
        if choice == "y":
            print(((((((json.dumps(delete_task('y'),indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",",""))
            jsonTodoDict = json.dumps(todoDict)
            
            with open("list.json","w") as f:
                data = f.write(jsonTodoDict)
            with open("list.json") as f:
                data = f.read()
            todoDict = json.loads(data)

        elif choice == "n":
            choice = input("Do you want to add any task ?\nIf no then you can see your current tasks (y/n)").lower()
            if choice == "y":
                
                print("To exit type exit")
                print("To display type display")
                label = input("Label: ").strip()
                if label.lower() == "exit":
                    break
                elif label.lower() == "display":
                    print(((((((json.dumps(todoDict,indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",",""))
                    continue
                task = input("Task: ").strip()
                if task.lower() == "exit":
                    break
                elif task.lower() == "display":
                    print(((((((json.dumps(todoDict,indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",",""))
                    continue
                status = input("Status: ").strip()
                if status.lower() == "exit":
                    break
                elif status.lower() == "display":
                    print(((((((json.dumps(todoDict,indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",",""))
                    continue
                if label not in todoDict:
                    c = 0
                    todoDict.update({label:{str(c):[task,status]}})
                    c+=1
                
                else:
                    
                    if c != 0:
                        
                        if check_through_taskes(c,task,label,status):
                            todoDict[label].update({str(c-1):[task,status]})
                            
                        else:
                            todoDict[label].update({str(c):[task,status]})
                            c+=1
                            
                    else:
                        if task in todoDict[label][str(c)]:
                            todoDict[label].update({str(c):[task,status]})
                            c+=1
                        else:
                            c+=1
                            todoDict[label].update({str(c):[task,status]})
            elif choice == "n":
                print(((((((json.dumps(todoDict,indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",",""))
                continue
            elif choice == "exit":
                break
            elif choice == "display":
                print(((((((json.dumps(todoDict,indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",",""))
                continue
        elif choice == "exit":
            break
        elif choice == "display":
            print(((((((json.dumps(todoDict,indent=3)).replace("{","")).replace("}",""))).replace("[","")).replace("]","")).replace(",",""))
            break        

main()
jsonTodoDict = json.dumps(todoDict)
with open("list.json","w") as f:
    data = f.write(jsonTodoDict)
