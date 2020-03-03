using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModelLayer
{
    public class directory
    {
        public string path { set; get; }
        public bool read { set; get; }
        public directory(string path)
        {
            this.path = path;
            read = false;
        }
    }
}
