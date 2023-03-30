import time
import machine
import utime
from utime import localtime
from breakout_bme280 import BreakoutBME280
from pimoroni_i2c import PimoroniI2C
from pimoroni import PICO_EXPLORER_I2C_PINS
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
from pimoroni import Button
import random
import sys

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
i2c = PimoroniI2C(**PICO_EXPLORER_I2C_PINS)
bme = BreakoutBME280(i2c, address=0x76)
button_x = Button(14)
button_a = Button(12)
button_b = Button(13)
button_y = Button(15)

import network
import time
#from time import localtime
from umqtt.simple import MQTTClient

import utime
from utime import localtime
dateTimeObj = localtime()


    
def time_1():
    Dyear, Dmonth, Dday, Dhour, Dmin, Dsec, Dweekday, Dyearday = (dateTimeObj)
    Ddateandtime = "{}/{}/{}"
    timex = Ddateandtime.format(Dday, Dmonth, Dyear)
    return timex

def time_2():
    Dyear, Dmonth, Dday, Dhour, Dmin, Dsec, Dweekday, Dyearday = (dateTimeObj)
    Ddateandtime_2 = "{00}:{00}"
    timey = Ddateandtime_2.format(Dhour, Dmin)
    return timey
        

mqtt_server = 'broker.mqttdashboard.com'
client_id = 'bigles'

TEMPCOLOUR = display.create_pen(0, 0, 0)  # this colour will get changed in a bit
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
RED = display.create_pen(255, 0, 0)
GREY = display.create_pen(150, 170, 170)
BLUE = display.create_pen(0, 0, 255)
GREEN = display.create_pen(0, 255, 0)
LIGHTBLUE = display.create_pen(137, 207, 240)
YELLOW = display.create_pen(255, 255, 0)

temperature, pressure, humidity = bme.read()

def describe_temperature(temperature):
    global TEMPCOLOUR
    if temperature < 10:
        description = "very cold"
        display.set_pen(BLUE)
    elif 10 <= temperature < 15:
        description = "cold"
        display.set_pen(LIGHTBLUE)
    elif 15 <= temperature < 20:
        description = "bit chilly"
        display.set_pen(GREEN)
    elif 20 <= temperature < 26:
        description = "warm"
        display.set_pen(YELLOW)
    elif temperature >= 26:
        description = "very warm / hot"
        display.set_pen(RED)
    else:
        description = ""
        TEMPCOLOUR = display.create_pen(0, 0, 0)
    return description

def describe_pressure(pressure):
    if pressure < 970:
        description = "storm"
        display.set_pen(RED)
    elif 970 <= pressure < 990:
        description = "rain"
        display.set_pen(LIGHTBLUE)
    elif 990 <= pressure < 1010:
        description = "change"
        display.set_pen(YELLOW)
    elif 1010 <= pressure < 1030:
        description = "fair"
        display.set_pen(GREEN)
    elif pressure >= 1030:
        description = "dry"
        display.set_pen(GREY)
    else:
        description = ""
    return description

def describe_humidity(humidity):
    if 30 < humidity < 50:
        description = "good"
        display.set_pen(GREEN)
    else:
        description = "bad"
        display.set_pen(RED)
    return description

    
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("AirTrafficControlTower","ny00000m")
#if wlan.connect == True:
 #   print('wlan.isconnected()')
  #  time.sleep(3)
#else:
 #   print('wlan is not connected')
  #  time.sleep(3)

#mqtt_server = 'eu1.cloud.thethings.network:8883'
#client_id = 'clientId-MHAN0dMVMC'
#username = 'cheribim-app@ttn'
#password = 'NNSXS.PJ3XCNSTVNASIOQJD77SKYFVO2Y7TMSD6ULH34Q.EONU7BWNI4QHLAEAEMBRRESOXSZTDNHDKJILFQXQP4O2XC2HZ3SA'
mqtt_server = 'broker.mqttdashboard.com'
client_id = 'bigles'

#def mqtt_connect():
   # client = MQTTClient(client_id, mqtt_server, keepalive=3600)
   # client.connect()
    #print('Connected to %s MQTT Broker'%(mqtt_server))
    #return client

#def reconnect():
    #print('Failed to connect to the MQTT Broker. Reconnecting...')
    #time.sleep(5)
    #machine.reset()
    
while True:
    
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    display.text("Working on it!", 10, 170, 240, 3)
        
    display.set_pen(BLACK)
    display.clear()

    temperature, pressure, humidity = bme.read()
    revised_pressure = pressure/100
    
    display.set_pen(WHITE)
    display.text("temperature:", 10, 10, 240, 3)
    """aassedisplay.set_pen(TEMPCOLOUR)"""
    display.text('{:.1f}'.format(temperature) + ' °' + 'C', 10, 30, 240, 5)
    display.set_pen(RED)
    display.text(describe_temperature(temperature), 10, 60, 240, 3)

    display.set_pen(WHITE)
    display.text("pressure:", 10, 90, 240, 3)
    display.text('{:.0f}'.format(revised_pressure) + ' ' + 'hPa', 10, 110, 240, 5)
    display.set_pen(RED)
    display.text(describe_pressure(revised_pressure), 10, 140, 240, 3)

    display.set_pen(WHITE)
    display.text("humidity:", 10, 170, 240, 3)
    display.text('{:.0f}'.format(humidity) + '' + '%', 10, 190, 240, 5)
    display.set_pen(RED)
    display.text(describe_humidity(humidity), 10, 220, 240, 3)

    rand = random.randint(1, 1)
    
     #if rand == 1: 
        
        #topic_pub_1 = b'Temp'
        #topic_pub_2 = b'Humidity'
        #topic_pub_3 = b'Pressure'
            
            
    temperature, pressure, humidity = bme.read()
            
            
    topic_msg_1 = str('temperature:' + ' ' + '{:.1f}'.format(temperature) + ' ' + 'C')
    topic_msg_2 = str('humidity:' + ' ' + '{:.0f}'.format(humidity) + ' ' + '%')
    topic_msg_3 = str('pressure:' + ' ' + '{:.0f}'.format(revised_pressure) + ' ' + 'hPa')
            
        #try:
            #client = mqtt_connect()
        
        # except OSError as e:
            # reconnect()

        #client.publish(topic_pub_1, topic_msg_1)
        #client.publish(topic_pub_2, topic_msg_2)
        #client.publish(topic_pub_3, topic_msg_3)
            
    #print(topic_msg_1, topic_msg_2, topic_msg_3)
    time.update()   
    display.update()
    
    time.sleep(1)
    
    if button_x.read():
        
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        temperature, pressure, humidity = bme.read()
        display.text(str(time_1()), 10, 10, 240, 4)
        display.text(str(time_2()), 10, 50, 240, 4)
        display.text('{:.0f}'.format(pressure) + ' ' + 'hPa', 10, 80, 240, 4)
        display.text('{:.0f}'.format(temperature) + 'C', 10, 110, 240, 4)
        display.text('{:.0f}'.format(humidity) + '%', 10, 140, 240, 4)
        display.update()
        time.sleep(5)
        display.set_pen(BLACK)
        display.clear()
        display.update()
    
    elif button_a.read():
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.text('button a test', 10, 10, 240, 4)
        display.update()
        time.sleep(5)
        display.set_pen(BLACK)
        display.clear()
        display.update()
        
    elif button_b.read():
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.text('button b test', 10, 10, 240, 4)
        display.update()
        time.sleep(5)
        display.set_pen(BLACK)
        display.clear()
        display.update()
    
    elif button_y.read():
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.text('button y test', 10, 10, 240, 4)
        display.update()
        time.sleep(5)
        display.set_pen(BLACK)
        display.clear()
        display.update()
        
    else:
        pass
