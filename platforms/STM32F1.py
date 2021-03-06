from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="STM32F1"
    ROM_OFF=0x08000000 
    RAM_OFF=0x20000000
    IRQ=MCU.IRQ+ [
        "NVIC_WWDG_IRQ",
        "NVIC_PVD_IRQ",
        "NVIC_TAMPER_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_FLASH_IRQ",
        "NVIC_RCC_IRQ",
        "NVIC_EXTI0_IRQ",
        "NVIC_EXTI1_IRQ",
        "NVIC_EXTI2_IRQ",
        "NVIC_EXTI3_IRQ",
        "NVIC_EXTI4_IRQ",
        "NVIC_DMA1_CHANNEL1_IRQ",
        "NVIC_DMA1_CHANNEL2_IRQ",
        "NVIC_DMA1_CHANNEL3_IRQ",
        "NVIC_DMA1_CHANNEL4_IRQ",
        "NVIC_DMA1_CHANNEL5_IRQ",
        "NVIC_DMA1_CHANNEL6_IRQ",
        "NVIC_DMA1_CHANNEL7_IRQ",
        "NVIC_ADC1_2_IRQ",
        "NVIC_USB_HP_CAN_TX_IRQ",
        "NVIC_USB_LP_CAN_RX0_IRQ",
        "NVIC_CAN_RX1_IRQ",
        "NVIC_CAN_SCE_IRQ",
        "NVIC_EXTI9_5_IRQ",
        "NVIC_TIM1_BRK_IRQ",
        "NVIC_TIM1_UP_IRQ",
        "NVIC_TIM1_TRG_COM_IRQ",
        "NVIC_TIM1_CC_IRQ",
        "NVIC_TIM2_IRQ",
        "NVIC_TIM3_IRQ",
        "NVIC_TIM4_IRQ",
        "NVIC_I2C1_EV_IRQ",
        "NVIC_I2C1_ER_IRQ",
        "NVIC_I2C2_EV_IRQ",
        "NVIC_I2C2_ER_IRQ",
        "NVIC_SPI1_IRQ",
        "NVIC_SPI2_IRQ",
        "NVIC_USART1_IRQ",
        "NVIC_USART2_IRQ",
        "NVIC_USART3_IRQ",
        "NVIC_EXTI15_10_IRQ",
        "NVIC_RTC_ALARM_IRQ",
        "NVIC_USB_WAKEUP_IRQ",
        "NVIC_TIM8_BRK_IRQ",
        "NVIC_TIM8_UP_IRQ",
        "NVIC_TIM8_TRG_COM_IRQ",
        "NVIC_TIM8_CC_IRQ",
        "NVIC_ADC3_IRQ",
        "NVIC_FSMC_IRQ",
        "NVIC_SDIO_IRQ",
        "NVIC_TIM5_IRQ",
        "NVIC_SPI3_IRQ",
        "NVIC_UART4_IRQ",
        "NVIC_UART5_IRQ",
        "NVIC_TIM6_IRQ",
        "NVIC_TIM7_IRQ",
        "NVIC_DMA2_CHANNEL1_IRQ",
        "NVIC_DMA2_CHANNEL2_IRQ",
        "NVIC_DMA2_CHANNEL3_IRQ",
        "NVIC_DMA2_CHANNEL4_5_IRQ",
        "NVIC_DMA2_CHANNEL5_IRQ",
        "NVIC_ETH_IRQ",
        "NVIC_ETH_WKUP_IRQ",
        "NVIC_CAN2_TX_IRQ",
        "NVIC_CAN2_RX0_IRQ",
        "NVIC_CAN2_RX1_IRQ",
        "NVIC_CAN2_SCE_IRQ",
        "NVIC_OTG_FS_IRQ",
        ]
