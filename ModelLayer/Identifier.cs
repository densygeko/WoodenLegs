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
        
        public string Type { set; get; } //Witch type of Identifier it is (email, phoneNo or ip)
        public List<string> Paths { set; get; } //list of paths since Indentifier does Occure on less it found in two diffent files
        public int Occurences { set; get; } //how meny different
        public string identifier { set; get; } //what Identifer is
        public bool isBlacklisted { get; set; } //show if the identifier is blacklisted or not.
        public Identifier()
        {
            this.Paths = new List<string>();
            this.Type = "";
            this.identifier = "";
        }
    }
}
