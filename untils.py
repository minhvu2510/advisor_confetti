from settings import *

def check_answer_notdetach(string):
    if any(ext.lower() in string.lower() for ext in NAME_PROD):
        return True
    return False
def chech_answer_detach(string):
    if any(ext.lower() in string.lower() for ext in NAME_PERSON):
        return True
    return False

def get_key_replace_negative_question(string):
    for i in NEGATIVE_REPLACE:
        if (i.lower() in string.lower()):
            return i
    else:
        return ''
def get_key_replace_question_common(string):
    for i in KEY_REPLACE:
        if (i.lower() in string.lower()):
            return i
    else:
        return ''
def check_name_product(string):
    if any(ext.lower() in string.lower() for ext in NAME_PROD):
        return True
    return False
# ------------------------------ check appear ----------------
def check_all_appear(answer,string_origin):
    answer = answer.strip().lower()
    string_origin = string_origin.lower().replace('\n', '')
    if ((answer in string_origin)):
        return True
    # new_an = ''
    if ('-' in answer):
        new_an = answer.replace('-', '')
        if (new_an in string_origin):
            return True
def check_appear_8(answer, string_origin):
    answer = answer.strip()
    list_words = answer.split(' ')
    string_origin = string_origin.lower().replace('\n','')
    if (len(list_words) >= 7):
        # if answer in string_origin:
        #     return True
        if len(list_words) > 8:
            for i in range(0, len(list_words) - 7):
                graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2] + ' ' + list_words[i + 3] + ' ' + list_words[i + 4] + ' ' + list_words[i + 5] + ' ' + list_words[i + 6] + ' ' + list_words[i + 7]
                if graft.lower() in string_origin:
                    return True
def check_appear_7(answer, string_origin):
    answer = answer.strip()
    list_words = answer.split(' ')
    string_origin = string_origin.lower().replace('\n','')
    if (len(list_words) >= 6):
        # if answer in string_origin:
        #     return True
        if len(list_words) > 7:
            for i in range(0, len(list_words) - 6):
                graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2] + ' ' + list_words[i + 3] + ' ' + list_words[i + 4] + ' ' + list_words[i + 5] + ' ' + list_words[i + 6]
                if graft.lower() in string_origin:
                    return True
def check_appear_6(answer, string_origin):
    answer = answer.strip()
    list_words = answer.split(' ')
    string_origin = string_origin.lower().replace('\n','')
    if (len(list_words) >= 5):
        # if answer in string_origin:
        #     return True
        if len(list_words) > 6:
            for i in range(0, len(list_words) - 5):
                graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2] + ' ' + list_words[i + 3] + ' ' + list_words[i + 4] + ' ' + list_words[i + 5]
                if graft.lower() in string_origin:
                    return True
def check_appear_5(answer, string_origin):
    answer = answer.strip()
    list_words = answer.split(' ')
    string_origin = string_origin.lower().replace('\n','')
    if (len(list_words) >= 4):
        # if answer in string_origin:
        #     return True
        if len(list_words) > 5:
            for i in range(0, len(list_words) - 4):
                graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2] + ' ' + list_words[i + 3] + ' ' + list_words[i + 4]
                if graft.lower() in string_origin:
                    return True
    return False
def check_appear_4(answer,string_origin):
    answer = answer.strip().lower()
    list_words = answer.split(' ')
    string_origin = string_origin.lower().replace('\n','')
    if (len(list_words) >= 4):
        for i in range(0, len(list_words) - 3):
            graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2] + ' ' + list_words[i + 3]
            if graft.lower() in string_origin:
                # print(graft)
                # print('(((((', graft)
                return True
    return False
def check_appear_3(answer,string_origin):
    answer = answer.strip().lower()
    list_words = answer.split(' ')
    string_origin = string_origin.lower().replace('\n', '')
    if len(list_words) >= 3:
        for i in range(0, len(list_words) - 2):
            graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2]
            if graft.lower() in string_origin:
                return True
def check_upper(origin_string):
    k = origin_string.split()
    del k[0]
    for i in k:
        if (i[:1].isupper() == False):
            return False
    return True
def check_appear_2_upper(answer,string_origin):
    list_words = answer.split(' ')
    if len(list_words) > 2:
        for i in range(0, len(list_words) - 1):
            graft = list_words[i] + ' ' + list_words[i + 1]
            if (graft in string_origin) and (check_upper(graft)):
                return True
def check_appear_detach(answer,string_origin):
    answer = answer.strip()
    list_words = answer.split(' ')
    answer = answer.lower()
    string_origin = string_origin.lower().replace('\n','')
    if (len(list_words) > 4):
        if answer in string_origin:
            return True
        if len(list_words) > 4:
            for i in range(0, len(list_words) - 3):
                graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2] + ' ' + list_words[i + 3]
                if graft.lower() in string_origin:
                    return True
        if len(list_words) > 3:
            for i in range(0, len(list_words) - 2):
                graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2]
                if graft.lower() in string_origin:
                    return True
    if (len(list_words) > 2):
        if answer in string_origin:
            return True
        if len(list_words) > 3:
            for i in range(0, len(list_words) - 2):
                graft = list_words[i] + ' ' + list_words[i + 1] + ' ' + list_words[i + 2]
                if graft.lower() in string_origin:
                    # print(string_origin)
                    return True
        if len(list_words) > 2:
            for i in range(0, len(list_words) - 1):
                graft = list_words[i] + ' ' + list_words[i + 1]
                if graft.lower() in string_origin:
                    # print(string_origin)
                    return True
    else:
        if len(list_words) == 1:
            string_origin = string_origin.split()
            new_an = ''
            if ('-' in answer):
                new_an = answer.replace('-', '')
            if (new_an != ''):
                if ((answer in string_origin) or (new_an in string_origin)):
                    return True
        if answer in string_origin:
            return True
        if (len(list_words) == 2):
            if allow(list_words[1]):
                if ((list_words[0].lower() in string_origin) or (list_words[1].lower() in string_origin)):
                    return True
    return False
def allow (str):
    return str[0].isupper()