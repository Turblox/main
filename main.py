def on_button_pressed_a():
    basic.pause(1000)
    while True:
        if Kitronik_Move_Motor.measure() <= 13:
            Kitronik_Move_Motor.stop()
            basic.pause(500)
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE, randint(10, 45))
            basic.pause(400)
            Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.LEFT, randint(10, 50))
            basic.pause(randint(100, 250))
            Kitronik_Move_Motor.stop()
        else:
            Kitronik_Move_Motor.motor_balance(Kitronik_Move_Motor.SpinDirections.RIGHT, 2)
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 45)
input.on_button_pressed(Button.A, on_button_pressed_a)



def on_button_pressed_b():
    basic.pause(1000)
    while True:
        basic.show_number(Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT))
        basic.pause(100)

        
input.on_button_pressed(Button.B, on_button_pressed_b)

moveMotorZIP: Kitronik_Move_Motor.MoveMotorZIP = None
while input.button_is_pressed(Button.B) == False and input.button_is_pressed(Button.A) == False:
    moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
    moveMotorZIP.set_zip_led_color(0,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.set_zip_led_color(1,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.set_zip_led_color(2,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.set_zip_led_color(3,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.show()
moveMotorZIP.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.ORANGE))
moveMotorZIP.show()
basic.pause(1000)
moveMotorZIP.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.GREEN))
moveMotorZIP.show()
basic.pause(500)
moveMotorZIP.set_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLACK))
moveMotorZIP.show()