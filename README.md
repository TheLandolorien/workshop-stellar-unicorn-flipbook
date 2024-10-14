# Stellar Unicorn Flipbook Workshop

This is the setup and steps for the workshop run at SEA-Tech High School in Castle Hayne, NC on October 14, 2024 by Lando Toothman.

## :zap: Quick Start

> See [Pimoroni's Getting started with Raspberry Pi Pico Guide](https://learn.pimoroni.com/article/getting-started-with-pico) for a more detailed walkthrough for connecting Thonny to Raspberry Pi Pico.

Ensure the [Thonny IDE](https://thonny.org/) is installed.

Open Thonny and select the **"MicroPython (Raspberry Pi Pico)"** device from the menu in the bottom right corner.

![Thonny Device Selection](.github/assets/thonny_device-selection.jpg)

In the Thonny menu, make sure **View > Files** is selected so that the device files are visible.

![Thonny View Files Option](.github/assets/thonny_view-files-menu-option.jpg)

Double-click the [`main.py`](./main.py) file to open it in the Thonny file editor. Press the green play button to run the file on the Stellar Unicorn.

Press the green play button (or press the F5 key).

![Thonny Run Script Button](.github/assets/thonny_run-script-button.jpg)

Your Stellar Unicorn will start flashing 4 colorful LEDs.

<img src=".github/assets/stellar-unicorn_main.gif" width="250" height="250" alt="Stellar Unicorn Main Flashing"/>

Behind each LED is a button labeled A, B, C, or D.

<img src=".github/assets/stellar-unicorn_buttons.png" width="250" height="250" alt="Stellar Unicorn Main Flashing"/>

Press one of these buttons to start an example display:

| Button | Effect        | Description                                                                      |
| ------ | ------------- | -------------------------------------------------------------------------------- |
| A      | Fire          | An animation of a burning fire                                                   |
| B      | Supercomputer | An animation of yellow dots that look like a old-computer processing a request   |
| C      | Rainbow       | An animation of a flowing rainbow                                                |
| D      | Today's Date  | If connected to Wi-Fi a display of the day of the week and the date of the month |

Pressing **C** will display a flowing rainbow :rainbow:.

<img src=".github/assets/stellar-unicorn_rainbow-effect.gif" width="250" height="250" alt="Stellar Unicorn Rainbow Effect"/>

And ta-da! You're ready to start coding a Stellar Unicorn! :tada:

## :movie_camera: Creating a Flipbook

TBD