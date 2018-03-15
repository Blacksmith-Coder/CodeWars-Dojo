using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Katas
{
    public static class Kata
    {
        /// <summary>
        /// Functionnal Addition
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        public static Func<double, double> Add(double n)
        {
            return x => x + n;
        }

        /// <summary>
        /// Credit Card issuer checking
        /// </summary>
        /// <param name="number"></param>
        /// <returns></returns>
        public static string getIssuer(long number)
        {
            int nl = number.ToString().Length;
            return (nl == 15 && (number.ToString().Substring(0, 2) == "34" || number.ToString().Substring(0, 2) == "37")) ? "AMEX" : 
                (number.ToString().Substring(0, 4) == "6011" && nl == 16) ? "Discover" :
                ((number.ToString().Substring(0, 2) == "51" || number.ToString().Substring(0, 2) == "52" || number.ToString().Substring(0, 2) == "53" ||
                number.ToString().Substring(0, 2) == "54" || number.ToString().Substring(0, 2) == "55") && nl == 16) ? "Mastercard" : 
                (number.ToString().Substring(0, 1) == "4" && (nl == 13 || nl == 16)) ? "VISA" : "Unknown";
        }

        
    }
}
