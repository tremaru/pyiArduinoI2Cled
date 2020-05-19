// ПРИМЕР ВЫВОДИТ СЕКУНДЫ ПРОШЕДШИЕ ПОСЛЕ СТАРТА: // * Строки со звёздочкой являются необязательными.
                                                  //
#include "../iarduino_I2C_4LED.h"                 //   Подключаем библиотеку для работы с индикатором I2C-flash.
#include <sys/timeb.h>

iarduino_I2C_4LED dispLED(0x09);                  //   Объявляем объект dispLED для работы с функциями и методами библиотеки iarduino_I2C_4LED, указывая адрес модуля на шине I2C.
                                                  //   Если объявить объект без указания адреса (iarduino_I2C_4LED dispLED;), то адрес будет найден автоматически.
struct timeb start, end;

void loop(void);

int main()
{
	delay(500);                                  // * Ждём завершение переходных процессов связанных с подачей питания.
	dispLED.begin();                             //   Инициируем работу с индикатором.
	ftime(&start);
	for(;;)
		loop();
}

void loop()
{
	ftime(&end);
	int diff = (int)(1000.0 * (end.time - start.time) + (end.millitm - start.millitm));
	//double i = diff/1000;                   		//   Получаем время в секундах с момента старта скетча в виде числа с плавающей точкой.
	//float j = 0.01;
	int sec = diff / 10;
	dispLED.print(sec);                       //   Выводим число с двумя знаками после запятой.
	delay(1);
}
