/**
 * Copyright (c) 2014 Xavier Mendez
 * All rights reserved.

 * This file is part of Voltrinket.
 *
 * Voltrinket is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Voltrinket is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with Voltrinket.  If not, see <http://gnu.org/licenses/>
 **/

// Must match with the receiver in order for it to accept the data
char FOOTPRINT[] = "Voltrinket 0.1.0";

// Delay between each voltage read (ms)
int delay = 400;


#include <avr/power.h>

void setup() {
  // First, set frequency to 16MHz.
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);

  //TODO
}

void loop() {
  
}
