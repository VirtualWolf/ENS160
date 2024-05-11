# ENS160
A MicroPython library for the [ScioSense ENS160](https://www.sciosense.com/ens16x-digital-metal-oxide-multi-gas-sensor-family/) indoor air quality sensor.

Full credit for the primary code goes to [Lukasz Awsiukiewicz](https://github.com/awsiuk/ENS160/), I just tweaked it a bit for more configurability (the I2C class now needs to be passed in, a custom I2C address can be specified, and it allows custom temperature and humidity values to be used for calibration). See [example.py](example.py) for usage.

The vendor's chip documentation can be found [here](https://www.sciosense.com/wp-content/uploads/2023/12/ENS160-Datasheet.pdf).

# License

You may use this code in comercial and personal use without fee. You are free to modify it and create copy of it and make your own project. When modifying this code in your own project that is separat from this package on personal or comericial purpose just leave credit information in your code.
