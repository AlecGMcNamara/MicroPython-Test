from machine import Pin, PWM    # type: ignore  stop missing machine module error
from time import sleep

frequency = 5000
led = PWM(Pin(2), frequency)

while True:
  for duty_cycle in range(0, 1024, 3):
    led.duty(duty_cycle)
    sleep(0.005)
  sleep(1)
  for duty_cycle in range(1020, 0, -3):
    led.duty(duty_cycle)
    sleep(0.005)
  sleep(1)