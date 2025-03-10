class RailFenceCipher:
    def __init__(self):
        pass

    def railfence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def railfence_decrypt(self, cipher_text, num_rails):
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Xác định số ký tự trên từng đường ray
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Tạo danh sách đường ray chứa ký tự
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start+length]))  # Chuyển thành list để dễ cập nhật
            start += length

        # Giải mã bằng cách tái tạo thứ tự ký tự ban đầu
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0)  # Lấy ký tự đầu tiên của mỗi rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text

# Kiểm tra chương trình
cipher = RailFenceCipher()
text = "HELLO WORLD"
num_rails = 3

encrypted = cipher.railfence_encrypt(text, num_rails)
print("Encrypted:", encrypted)

decrypted = cipher.railfence_decrypt(encrypted, num_rails)
print("Decrypted:", decrypted)
