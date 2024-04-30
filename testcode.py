import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

buzzer_pin = 18
button_pin = 26
sound_pin = 24

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

def ButtonInput():
    try:
        while True:
            # check if button pressed
            if(GPIO.input(button_pin) == 0):
                lcd.message('ON')
                # set buzzer on
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(buzzer_pin, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(buzzer_pin, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(buzzer_pin, GPIO.HIGH)
            else:
                lcd.message('OFF')
                # it's not pressed, set button off
                GPIO.output(buzzer_pin, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()
        lcd.clear()
        lcd.set_backlight(1)

def SoundInput():
    try:
        while True:
            # check if sound detected or not
            if(GPIO.input(sound_pin)==GPIO.LOW):
                print('Sound Detected')
                time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        lcd.clear()
        lcd.set_backlight(1)


userinput = input("sound or button").lower

if userinput == "button":
    ButtonInput()
elif userinput == sound:
    SoundInput()
else:
    print("error")
