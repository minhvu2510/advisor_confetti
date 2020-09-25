import analys_detach
import _thread
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from operator import itemgetter
rate_a = {}
rate_b = {}
rate_c = {}
rate_a1 = {}
rate_b1 = {}
rate_c1 = {}
answer_tele = ''
nav = 0

def get_resutl(quest,ans_a,ans_b,ans_c,ans_or):
    def get_rate_a():
        global rate_a
        global nav
        if 'KHÔNG' in quest:
            rate_a = analys_detach.negative_question(quest, ans_a)
            nav = 1
        elif '"' in quest:
            rate_a = analys_detach.quotation_mark(quest, ans_a)
        else:
            print('======================================================================')
            rate_a = analys_detach.normal_question(quest, ans_a)
    def get_rate_b():
        global rate_b
        global nav
        if 'KHÔNG' in quest:
            rate_b = analys_detach.negative_question(quest, ans_b)
        elif '"' in quest:
            rate_b = analys_detach.quotation_mark(quest,ans_b)
        else:
            rate_b = analys_detach.normal_question(quest, ans_b)
    def get_rate_c():
        global rate_c
        global nav
        if 'KHÔNG' in quest:
            rate_c = analys_detach.negative_question(quest, ans_c)
        elif '"' in quest:
            rate_c = analys_detach.quotation_mark(quest,ans_c)
            # if rate_c[ans_c] == 0:
            #     rate_c = detach_answer.quotation_mark_ans(quest, ans_c)
        else:
            rate_c = analys_detach.normal_question(quest, ans_c)
    x = threading.Thread(target=get_rate_a())
    y = threading.Thread(target=get_rate_b())
    z = threading.Thread(target=get_rate_c())
    print('----', rate_a)
    print('----', rate_b)
    print('----', rate_c)
    print('----', ans_or)
    x.start()
    y.start()
    z.start()
    # ---------------------
    # ---------------------------
    x.join()
    y.join()
    if 'KHÔNG' in quest:
        print('-----------------------------KHÔNG-------------------------------')
    # print('----', rate_a)
    # print('----', rate_b)
    # print('----', rate_c)
    # print('----', ans_or)
    # k = [rate_a, rate_b, rate_c]
    print('-------------a1', rate_a1)
    print('-------------b1', rate_b1)
    print('-------------b1', rate_c1)
    # max(node.y for node in path.nodes)