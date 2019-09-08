#!/usr/bin/python
# -*- coding: utf-8 -*-
# from redis import Redis
from googleapiclient.discovery import build
import untils
import threading
from settings import *
from googletrans import Translator
translator = Translator()

# QUESTION = Redis(host=settings.REDIS_MASTER, port=int(6379), db=7)
def rate_answer(keyword):
    # my_api_key = 'AIzaSyBQGUQjol8SGcU45E8AoVC1ml2ssmjgiqc'
    # my_cse_id = "007634521947617393818:q2nm52o-9fs"
    # my_cse_id = "007634521947617393818:q2nm52o-9fs"
    #
    my_api_key = 'AIzaSyBLjpmGnVgk17r8UezfiSBDBInQgX8kNMY'
    my_cse_id = "012292668574518592803:v0yhz0lyrhi"
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res
    result = google_search(keyword, my_api_key, my_cse_id)
    try:
        list_result = result['items']
    except:
        list_result = []
    return list_result
def translate_api(string_origin):
    translations = translator.translate(string_origin,dest='en')
    # print('--origin--',string_origin)
    # print('--translate--',translations)
    return translations.text
# test ok phết
def negative_question(question, answer):
    question = question.replace('KHÔNG phải ','')
    question = question.replace('KHÔNG ','')
    question = question.replace('?','')
    key_replace = untils.get_key_replace_negative_question(question)
    if key_replace != '':
        key_search = question.replace(key_replace, answer).strip()
    else:
        key_search = question + ' ' +answer
    # print('+++++',key_search)
    result_search = rate_answer(key_search)
    global dem
    dem = 0
    for i in result_search:
        if (untils.check_appear_detach(answer,i['title']) or untils.check_appear_detach(answer,i['snippet'])):
            if untils.check_appear_5(question,i['title']) or untils.check_appear_5(question,i['snippet']):
                dem += 10
                continue
            if untils.check_appear_4(question, i['title']) or untils.check_appear_4(question, i['snippet']):
                dem += 4
                continue

            if untils.check_appear_3(question, i['title']) or untils.check_appear_3(question, i['snippet']):
                # print(i['title'], i['snippet'])
                dem += 1
                # continue
            if untils.check_appear_2_upper(question, i['title']) or untils.check_appear_2_upper(question, i['snippet']):
                # print(i['title'], i['snippet'])
                dem += 2
                continue
            dem += 0.1
    if dem < 4:
        key_search_en = translate_api(key_search)
        # print('+++', key_search_en)
        result_search_en = rate_answer(key_search_en)
        quets_en = translate_api(question)
        anw_en = translate_api(answer)
        # print('Dap an:', anw_en)
        for i in result_search_en:
            if (untils.check_appear_detach(anw_en, i['title']) or untils.check_appear_detach(anw_en, i['snippet'])):
                if untils.check_appear_5(quets_en, i['title']) or untils.check_appear_5(quets_en, i['snippet']):
                    dem += 10
                    continue
                if untils.check_appear_4(quets_en, i['title']) or untils.check_appear_4(quets_en, i['snippet']):
                    dem += 4
                    continue
                if untils.check_appear_3(quets_en, i['title']) or untils.check_appear_3(quets_en, i['snippet']):
                    dem += 1
                    # continue
                if untils.check_appear_2_upper(quets_en, i['title']) or untils.check_appear_2_upper(quets_en,
                                                                                                    i['snippet']):
                    dem += 3
                    continue
                dem += 0.1
    # print('-----------------', dem)
    re = {answer: dem}
    return re

# test tàm tạm
def quotation_mark(question, answer):
    global dem
    global dem1
    dem = 0
    def count_no_answer(keysearch):
        global dem1
        dem1 = 0
        result_search = rate_answer(keysearch)
        # print('-----', keysearch)
        for i in result_search:
            if (untils.check_appear_detach(answer, i['title']) or untils.check_appear_detach(answer, i['snippet'])):
                if untils.check_appear_5(question, i['title']) or untils.check_appear_5(question, i['snippet']):
                    dem1 += 10
                    continue
                if untils.check_appear_4(question, i['title']) or untils.check_appear_4(question, i['snippet']):
                    dem1 += 4
                    continue
                if untils.check_appear_3(question, i['title']) or untils.check_appear_3(question, i['snippet']):
                    dem1 += 1
                    # continue
                if untils.check_appear_2_upper(question, i['title']) or untils.check_appear_2_upper(question,
                                                                                                    i['snippet']):
                    dem1 += 3
                    continue
                dem1 += 0.1
        if dem1 < 4:
            keysearch_en = translate_api(keysearch)
            question_en = translate_api(question)
            answer_en = translate_api(answer)
            # print('---answer_en',answer_en)
            result_search_en = rate_answer(keysearch_en)
            for i in result_search_en:
                if (untils.check_appear_detach(answer_en, i['title']) or untils.check_appear_detach(answer_en, i['snippet'])):
                    if untils.check_appear_5(question_en, i['title']) or untils.check_appear_5(question_en, i['snippet']):
                        dem1 += 10
                        continue
                    if untils.check_appear_4(question_en, i['title']) or untils.check_appear_4(question_en, i['snippet']):
                        dem1 += 4
                        continue
                    if untils.check_appear_3(question_en, i['title']) or untils.check_appear_3(question_en, i['snippet']):
                        dem1 += 1
                        # continue
                    if untils.check_appear_2_upper(question_en, i['title']) or untils.check_appear_2_upper(question_en,
                                                                                                        i['snippet']):
                        dem1 += 3
                        continue
                    dem1 += 0.1
    def count_has_answer(keysearch):
        global dem
        dem = 0
        key_replace = untils.get_key_replace_question_common(keysearch)
        # print('====key replace:', key_replace)
        if key_replace != '':
            key_search = keysearch.replace(key_replace, answer).strip()
        else:
            key_search = keysearch + ' ' + answer
        result_search = rate_answer(key_search)
        # print('+++++++++++++', key_search)
        for i in result_search:
            if (untils.check_appear_detach(answer, i['title']) or untils.check_appear_detach(answer, i['snippet'])):
                if untils.check_appear_5(question, i['title']) or untils.check_appear_5(question, i['snippet']):
                    dem += 10
                    continue
                if untils.check_appear_4(question, i['title']) or untils.check_appear_4(question, i['snippet']):
                    # print(i['snippet'])
                    dem += 4
                    continue
                if untils.check_appear_3(question, i['title']) or untils.check_appear_3(question, i['snippet']):
                    dem += 1
                    # continue
                if untils.check_appear_2_upper(question, i['title']) or untils.check_appear_2_upper(question,
                                                                                                    i['snippet']):
                    dem += 3
                    continue
                dem += 0.1
        if dem < 4:
            key_search_en = translate_api(key_search)
            answer_en = translate_api(answer)
            # print('---answer_en', answer_en)
            question_en = translate_api(question)
            result_search_en = rate_answer(key_search_en)
            for i in result_search_en:
                if (untils.check_appear_detach(answer_en, i['title']) or untils.check_appear_detach(answer_en, i['snippet'])):
                    if untils.check_appear_5(question_en, i['title']) or untils.check_appear_5(question_en,
                                                                                               i['snippet']):
                        dem += 10
                        continue
                    if untils.check_appear_4(question_en, i['title']) or untils.check_appear_4(question_en,
                                                                                               i['snippet']):
                        dem += 4
                        continue
                    if untils.check_appear_3(question_en, i['title']) or untils.check_appear_3(question_en,
                                                                                               i['snippet']):
                        dem += 1
                        # continue
                    if untils.check_appear_2_upper(question_en, i['title']) or untils.check_appear_2_upper(question_en,
                                                                                                           i[
                                                                                                               'snippet']):
                        dem += 3
                        # print(question_en)
                        # print(i['snippet'])
                        continue
                    dem += 0.1

    if question.count('"') == 2:
        word_detach = question.split('"')
        # print(word_detach[1])
        list1 = word_detach[0].strip().split()
        list2 = word_detach[2].strip().split()
        if (len(list1) > len(list2)):
            keysearch = word_detach[0].strip() + ' "' + word_detach[1] + '"'
        else:
            keysearch = '"' + word_detach[1] + '" ' + word_detach[2].strip()
        # print(keysearch)
        x = threading.Thread(target=count_no_answer,args=(keysearch, ))
        y = threading.Thread(target=count_has_answer,args=(keysearch, ) )
        # logging.info("Main    : before running thread")
        x.start()
        y.start()
        x.join()
        y.join()
        # print('------dem', dem)
        # print('------dem11', dem1)
        re = {answer: dem + dem1}
        return re
    else:
        keysearch = question
        # print(question)
        x = threading.Thread(target=count_no_answer, args=(keysearch,))
        y = threading.Thread(target=count_has_answer, args=(keysearch,))
        # logging.info("Main    : before running thread")
        x.start()
        y.start()
        x.join()
        y.join()
        # print('------dem', dem)
        # print('------dem11', dem1)
        re = {answer: dem + dem1}
        return re

def normal_question(question, answer):
    global dem
    global dem1
    dem = 0
    if ',' in question:
        question = question.split(',')[1]
    def count_no_answer():
        global dem1
        dem1 = 0
        result_search = rate_answer(question)
        # print('-----', question)
        for i in result_search:
            if (untils.check_appear_detach(answer, i['title']) or untils.check_appear_detach(answer, i['snippet'])):
                if untils.check_appear_5(question, i['title']) or untils.check_appear_5(question, i['snippet']):
                    # print('-------------5')
                    dem1 += 10
                    continue
                if untils.check_appear_4(question, i['title']) or untils.check_appear_4(question, i['snippet']):
                    # print('-------------4')
                    dem1 += 4
                    continue
                if untils.check_appear_3(question, i['title']) or untils.check_appear_3(question, i['snippet']):
                    # print('-------------3')
                    dem1 += 1
                    # continue
                if untils.check_appear_2_upper(question, i['title']) or untils.check_appear_2_upper(question,
                                                                                                    i['snippet']):
                    # print('-------------2')
                    dem1 += 3
                    continue
                dem1 += 0.1
        if dem1 < 4:
            # print('vào----------------------------------')
            keysearch_en = translate_api(question)
            question_en = translate_api(question)
            answer_en = translate_api(answer)
            # print('---answer_en',answer_en)
            # print ('+++++', keysearch_en)
            result_search_en = rate_answer(keysearch_en)
            for i in result_search_en:
                if (untils.check_appear_detach(answer_en, i['title']) or untils.check_appear_detach(answer_en, i['snippet'])):
                    if untils.check_appear_5(question_en, i['title']) or untils.check_appear_5(question_en,
                                                                                               i['snippet']):
                        dem1 += 10
                        continue
                    if untils.check_appear_4(question_en, i['title']) or untils.check_appear_4(question_en,
                                                                                               i['snippet']):
                        dem1 += 4
                        continue
                    if untils.check_appear_3(question_en, i['title']) or untils.check_appear_3(question_en,
                                                                                               i['snippet']):
                        dem1 += 1
                        # continue

                    if untils.check_appear_2_upper(question_en, i['title']) or untils.check_appear_2_upper(question_en,
                                                                                                           i[
                                                                                                               'snippet']):
                        dem1 += 3
                        continue
                    dem1 += 0.1

    def count_has_answer():
        global dem
        dem = 0
        key_replace = untils.get_key_replace_question_common(question)
        # print('====key replace:', key_replace)
        if key_replace != '':
            # key_search = question.lower().replace(key_replace.lower(), answer).strip()
            key_search = question.replace(key_replace, answer).strip()
            # print('00000000000',key_search,answer)
        else:
            key_search = question + ' ' + answer
        result_search = rate_answer(key_search)
        # print('+++++++++++++-------', key_search)
        for i in result_search:
            if (untils.check_appear_detach(answer, i['title']) or untils.check_appear_detach(answer, i['snippet'])):
                if untils.check_appear_5(question, i['title']) or untils.check_appear_5(question, i['snippet']):
                    dem += 10
                    continue
                if untils.check_appear_4(question, i['title']) or untils.check_appear_4(question, i['snippet']):
                    # print(question)
                    # print(i['snippet'])

                    dem += 4
                    continue
                if untils.check_appear_3(question, i['title']) or untils.check_appear_3(question, i['snippet']):
                    dem += 1
                    # continue
                if untils.check_appear_2_upper(question, i['title']) or untils.check_appear_2_upper(question,
                                                                                                    i['snippet']):
                    dem += 3
                    continue
                # else:
                dem += 0.1
        if dem < 4:
            key_search_en = translate_api(key_search)
            answer_en = translate_api(answer)
            # print('---answer_en', answer_en)
            question_en = translate_api(question)
            result_search_en = rate_answer(key_search_en)
            # print ('++++',key_search_en)
            for i in result_search_en:
                if (untils.check_appear_detach(answer_en, i['title']) or untils.check_appear_detach(answer_en, i['snippet'])):
                    if untils.check_appear_5(question_en, i['title']) or untils.check_appear_5(question_en,
                                                                                               i['snippet']):
                        dem += 10
                        continue
                    if untils.check_appear_4(question_en, i['title']) or untils.check_appear_4(question_en,
                                                                                               i['snippet']):
                        dem += 4
                        continue
                    if untils.check_appear_3(question_en, i['title']) or untils.check_appear_3(question_en,
                                                                                               i['snippet']):
                        dem += 1
                        # continue
                    if untils.check_appear_2_upper(question_en, i['title']) or untils.check_appear_2_upper(question_en,
                                                                                                           i[
                                                                                                               'snippet']):
                        dem += 3
                        # print(question_en)
                        # print(i['snippet'])
                        continue
                    dem += 0.1

    x = threading.Thread(target=count_no_answer)
    y = threading.Thread(target=count_has_answer)
    # logging.info("Main    : before running thread")
    x.start()
    y.start()
    x.join()
    y.join()
    # print('------dem', dem)
    # print('------dem11', dem1)
    re = {answer: dem + dem1}
    return re
    # result_search = rate_answer(question)
    # dem = 0
    # for i in result_search:
    #     if ((untils.check_appear_pro(answer, i['title']) or untils.check_appear_pro(answer, i['snippet'])) and
    #             (untils.check_appear_how(question,i['title']) or untils.check_appear_how(question,i['snippet']))):
    #         # print('========',i['snippet'], i['title'], answer)
    #         dem += 9
    #     if (untils.check_appear_pro(answer, i['title']) or untils.check_appear_pro(answer, i['snippet'])):
    #         dem += 1
    # re = {answer: dem}
    # return re

if __name__ == '__main__':
    # quotation_mark('Vở cải lương "Tiếng trống Mê Linh" được công diễn lần đầu tiên vào năm nào?',
    #                '1976')
    # 1: Cây bách(score: 0 - 3.5)
    # 2: Cây tùng(score: 1 - 4).....
    # 3: Cây sồi(score: 0 - 3.5)
    # negative_question('Nước nào sau đây KHÔNG thuộc múi giờ GMT 3?',
    #                   'En-Xan-va-đo')
    normal_question('Con của con trâu được gọi là gì',
                      ' Con nghé')
    # question_how('Quốc gia nào sau đây nghiêm cấm du khách mang giày cao gót khi đến thăm những khu di tích cổ?','Hy Lạp')
    # question_how('Theo Telegraph, cầu thủ bóng đá nào sau đây có đai đen Taekwondo?',
    #              'Zlatan Ibrahimovic')
    #     Cô bé và sóng biển
    # negative_question('Đâu KHÔNG phải là tên gọi khác của Hồ Tây?',
    #                   'Hồ Dâm Đàm')
