import sys
from PIL import Image
import os

def encode_image(image_path, message):
    try:
        # Kiểm tra file tồn tại
        if not os.path.exists(image_path):
            print("Lỗi: Không tìm thấy file ảnh!")
            return False
            
        # Mở ảnh
        img = Image.open(image_path)
        
        # Chuyển ảnh sang RGB nếu cần
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        width, height = img.size
        total_pixels = width * height
        max_message_length = (total_pixels * 3) // 8 - 1  # Trừ 1 byte cho ký tự kết thúc
        
        # Kiểm tra độ dài thông điệp
        if len(message) > max_message_length:
            print(f"Lỗi: Thông điệp quá dài! Độ dài tối đa là {max_message_length} ký tự")
            return False
            
        # Chuyển đổi thông điệp thành nhị phân
        binary_message = ''.join([format(ord(char), '08b') for char in message])
        binary_message += '11111111'  # Đánh dấu kết thúc thông điệp
        
        # Tạo bản sao của ảnh để không ảnh hưởng đến ảnh gốc
        encoded_img = img.copy()
        data_index = 0
        
        # Mã hóa thông điệp vào ảnh
        for row in range(height):
            for col in range(width):
                pixel = list(encoded_img.getpixel((col, row)))
                
                for color_channel in range(3):
                    if data_index < len(binary_message):
                        # Thay đổi bit cuối cùng của mỗi kênh màu
                        pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                        data_index += 1
                        
                encoded_img.putpixel((col, row), tuple(pixel))
                
                if data_index >= len(binary_message):
                    break
                    
            if data_index >= len(binary_message):
                break
                
        # Lưu ảnh đã mã hóa
        output_path = 'encoded_image.png'
        encoded_img.save(output_path)
        print(f"Mã hóa thành công! Ảnh đã được lưu tại: {output_path}")
        return True
        
    except Exception as e:
        print(f"Lỗi: {str(e)}")
        return False

def main():
    if len(sys.argv) != 3:
        print("Cách sử dụng: python encrypt.py <đường_dẫn_ảnh> <nội_dung_cần_ẩn>")
        print("Ví dụ: python encrypt.py test.jpg 'Xin chào thế giới'")
        return
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    
    encode_image(image_path, message)

if __name__ == "__main__":
    main()

