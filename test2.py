import pywhatkit

pywhatkit.sendwhatmsg(
    '+601139394022', #no ws yang kita nak hantar
    'woi dapat tak mesej ni', #mesej nak dihantar ke nombor 
    20, #jam dalam 24 hour format
    5, #minute 
    10, #10 saat akan digunakan untuk buka ws
    True, #untuk close ws lepas dah guna
    3, #saat untuk close browser
)