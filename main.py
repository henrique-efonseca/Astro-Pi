# Astro Pi Mission Space Lab
# Theme: Life on Earth
# Team: cos(π) - Coding of Space


# Libraries
from sense_hat import SenseHat
from ephem import readtle
from picamera import PiCamera
from gpiozero import CPUTemperature
from time import sleep
from pisense import SenseHAT, array
from colorzero import Color
import logging
from logzero import setup_logger, logger
import os
import datetime
import threading

# Raspberry Pi tools
sh = SenseHat()
hat = SenseHAT()
cam = PiCamera()

# Latest TLE data for ISS location
name = "ISS (ZARYA)"
l1 = "1 25544U 98067A   18327.76881777  .00002477  00000-0  44843-4 0  9999"
l2 = "2 25544  51.6406 303.4674 0005305  77.2314 344.6784 15.54011739143334"
iss = readtle(name, l1, l2)

# Datetime variable to store the start time
start_time = datetime.datetime.now()
# Datetime variable to store the current time
now_time = datetime.datetime.now()

# Sets working directory and names the log files
dir_path = os.path.dirname(os.path.realpath(__file__))

setup_logger('log1', dir_path + '/data01.csv')
setup_logger('log2', dir_path + '/data02.csv')
logger_1 = logging.getLogger('log1')
logger_2 = logging.getLogger('log2')


def security():
    """
    Function to get data from the environment on the ISS and compare it to
    the referenced values. This is used to check if anyone is near
    the AstroPi and to set colors and messages on the Sense Hat
    depending on Human Presence.
    """

    global start_time, now_time
    temperature = round(sh.get_temperature(), 2)
    humidity = round(sh.get_humidity(), 2)
    pressure = round(sh.get_pressure() * 100, 2)

    black = (0, 0, 0)
    white = (255, 255, 255)

    r = Color('red')
    g = Color('green')

    red_line = [r, r, r, r, r, r, r, r]
    green_line = [g, g, g, g, g, g, g, g]

    red_screen = array(red_line * 8)
    green_screen = array(green_line * 8)

    message = "Temperature: " + \
        str(temperature) + " Humidity: " + \
        str(humidity) + " Pressure : " + str(pressure)

    while now_time < start_time + datetime.timedelta(minutes=174):

        if temperature < 18.3 or temperature > 26.7:
            hat.screen.fade_to(red_screen)
            sleep(3)
            sh.show_message("Please step aside from the AstroPi!",
                            text_colour=white, back_colour=black, scroll_speed=0.04)
            # Update the current time
            now_time = datetime.datetime.now()

        elif humidity < 55 or humidity > 65:
            hat.screen.fade_to(red_screen)
            sleep(3)
            sh.show_message("Please step aside from the AstroPi!",
                            text_colour=white, back_colour=black, scroll_speed=0.04)
            # Update the current time
            now_time = datetime.datetime.now()

        elif pressure < 97900 or pressure > 102700:
            hat.screen.fade_to(red_screen)
            sleep(3)
            sh.show_message("Please step aside from the AstroPi!",
                            text_colour=white, back_colour=black, scroll_speed=0.04)
            # Update the current time
            now_time = datetime.datetime.now()

        else:
            hat.screen.fade_to(green_screen)
            sleep(5)
            sh.show_message(message, scroll_speed=0.07)
            # Update the current time
            now_time = datetime.datetime.now()


def get_Lat_Lon():
    """
    Function to get the latitude and longitude values
    from the 'ephem' library and write them to EXIF data for the
    photographys.
    """

    global start_time, now_time

    while now_time < start_time + datetime.timedelta(minutes=174):

        iss.compute()
        long_value = [float(i) for i in str(iss.sublong).split(":")]

        if long_value[0] < 0:
            long_value[0] = abs(long_value[0])
            cam.exif_tags['GPS.GPSLongitudeRef'] = "W"
            # Update the current time
            now_time = datetime.datetime.now()

        else:
            cam.exif_tags['GPS.GPSLongitudeRef'] = "E"
            # Update the current time
            now_time = datetime.datetime.now()

        cam.exif_tags['GPS.GPSLongitude'] = '%d/1,%d/1,%d/10' % (
            long_value[0], long_value[1], long_value[2] * 10)

        lat_value = [float(i) for i in str(iss.sublat).split(":")]

        if lat_value[0] < 0:
            lat_value[0] = abs(lat_value[0])
            cam.exif_tags['GPS.GPSLatitudeRef'] = "S"
            # Update the current time
            now_time = datetime.datetime.now()
        else:
            cam.exif_tags['GPS.GPSLatitudeRef'] = "N"
            # Update the current time
            now_time = datetime.datetime.now()

        cam.exif_tags['GPS.GPSLatitude'] = '%d/1,%d/1,%d/10' % (
            lat_value[0], lat_value[1], lat_value[2] * 10)

        return(str(lat_value), str(long_value))


def photography():
    """
    Function to take photographs every 5 seconds
    """

    global start_time, now_time
    # Variable to name the photographys
    photo_counter = 1

    while now_time < start_time + datetime.timedelta(minutes=174):

        cam.resolution = (1296, 972)
        cam.capture(dir_path + '/photo_' +
                    str(photo_counter).zfill(4) + '.jpg')
        photo_counter += 1
        sleep(5)
        # Update the current time
        now_time = datetime.datetime.now()


def data():
    """
    Function to read the data gathered by the Raspberry Pi and store it in designated log file
    """

    global start_time, now_time

    while now_time < start_time + datetime.timedelta(minutes=174):

        lat, lon = get_Lat_Lon()
        cpu = CPUTemperature()
        temperature = round(sh.get_temperature(), 2)
        humidity = round(sh.get_humidity(), 2)
        pressure = round(sh.get_pressure() * 100, 2)

        logger_1.info("Temperature: {}ºC; Humidity: {}%; Pressure: {}Pa; CPU_Temperature: {:.2f}ºC".format(
            temperature, humidity, pressure, cpu.temperature))
        logger_2.info(" Latitude: {}; Longitude: {}".format(lat, lon))

        sleep(5)
        # Update the current time
        now_time = datetime.datetime.now()


def MainFunction():
    """
    Function to run all the other functions in a multi-threading procedure
    """

    try:
        t1 = threading.Thread(target=security)
        t2 = threading.Thread(target=get_Lat_Lon)
        t3 = threading.Thread(target=photography)
        t4 = threading.Thread(target=data)

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

    except Exception as e:
        logger.error("An error occurred: " + str(e))


MainFunction()
