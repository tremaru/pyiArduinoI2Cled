DEPS=../iarduino_I2C_4LED.cpp ../itoa.cpp ../WString.cpp ../dtostrf.cpp
all: FindDevices NewAddress ShowOptions ShowTime ShowMillis

FindDevices             :FindDevices.cpp $(DEPS)
NewAddress              :NewAddress.cpp $(DEPS)
ShowOptions             :ShowOptions.cpp $(DEPS)
ShowTime                :ShowTime.cpp $(DEPS)
ShowMillis              :ShowMillis.cpp $(DEPS)

clean:
	rm -f FindDevices NewAddress ShowOptions ShowTime ShowMillis
