import analys_detach
import _thread
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from operator import itemgetter
# Fetch the service account key JSON file contents
# cred = credentials.Certificate('mv.json')
# # Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://confetti-be3fc.firebaseio.com/'
#  })
# ref = db.reference('/minhvu')
# ref.set({ 'quest': '','ans_': 1,'ans_b': 0,'ans_c': 0,'tele': '3777777'})

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
    # if rate_a[ans_a] == 0:
    #     a1 =threading.Thread(target=get_rate_a1())
    #     a1.start()
    # if rate_b[ans_b] == 0:
    #     b1 = threading.Thread(target=get_rate_b1())
    #     b1.start()
    # if rate_c[ans_c] == 0:
    #     c1 = threading.Thread(target=get_rate_c1())
    #     c1.start()
    x.start()
    y.start()
    z.start()
    # ---------------------
    # ---------------------------
    x.join()
    y.join()
    # z.join()
    # o.join()
    # quest_a = ans_a
    # quest_b = ans_b
    # quest_c = ans_c
    # k1 = [{'key': ans_a, 'value': rate_a[ans_a]},
    #      {'key': ans_b, 'value': rate_b[ans_b]},
    #      {'key': ans_c, 'value': rate_c[ans_c]}]
    # # k2 = [rate_a[ans_a],rate_b[ans_b],rate_c[ans_c]]
    # k = max(rate_a[ans_a],rate_b[ans_b],rate_c[ans_c])
    # if (rate_a[ans_a] == k):
    #     print('----', rate_a)
    # if (rate_b[ans_b] == k):
    #     print('----', rate_b)
    # if (rate_c[ans_c] == k):
    #     print('----', rate_c)
    # maxPricedItem = max(k1, key=lambda x: x['value'])
    # max = max(map(itemgetter('value'), k1))
    # k = [rate_a, rate_b, rate_c]
    # ref.set({'quest': quest, 'ans_a': ans_a,'count_a': rate_a[ans_a],
    #          'ans_b': ans_b,'count_b': rate_b[ans_b],
    #          'ans_c': ans_c,'count_c': rate_c[ans_c],
    #          'tele': ans_or})
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