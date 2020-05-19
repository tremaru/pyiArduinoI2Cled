DEPS=../itoa.cpp ../WString.cpp ../dtostrf.cpp
all: FindDevices NewAddress

FindDevices             :FindDevices.cpp ../iarduino_I2C_4LED.cpp
NewAddress              :NewAddress.cpp ../iarduino_I2C_4LED.cpp $(DEPS)

clean:
	rm -f FindDevices NewAddress
