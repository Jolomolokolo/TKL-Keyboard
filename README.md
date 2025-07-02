# TKL Keyboard – Custom Tenkeyless Mechanical Keyboard with Integrated RP2040

This project is a custom-designed TKL (Tenkeyless) mechanical keyboard with an ISO DE/QWERTZ layout. It features a fully hand-routed PCB with an onboard RP2040 microcontroller, integrated flash memory, reset and boot buttons, and support for hot-swap sockets.

---

## Project Overview

### Keyboard Overview  
This is an overview of the complete TKL keyboard project, including schematic, PCB, and case layout:

![Keyboard Overview](images/CASE-Complete.png)

---

### Schematic  
The keyboard uses a row-column matrix with diodes to prevent ghosting. The RP2040 is directly mounted on the PCB along with a crystal, power regulation, ESD protection, and SPI flash for firmware storage.

![Schematic](images/schematics.png)

---

### PCB Layout  
The PCB is fully hand-routed and includes:

- RP2040 with external flash memory  
- USB-C port for programming and power  
- Boot and reset buttons  
- Crystal oscillator  
- Fuse for protection  
- Support for hot-swap switch sockets  
- ISO DE/QWERTZ-compliant layout  

![PCB Layout](images/pcb.png)

---

### Case & Assembly  
The case uses standoffs, heated inserts, and screws to mount the PCB securely. Cutout for USB-C.
Compatible with standard MX keycaps and Cherry stabilizers.

![Case Bottom with space for heated inserts](images/case-bottom.png)
![Case](images/case-top.png)

---

## Bill of Materials (BOM)

| Qty | Component              | Value / Description                          | Footprint / Type                      |
|-----|------------------------|----------------------------------------------|---------------------------------------|
| 8   | Capacitor              | 100n                                         | C_0402                                |
| 5   | Capacitor              | 1u                                           | C_0402                                |
| 2   | Capacitor              | 22p                                          | C_0402                                |
| 1   | Capacitor              | 10u                                          | C_0603                                |
| 5   | Resistor               | 5.1k                                         | R_0402                                |
| 2   | Resistor               | 27k                                          | R_0402                                |
| 2   | Resistor               | 1k                                           | R_0402                                |
| 88  | Diodes                 | 1N4148 or equivalent (Ghosting Prevention)   | SOD-123                               |
| 1   | Microcontroller        | RP2040                                       | QFN-56                                |
| 1   | Voltage Regulator      | XC6206PxxxMR                                 | SOT-23-3                              |
| 1   | ESD Protection         | SRV05-4                                      | SOT-23-6                              |
| 1   | Flash Memory           | W25Q128JVS                                   | SOIC-8                                |
| 1   | Crystal                | 12MHz / GND24                                | SMD 3225-4Pin                         |
| 1   | Fuse                   | For USB protection                           | 1206                                  |
| 2   | Push Button            | Reset / Boot                                 | TL3342                                |
| 88  | Hot-swap Sockets       | MX-compatible                                | CPG151101S11                          |
| 4   | Stabilizers            | 6.25u / 2.75u / 2u / ISO                     | Cherry MX                             |
| 1   | USB Port               | USB-C 2.0                                    | 16P Receptacle                        |
| 1   | Debug Header           | 4-pin JST                                    | JST-SH 1.0mm                          |
| 1   | Debug Header           | 5-pin Header                                 | 2.54mm Vertical                       |
| 88  | Switches               | Cherry MX or clone                           | MX-compatible                         |
| 88  | Keycaps                | ISO DE Layout                                | Cherry Profile                        |
| 6   | Standoffs              | 6×6mm M2.5                                   | Female-Male                           |
| 6   | Screws                 | M2.5×6mm                                     | Steel                                 |
| 6   | Heated Inserts         | M2.5×6mm                                     | Brass                                 |
| 1   | USB Cable              | USB-A to USB-C                               | —                                     |

---

## Firmware

The firmware is based on [KMK Firmware](https://github.com/KMKfw/kmk_firmware), a powerful Python-based keyboard firmware running on CircuitPython.

- Full matrix mapping (ISO DE layout)  
- Boot/reset control  
- Flash via USB, no external programmer required

Configuration is managed via `code.py` and `keymap.py`.

- Multi Layer Keyboard will be added!

---

## Future Improvements
 
- Add rotary encoder or OLED display  
- Bluetooth support (via BLE module)  
- Add underglow LED layer

---

## License

This project is open-source under the MIT License.
