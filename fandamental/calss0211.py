

is_office_close = bool(int(input("Is office close 0/1 : ")))
has_special_event = bool(int(input("Is any special event 0/1 : ")))

getup_early_status = (is_office_close and has_special_event) or not is_office_close
print("Your getup status : ", getup_early_status)