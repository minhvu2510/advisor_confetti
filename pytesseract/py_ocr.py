# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
 
def image_to_text():

	# Đọc file ảnh và chuyển về ảnh xám
	image = cv2.imread('tesst.jpg')
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(gray, 0, 255,
						 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	# gray = cv2.medianBlur(gray, 3)
	# Check xem có sử dụng tiền xử lý ảnh không
	# Nếu phân tách đen trắng
	# if args["preprocess"] == "thresh":
	# 	gray = cv2.threshold(gray, 0, 255,
	# 						 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	#
	# # Nếu làm mờ ảnh
	# elif args["preprocess"] == "blur":
	# 	gray = cv2.medianBlur(gray, 3)

	# Ghi tạm ảnh xuống ổ cứng để sau đó apply OCR
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# Load ảnh và apply nhận dạng bằng Tesseract OCR
	text = pytesseract.image_to_string(Image.open(filename), lang='vie')

	# Xóa ảnh tạm sau khi nhận dạng
	os.remove(filename)

	# In dòng chữ nhận dạng được
	print(text)
	return text

# Hiển thị các ảnh chúng ta đã xử lý.
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)

# Đợi chúng ta gõ phím bất kỳ
# cv2.waitKey(0)
if __name__ == '__main__':
    image_to_text()
