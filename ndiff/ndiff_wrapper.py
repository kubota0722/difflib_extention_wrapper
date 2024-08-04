import difflib

def double_line_to_double_list(base: str, edit: str):
    base_list = [] #編集元のリストを保存する
    edit_list = [] #編集後のリストを保存する

    diff = list(difflib.ndiff(base.splitlines(), edit.splitlines()))

    for i in range(0, len(diff)):
        print(diff[i])

    set_flag = "f" 

    insert_base_line = ""
    insert_edit_line = ""

    di = 0
    while di < len(diff):
        now_flag = diff[di][0] #チェックする行のdiffの種類を取得
        target_sentence = diff[di][2:]
        #print("------------")
        #print("di: ", di)
        #print("now_flag: ", now_flag)
        #print("set_flag: ", set_flag)
        #print("diff[di]: ", diff[di])
        #print("target_sentence: ", target_sentence)
        #print("base_list: ", base_list)
        #print("edit_list: ", edit_list)
        #print("insert_base_line: ", insert_base_line)
        #print("insert_edit_line: ", insert_edit_line)
        #print("------------")
        #time.sleep(2)

        # 最初の行に適用する処理 set_flag == "f"のとき
        if (set_flag == "f") and (now_flag == " "):
            insert_base_line += target_sentence + "\n"
            insert_edit_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1
        elif (set_flag == "f") and (now_flag == "+"):
            insert_base_line += " "
            insert_edit_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1
        elif (set_flag == "f") and (now_flag == "-"):
            insert_base_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1

        # set_flag == " " のとき
        elif (set_flag == " ") and (now_flag == " "):
            insert_base_line += target_sentence + "\n"
            insert_edit_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1
        elif (set_flag == " ") and (now_flag == "+"):
            insert_edit_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1
        elif (set_flag == " ") and (now_flag == "-"):
            insert_base_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1

        # set_flag == "+"のとき
        elif (set_flag == "+") and (now_flag == " "):
            base_list.append(insert_base_line)
            edit_list.append(insert_edit_line)
            insert_base_line = ""
            insert_edit_line = ""
            set_flag = now_flag
        elif (set_flag == "+") and (now_flag == "+"):
            insert_edit_line += target_sentence + "\n"
            di += 1
            set_flag = now_flag
        elif (set_flag == "+") and (now_flag == "-"):
            insert_base_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1

        # set_flag == "-"のとき
        elif (set_flag == "-") and (now_flag == " "):
            base_list.append(insert_base_line)
            edit_list.append(insert_edit_line)
            insert_base_line = ""
            insert_edit_line = ""
            set_flag = now_flag
        elif (set_flag == "-") and (now_flag == "+"):
            insert_edit_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1
        elif (set_flag == "-") and (now_flag == "-"):
            insert_base_line += target_sentence + "\n"
            set_flag = now_flag
            di += 1
        
        elif (now_flag == "?"):
            di += 1

        else:
            di += 1
    base_list.append(insert_base_line)
    edit_list.append(insert_edit_line)

    return base_list, edit_list