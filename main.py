# სავარჯიშო N1

raw_username = "  Super_coder_2026  "

username = raw_username.strip().lower().replace("_" , "-")

lenght = len(raw_username)
upper_case_start = username.startswith("super")
dash_count = username.count("-")
only_valid_char = username.replace("-", "").isalnum()

print("მომხმარებლის სახელი: ", username)
print("სიგრძე: " , lenght)
print("იწყება super-ით: ", upper_case_start)
print("ტირეების რაოდენობა: ", dash_count)
print("მხოლოდ ასოები და ციფრები: ", only_valid_char)


#სავარჯიშო N2

card = "4111222233334444"
phone = "599123456"

clean_card = card.replace(" ", "").replace("-", "")
numb_count = len(clean_card)

first_four = clean_card[:4]
last_four = clean_card[-4:]

hidden_card = "**** **** **** " + last_four
rotated_card = clean_card[:: -1]

clean_phone = phone.replace(" ", "")
changed_phone = phone[:3] + " " + phone[3:5] + " " + phone [5:7] + " " + phone [7:]

print("დამალული:", hidden_card)
print("პირველი 4 ციფრი:", first_four)
print("ციფრების რაოდენობა:", numb_count)
print("შებრუნებული:", rotated_card)
print("ტელეფონი:", changed_phone)


