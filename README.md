# Tư vấn đáp án đúng cho các câu hỏi livestream Confetti
## Mô tả
* Khi trương trình đưa ra câu hỏi thì chụp màn hình góc chứa câu hỏi dùng pytesseract quét ảnh
lấy ra text. Sau đó tách chuỗi, search google api để tìm đám án và đưa ra tư vấn. Sử dụng multi thread python
để đảm bảo tốc độ
![tesst](https://user-images.githubusercontent.com/36092539/94245629-bbb0b300-ff44-11ea-871d-c83808b494fc.jpg)
* Sử dụng Firebase Realtime để đưa kết quả lên fronend:
![cap](https://user-images.githubusercontent.com/36092539/94246701-48a83c00-ff46-11ea-9f8b-eb1615c4b3bb.jpg)
## Các bước cài đặt
1: Cài đặt tesseract-ocr
```bash
sudo apt-get install tesseract-ocr
```
2: Cài đặt ngôn ngữ tiếng việt
* Tại link https://github.com/tesseract-ocr/tessdata tải file ngôn ngữ tiếng việt 'vie.traineddata'
* Sử dụng lệnh sau để tìm thư mục tesearact đã cài:
 sudo find / -type d -name tessdata
```bash
sudo find / -type d -name tessdata
```

* Sao chép file 'vie.traineddata' vào thư mục cài đặt:
```bash
cp vie.traineddata /usr/share/tesseract-ocr/4.00/tessdata
```
* Cài các thư viện khác của python 
```bash
pip install -r requirements.txt
```
* Chạy files py_ocr.py thu được kết quả tử ảnh, dùng api goole search tìm kết quả và gửi lên firebase