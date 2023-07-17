def on_logo_pressed():
    basic.show_string("H=" + str(Math.round(Math.map(pins.analog_read_pin(AnalogPin.P10), 0, 1023, 0, 100))) + "%")
    Nivel_humedad(Math.round(Math.map(pins.analog_read_pin(AnalogPin.P10), 0, 1023, 0, 100)))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def Temperatura(Temp: number):
    return Temp * 60 / 1023

def on_button_pressed_a():
    basic.show_string("Temp=" + str(Math.round(Temperatura(pins.analog_read_pin(AnalogPin.P0)))) + ".C")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("L=" + str(Math.round(Math.map(pins.analog_read_pin(AnalogPin.P1), 0, 1023, 0, 100))) + "%")
input.on_button_pressed(Button.B, on_button_pressed_b)

def Nivel_humedad(Hum: number):
    if Hum <= 40:
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    elif Hum <= 80:
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        basic.show_leds("""
            # . . . #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    basic.pause(1000)
    basic.clear_screen()
basic.show_icon(IconNames.COW)
basic.pause(1000)
basic.clear_screen()
ON_OFF = False
strip = neopixel.create(DigitalPin.P9, 4, NeoPixelMode.RGB)
strip.clear()

def on_forever():
    if Temperatura(pins.analog_read_pin(AnalogPin.P0)) <= 10 or Temperatura(pins.analog_read_pin(AnalogPin.P0)) >= 28:
        basic.show_icon(IconNames.TRIANGLE)
        basic.clear_screen()
    if pins.digital_read_pin(DigitalPin.P6) == 0:
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
basic.forever(on_forever)
