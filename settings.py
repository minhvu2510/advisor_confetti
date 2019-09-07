#! coding: utf-8
# pylint: disable-msg=W0311
# diễn viên nào

QUEUE = '127.0.0.1:16382:0'
REDIS_MASTER = '127.0.0.1'
# detach
NAME_PERSON = ['ai', 'cầu thủ bóng đá nào', 'sông nào', 'cây gì', 'hoa gì', 'bánh', 'đạo diễn']
# not detach
NAME_PROD = ['tác phẩm', 'bài hát', 'bài thơ', 'bản nhạc', 'câu chuyện',
             'thực vật', 'quốc gia', 'đất nước', 'Địa danh','loài vật', 'thứ mấy',
             'nước nào', 'Bộ phim', 'tiểu bang', 'ca khúc ', 'món ăn', 'nhân vật', 'năm nào','Hình ảnh nào','tên là gì',
             'tranh nào', 'bao nhiêu', 'tỉnh nào']

NEGATIVE_REPLACE = ['nào sau đây', 'Đâu']
KEY_REPLACE = ['nào sau đây', 'Đâu', 'nào', 'là gì', 'bao nhiêu', 'gì', 'thứ mấy', 'quốc gia nào']
KEY_REPLACE2 = ['nào sau đây', 'Đâu', 'nào', 'là gì']

CHECK_NUMBER = [{1:'một', 2:'hai', 3:'ba', 4:'bốn',5:'năm',6:'sáu',7: 'bẩy', 8: 'tám', 9: 'chín', 10: 'mười'}]