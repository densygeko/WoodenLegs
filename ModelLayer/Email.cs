using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModelLayer
{
    public class Email 
    {
        public int id { get; set; }
        public string path { get ; set ; }
        public string identifier { get ; set ; }
        public int gane_fundet { get ; set ; }

        public Email(int id, string path, string identifier, int id_rawdata)
        {
            this.id = id;
            this.path = path;
            this.identifier = identifier;
            this.gane_fundet = id_rawdata;
        }
    }
}
