using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Katas
{
    class Program
    {
        static void Main(string[] args)
        {
            Func<double, double> AddOne = Kata.Add(1);
            Trace.WriteLine(AddOne(3));
        }
    }
}
