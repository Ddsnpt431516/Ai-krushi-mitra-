
import json

def handle_message(message):
    # Dummy handler
    return f"धन्यवाद! आपल्या AI कृषी मित्राकडून सूचना लवकरच मिळतील. ({message})"

if __name__ == "__main__":
    msg = input("आपला प्रश्न: ")
    print(handle_message(msg))
