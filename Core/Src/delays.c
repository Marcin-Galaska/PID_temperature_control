#include "main.h"
#include "stm32f7xx_hal.h"
#include "main.h"
#include "delays.h"

extern TIM_HandleTypeDef htim1;

void Delay_us(uint16_t us)
{
	htim1.Instance->CNT = 0;
	while(htim1.Instance->CNT <= us);
}
