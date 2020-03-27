using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModelLayer
{
    public class Email 
    {
        public int Id { get; set; }
        public string path { get ; set ; }
        public string Identifier { get ; set ; }
        public int Gane_fundet { get ; set ; }

        public Email(int id, string path, string identifier, int id_rawdata)
        {
            this.Id = id;
            this.path = path;
            this.Identifier = identifier;
            this.Gane_fundet = id_rawdata;
        }
    }
}
