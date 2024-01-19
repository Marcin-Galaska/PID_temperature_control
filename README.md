# PID_temperature_control
 An STM32 project that implements a PID controller to a ceramic resistor-based circuit.

### Features
- Real time PID regulation

- Target and read temperature logging, using UART

- Target temperature setting, using UART

- Target and read temperature displaying, using an 16-port LCD screen

- < 1% regulation error

### Electric Circuit Schematics
Resistor and transistor:

![Połączenie Tranzystor-Rezystor](https://github.com/Marcin-Galaska/PID_temperature_control/assets/106023363/c4984108-d29c-4166-a8a3-2999f4355500)

BMP280 sensor:

![Połączenie Czujnik-Nucleo](https://github.com/Marcin-Galaska/PID_temperature_control/assets/106023363/585cf4a2-14ea-4c97-a6ae-648ac4c54fd5)

LCD display:

![Połączenie LCD-Nucleo](https://github.com/Marcin-Galaska/PID_temperature_control/assets/106023363/aff3e248-3b35-49a5-8988-09b063617d05)
