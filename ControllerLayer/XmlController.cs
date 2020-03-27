using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ModelLayer;
using System.Xml;
using System.IO;

namespace ControllerLayer
{
    public class XmlController
    {
        public string GetXMLpath()
        {
            string folderpath = Directory.GetCurrentDirectory();
            string supsptring = folderpath.Substring(0, folderpath.IndexOf("WoddenLegs") - 1);
            string spriptpath = supsptring + @"\WoddenLegs\"; //eidit to path where the xml is
            return spriptpath;
        }
        public List<Identifier> ReadIdentifierFromXml()
        {
            
            XmlDocument xdoc = new XmlDocument();
            FileStream fileStream = new FileStream(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml", FileMode.Open);
            xdoc.Load(fileStream);
            XmlNodeList list = xdoc.GetElementsByTagName("Identifier");
            List<Identifier> Lidentifier = new List<Identifier>();
            for (int i = 0; i < list.Count; i++)
            {
                
                XmlElement cl = (XmlElement)xdoc.GetElementsByTagName("Identifier")[i];
                XmlElement IDF = (XmlElement)xdoc.GetElementsByTagName("name")[i];
                XmlNodeList paths = (XmlNodeList)xdoc.GetElementsByTagName("path");
                XmlElement type = (XmlElement)xdoc.GetElementsByTagName("type")[i];
                XmlElement occurences = (XmlElement)xdoc.GetElementsByTagName("Occurences")[i];

                if ((cl.GetAttribute("id")) != null)
                {
                    //map into class
                    
                    Identifier idf = new Identifier();
                    idf.Id = int.Parse(cl.GetAttribute("id"));
                    for (int x = 0; x < paths.Count; x++)
                    {
                        string s = paths[x].InnerText;
                        idf.Paths.Add(s); 
                    }
                    idf.Occurences = int.Parse(occurences.InnerText);
                    idf.Type = type.InnerText;
                    idf.identifier = IDF.InnerText;
                    Lidentifier.Add(idf); //add class to a list
                }
            }
            fileStream.Close();
            return Lidentifier;
            // return list of map objects
        }

        public  void InsertblackList()
        {
            XmlDocument xd = new XmlDocument();
            FileStream lfile = new FileStream(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml", FileMode.Open);
            xd.Load(lfile);
            XmlElement cl = xd.CreateElement("blacklistType");
            XmlElement blkw = xd.CreateElement("blacklistKeyword");
            //make one for each Attribute from the class
            XmlElement email = xd.CreateElement("email");
            XmlElement number = xd.CreateElement("number");
            XmlElement ip = xd.CreateElement("ip");
            
            //what's in the corresponding attribute 
            XmlText emailtext = xd.CreateTextNode("false");
            XmlText numbertext = xd.CreateTextNode("false");
            XmlText iptext = xd.CreateTextNode("false");
            email.AppendChild(emailtext);
            number.AppendChild(numbertext);
            ip.AppendChild(iptext);
            cl.AppendChild(email);
            cl.AppendChild(number);
            cl.AppendChild(ip);
            xd.DocumentElement.AppendChild(cl); //adds the class to the xmldoc
            xd.DocumentElement.AppendChild(blkw);
            lfile.Close(); //closes the data steam
            xd.Save(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml"); //saves the work
        }

        public void UpdataBlaclistType(bool email, bool number, bool ip)
        {
            XmlDocument xdoc = new XmlDocument(); //makes a XmlDocument class
            FileStream up = new FileStream(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml", FileMode.Open); //makes to steam of data out of an exsiting xml doc
            xdoc.Load(up); // uses the class to load the data steam
            XmlElement bemail = (XmlElement)xdoc.GetElementsByTagName("email")[0]; //finds email node takes the first 
            XmlElement bNumber = (XmlElement)xdoc.GetElementsByTagName("number")[0];//findes number node takes the first
            XmlElement bip = (XmlElement)xdoc.GetElementsByTagName("ip")[0]; //findes ip node takes the first
            
            if (bemail.InnerText != email.ToString()) //checks if it allrady stands what there supose to
            {
                bemail.InnerText =  email.ToString(); //edit the text in the xml doc
            }

            if (bNumber.InnerText != number.ToString()) //checks if it allrady stands what there supose to
            {
                bNumber.InnerText = number.ToString(); //edit the text in the xml doc
            }

            if(bip.InnerText != ip.ToString()) //checks if it allrady stands what there supose to
            {
                bip.InnerText = ip.ToString(); //edit the text in the xml doc
            }

            up.Close(); // closes the data steam
            xdoc.Save(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml"); // save the chenges
        }

        public void insertBlacklistKeyword( string keywaord)
        {
            XmlDocument xd = new XmlDocument();
            FileStream lfile = new FileStream(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml", FileMode.Open);
            xd.Load(lfile);
            XmlElement cl = (XmlElement)xd.GetElementsByTagName("blacklistKeyword")[0];
            XmlElement keyword = xd.CreateElement("keyword");
            XmlText keywordtext = xd.CreateTextNode(keywaord);
            keyword.AppendChild(keywordtext);
            cl.AppendChild(keyword);
            lfile.Close();
            xd.Save(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml");
        }
    
        public void DeleteformXML(string keyword)
        {
            FileStream rfile = new FileStream(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml", FileMode.Open); //makes data steam from and existing xml doc
            XmlDocument tdoc = new XmlDocument(); // makes an xmldoc class 
            tdoc.Load(rfile); //uses the data steam with the xmldoc class
            XmlNodeList list = tdoc.GetElementsByTagName("keyword"); //makes a list of the node  
            XmlElement Blkw = (XmlElement)tdoc.GetElementsByTagName("blacklistKeyword")[0];
            for (int i = 0; i < list.Count; i++)
            {
                XmlElement cl = (XmlElement)tdoc.GetElementsByTagName("keyword")[i]; // gets the elements we have arivde at
                if (cl.InnerText== keyword) //finds checks if the element we have arived is the one we wanna delete
                {
                    Blkw.RemoveChild(cl); // delete the element
                }
            }
            rfile.Close(); // closes the data steam
            tdoc.Save(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml"); //saved the changes
        }

        public List<string> getkeywords()
        {
            FileStream rfile = new FileStream(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml", FileMode.Open); //makes data steam from and existing xml doc
            XmlDocument tdoc = new XmlDocument(); // makes an xmldoc class 
            tdoc.Load(rfile); //uses the data steam with the xmldoc class
            List<string> keywords = new List<string>();
            XmlNodeList list = tdoc.GetElementsByTagName("keyword");
            for (int i = 0; i < list.Count; i++)
            {
                XmlElement words = (XmlElement)tdoc.GetElementsByTagName("keyword")[i];
                string s = words.InnerText;
                keywords.Add(s);
            }
            return keywords;
        }
    }
}
