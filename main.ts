input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("TEMP =" + ("" + Math.round(Temperatura(pins.analogReadPin(AnalogPin.P0)))) + ".C")
})
function Temperatura (Temp: number) {
    return Temp * 200 / 1023
}
input.onButtonPressed(Button.A, function () {
    basic.showString("HUM =" + ("" + Math.round(Math.map(pins.analogReadPin(AnalogPin.P10), 0, 1023, 0, 100))) + "%")
    Nivel_humedad(Math.round(Math.map(pins.analogReadPin(AnalogPin.P10), 0, 1023, 0, 100)))
})
input.onButtonPressed(Button.B, function () {
    basic.showString("LUZ =" + ("" + Math.round(Math.map(pins.analogReadPin(AnalogPin.P1), 0, 1023, 0, 100))) + "%")
})
function Nivel_humedad (Hum: number) {
    if (Hum <= 40) {
        basic.showLeds(`
            # . . . #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    } else if (Hum <= 80) {
        basic.showLeds(`
            # . . . #
            # . . . #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            # . . . #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    basic.pause(5000)
    basic.clearScreen()
}
let ON_OFF = false
basic.showIcon(IconNames.Yes)
basic.pause(1000)
basic.clearScreen()
let strip = neopixel.create(DigitalPin.P9, 4, NeoPixelMode.RGB)
strip.clear()
