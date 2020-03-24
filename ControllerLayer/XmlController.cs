using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
using System.IO;

namespace ControllerLayer
{
    class XmlController
    {
        public void readxml()
        {
            // do this for each tag
            XmlDocument xdoc = new XmlDocument();
            FileStream fileStream = new FileStream(@"path", FileMode.Open);
            xdoc.Load(fileStream);
            XmlNodeList list = xdoc.GetElementsByTagName("sometag");
            for (int i = 0; i < list.Count; i++)
            {
                //add more if there is more nunder tags
                XmlElement cl = (XmlElement)xdoc.GetElementsByTagName("sometagsundertag")[i];
                XmlElement add = (XmlElement)xdoc.GetElementsByTagName("anothertagundertag")[i];
                if ((cl.GetAttribute("id")) != null)
                {
                    //map into class
                    //add class to a list
                }
            }
            fileStream.Close();
            // return list of map objects
        }

        public  void insertinto(Object aClass)
        {
            XmlDocument xd = new XmlDocument();
            FileStream lfile = new FileStream(@"path", FileMode.Open);
            xd.Load(lfile);
            XmlElement cl = xd.CreateElement(aClass.GetType().ToString());
            cl.SetAttribute("id", "id to string");
            //make one for each Attribute from the class
            XmlElement na = xd.CreateElement("Address");
            //what's in the corresponding attribute 
            XmlText natext = xd.CreateTextNode("what is in the attribute");
            na.AppendChild(natext); //add the text tot the arrtibute
            cl.AppendChild(na); //adds the arrtibute to the class
            xd.DocumentElement.AppendChild(cl); //adds the class to the xmldoc
            lfile.Close(); //closes the data steam
            xd.Save(@"path"); //saves the work
        }

        public void updataXML()
        {
            XmlDocument xdoc = new XmlDocument(); //makes a XmlDocument class
            FileStream up = new FileStream(@"path", FileMode.Open); //makes to steam of data out of an exsiting xml doc
            xdoc.Load(up); // uses the class to load the data steam
            XmlNodeList list = xdoc.GetElementsByTagName("Customer"); //makes a list of an node in the xml doc
            for (int i = 0; i < list.Count; i++) //itarades tho  the list
            {
                XmlElement cu = (XmlElement)xdoc.GetElementsByTagName("Customer")[i]; //finds the node we have arrvied at
                XmlElement add = (XmlElement)xdoc.GetElementsByTagName("Address")[i]; // need to make a get like this for each under attribute
                if (cu.GetAttribute("Name") == "abc") // finding the right one
                {
                    cu.SetAttribute("Name", "efgh"); // make eidts 
                    add.InnerText = "pqrs,india"; // make eidts
                    break; // braks the loop
                }
            }
            up.Close(); // closes the data steam
            xdoc.Save(@"path"); // save the chenges
        }
    
        public void deleteformXML()
        {
            FileStream rfile = new FileStream(@"path", FileMode.Open); //makes data steam from and existing xml doc
            XmlDocument tdoc = new XmlDocument(); // makes an xmldoc class 
            tdoc.Load(rfile); //uses the data steam with the xmldoc class
            XmlNodeList list = tdoc.GetElementsByTagName("Customer"); //makes a list of the node  
            for (int i = 0; i < list.Count; i++)
            {
                XmlElement cl = (XmlElement)tdoc.GetElementsByTagName("Customer")[i]; // gets the elements we have arivde at
                if (cl.GetAttribute("Name") == "efgh") //finds checks if the element we have arived is the one we wanna delete
                {
                    tdoc.DocumentElement.RemoveChild(cl); // delete the element
                }
            }
            rfile.Close(); // closes the data steam
            tdoc.Save(@"path"); //saved the changes
        }
    }
}
