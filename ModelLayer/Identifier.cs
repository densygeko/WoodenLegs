using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModelLayer
{
    public class Identifier
    {
        public int Id { set; get; }
        public string Type { set; get; }
        public List<string> Paths { set; get; }
        public int Occurences { set; get; }
        public string identifier { set; get; }
       
        public Identifier()
        {
            this.Paths = new List<string>();
            this.Type = "";
            this.identifier = "";
        }
    }
}
