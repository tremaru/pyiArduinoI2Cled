# distutils: language = c++
# cython: language_level = 3

from iarduino_I2C_4LED cimport iarduino_I2C_4LED
#from time import sleep

DEF_CHIP_ID_FLASH =  0x3C
DEF_CHIP_ID_METRO =  0xC3

# Адреса регистров модуля:
REG_FLAGS_0          =  0x00
REG_BITS_0           =  0x01
REG_FLAGS_1          =  0x02
REG_BITS_1           =  0x03
REG_MODEL            =  0x04
REG_VERSION          =  0x05
REG_ADDRESS          =  0x06
REG_CHIP_ID          =  0x07
REG_SHT_PERIOD       =  0x08
REG_SHT_FLG          =  0x10
REG_SHT_TEM_L        =  0x11
REG_SHT_HUM_L        =  0x13
REG_SHT_TEM_CHANGE   =  0x15
REG_SHT_HUM_CHANGE   =  0x16
# Позиция битов и флагов:
SHT_TEM_NEGATIVE     =  0x80
SHT_FLG_CHANGED_HUM  =  0x04
SHT_FLG_CHANGED_TEM  =  0x02
SHT_FLG_CHANGED      =  0x01

NO_BEGIN = 1

cdef class pyiArduinoI2Cled:
    cdef iarduino_I2C_4LED c_module

    def __cinit__(self, address=None, auto=None):

        if address is not None:

            self.c_module = iarduino_I2C_4LED(address)

            if auto is None:
                #sleep(.5)
                if not self.c_module.begin():

                    print("ошибка инициализации модуля.\n"
                          "Проверьте подключение и адрес модуля,"
                          " возможно не включен интерфейс I2C.\n"
                          " Запустите raspi-config и включите интерфейс"
                          ", инструкция по включению:"
                          " https://wiki.iarduino.ru/page/raspberry-i2c-spi/")

        else:

            self.c_module = iarduino_I2C_4LED()

            if auto is None:
                #sleep(.5)
                if not self.c_module.begin():

                    print("ошибка инициализации модуля.\n"
                          "Проверьте подключение и адрес модуля, "
                          " возможно не включен интерфейс I2C.\n"
                          " Запустите raspi-config и включите интерфейс"
                          ", инструкция по включению:"
                          " https://wiki.iarduino.ru/page/raspberry-i2c-spi/")

    def begin(self):
        return self.c_module.begin()

    def changeAddress(self, unsigned char newAddr):
        return self.c_module.changeAddress(newAddr)

    def reset(self):
        return self.c_module.reset()

    def getAddress(self):
        return self.c_module.getAddress()

    def getVersion(self):
        return self.c_module.getVersion()

    def getPullI2C(self):
        return self.c_module.getPullI2C()

    def setPullI2C(self, flag = True):
        if flag is not True:
                return self.c_module.setPullI2C(flag)
        else:
                return self.c_module.setPullI2C(True)

    def scheme(var):
        self.c_module.scheme(var)

    def fps(freq):
        self.c_module.fps(freq)

    def light(level):
        self.c_module.light(level)

    def turn(flg):
        self.c_module.turn(flg)

    def clear():
        self.c_module.clear()

    def point(pos, flg):
        self.c_module.point(pos, flg)

    def blink(pos, flg):
        self.c_module.blink(pos, flg)

    def frequ(f):
        self.c_module.frequ(f)

    def setLED(a, b, c, d, e):
        self.c_module.setLED(a, b, c, d, e)

    def print(
