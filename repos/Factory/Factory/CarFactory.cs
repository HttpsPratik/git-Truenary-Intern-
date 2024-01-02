﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Factory
{
    public class CarFactory : VehicleFactory
    {
        public Vehicle CreateVehicle()
        {
            return new Car();
        }
    }
}
