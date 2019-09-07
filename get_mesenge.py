#!/usr/bin/python
# -*- coding: utf-8 -*-
from telethon import TelegramClient, sync, events
import result1
import result2
# from redis import Redis
import settings
# import analys
# import analys_answer
# import analys_notdetach

# QUESTION = Redis(host=settings.REDIS_MASTER, port=int(6379), db=7)
#account Mv Mv
# api_id = '962770'
# api_hash = '8fe3bd79c6014766020f62fbff5d1193'

#account MinhDuy
api_id = '1010743'
api_hash = '7b61317eb3da2d67a70bddca7c89bb82'
group_username = 'vudeptrai'
import timeit
import untils
client = TelegramClient('anon3', api_id, api_hash).start()
@client.on(events.NewMessage(pattern='^#|Sh'))
async def my_event_handler(event):
    print (event.raw_text)
    start = timeit.default_timer()
    if 'Best answer' in event.raw_text:
        # print (event.raw_text, type(event.raw_text))
        line_quest = event.raw_text.split('\n')
        question = line_quest[3].split(':')[1].strip().replace('?','')
        ans_a = line_quest[5].split('(')[0].split(':')[1].strip()
        ans_b = line_quest[6].split('(')[0].split(':')[1].strip()
        ans_c = line_quest[7].split('(')[0].split(':')[1].strip()
        origin_ans = line_quest[0].split('(')[0].split(':')[1].strip()
        # analys.ana_quest(question,ans_a,ans_b,ans_c,origin_ans)
        # if (untils.check_name_person(question)):
        #     print('--------------vào 1')
        #     analys_answer.get_resutl(question, ans_a, ans_b, ans_c, origin_ans)
        if (untils.check_name_product(question)):
            print('vào --------------1')
            result1.get_resutl(question, ans_a, ans_b, ans_c, origin_ans)
        else:
            print('vào --------------2')
            result2.get_resutl(question, ans_a, ans_b, ans_c, origin_ans)
            # if (untils.check_name_person(question)):
            #     print('--------------vào 1')
                # analys_answer.get_resutl(question, ans_a, ans_b, ans_c, origin_ans)
            # else:
            #     pass
                # analys.get_resutl(question, ans_a, ans_b, ans_c, origin_ans)
        # analys.get_resutl(question, ans_a, ans_b, ans_c, origin_ans)
        # print('===',question)
        # print('===',origin_ans)
        # print('==', ans_a)
        # print('==', ans_b)
        # print('==', ans_c)
        # QUESTION.set('question',question)
        # QUESTION.set('ans_a',ans_a)
        # QUESTION.set('ans_b',ans_b)
        # QUESTION.set('ans_c',ans_c)
        # QUESTION.set('origin_ans',origin_ans)
    else:
        pass
        # QUESTION.delete('question')
        # QUESTION.delete('ans_a')
        # QUESTION.delete('ans_b')
        # QUESTION.delete('ans_c')
        # QUESTION.delete('origin_ans')
        # QUESTION.set('result', event.raw_text.replace('#',''))
        # print(event.raw_text)
    stop = timeit.default_timer()
    print('Time: ', stop - start)
@client.on(events.NewMessage(pattern='vudeptrai'))
async def check_run_ok(event):
    print('chuan cmn roi ...')
client.start()
client.run_until_disconnected()

