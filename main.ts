input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.pause(1000)
    while (true) {
        if (Kitronik_Move_Motor.measure() <= 13) {
            Kitronik_Move_Motor.stop()
            basic.pause(500)
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Reverse, randint(10, 45))
            basic.pause(400)
            Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.Left, randint(10, 50))
            basic.pause(randint(100, 250))
            Kitronik_Move_Motor.stop()
        } else {
            Kitronik_Move_Motor.motorBalance(Kitronik_Move_Motor.SpinDirections.Right, 2)
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 45)
        }
        
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.pause(1000)
    while (true) {
        basic.showNumber(Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Left))
        basic.pause(100)
    }
})
let moveMotorZIP : Kitronik_Move_Motor.MoveMotorZIP = null
while (input.buttonIsPressed(Button.B) == false && input.buttonIsPressed(Button.A) == false) {
    moveMotorZIP = Kitronik_Move_Motor.createMoveMotorZIPLED(4)
    moveMotorZIP.setZipLedColor(0, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
    moveMotorZIP.setZipLedColor(1, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
    moveMotorZIP.setZipLedColor(2, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
    moveMotorZIP.setZipLedColor(3, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
    moveMotorZIP.show()
}
moveMotorZIP.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Orange))
moveMotorZIP.show()
basic.pause(1000)
moveMotorZIP.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Green))
moveMotorZIP.show()
basic.pause(500)
moveMotorZIP.setColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Black))
moveMotorZIP.show()
