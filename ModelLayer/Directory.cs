using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModelLayer
{
    //this class is made for beeing able to tell if the class has been read or not
    //this class is named with a small d ebcause system.IO namespace has a class called Directory
    public class directory
    {
        //this string is path to the directory
        public string path { set; get; }
        //this boolea are to tell if this class has been read or not
        public bool read { set; get; }
        //this is a construtre of the class you would allways be needing a path to directory
        public directory(string path)
        {
            this.path = path;
            read = false;
        }
    }
}
