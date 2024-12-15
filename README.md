A espresso machine can't be that complicated, can it?

# AIM
replacing the board of a Delonghi Dedica EC685 with a Raspberry pico.

# TRAIN-OF-THOUGHT
- The GAGGUINO project designed for GAGGIA CLASSIC is a project that makes the espresso machine smart by adding some sensors and controllers. 
- A Dedica is not so different from a GAGGIA CLASSIC: it uses the same pump and uses a simalair heating method.
- An espresso machine in its core is quite simple, such as a Flair. Water needs to heat to a certain point and the pump needs to be powered.
- The heating block and the pump are both 230v.
- Arduino and Pico are designed to control switches and read sensors.
- I need a challenge for in this afwull winter time.
- Being able to add extra sensors and controllers (such as an AC dimmer), enables for more espresso profiling.
- Thinkering with stuff is huge fun.

# CHECKLIST
- [x] Reading the temprature with the termoster 
- [x] Turning the heating block on and off
- [x] PID temprature control
- [ ] Turning the pump on and off
- [ ] Pump power control (AC dimmer)
- [ ] Reading the flow sensor
- [ ] Implement the steam wand
- [x] Read the front buttons and control the LEDs