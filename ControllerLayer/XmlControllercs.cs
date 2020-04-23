
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
            FileStream fileStream = new FileStream(GetXMLpath() + "text.xml", FileMode.Open);
            xdoc.Load(fileStream);
            XmlNodeList list = xdoc.GetElementsByTagName("Identifier");
            List<Identifier> Lidentifier = new List<Identifier>();
            for (int i = 0; i < list.Count; i++)
            {
                XmlElement cl = (XmlElement)xdoc.GetElementsByTagName("Identifier")[i];

                XmlElement IDF = (XmlElement)xdoc.GetElementsByTagName("name")[i];
                XmlNodeList paths = (XmlNodeList)xdoc.GetElementsByTagName("path");
                XmlElement type = (XmlElement)xdoc.GetElementsByTagName("type")[i];
                XmlElement occurences = (XmlElement)xdoc.GetElementsByTagName("occurences")[i];

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

        public void InsertblackList()
        {
            XmlDocument xd = new XmlDocument();
            FileStream lfile = new FileStream(@"C:\Users\Uth\Desktop\WoddenLegs\filepaths.xml", FileMode.Open);
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
                bemail.InnerText = email.ToString(); //edit the text in the xml doc
            }

            if (bNumber.InnerText != number.ToString()) //checks if it allrady stands what there supose to
            {
                bNumber.InnerText = number.ToString(); //edit the text in the xml doc
            }

            if (bip.InnerText != ip.ToString()) //checks if it allrady stands what there supose to
            {
                bip.InnerText = ip.ToString(); //edit the text in the xml doc
            }

            up.Close(); // closes the data steam
            xdoc.Save(@"C:\Users\Uth\Desktop\WoddenLegs\ControllerLayer\XMLFile1.xml"); // save the chenges
        }

        public void insertBlacklistKeyword(string keywaord)
        {
            XmlDocument xd = new XmlDocument();
            FileStream lfile = new FileStream(GetXMLpath() + "/filepaths.xml", FileMode.Open);
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
                if (cl.InnerText == keyword) //finds checks if the element we have arived is the one we wanna delete
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

        public void makeXmlfile()
        {
            XmlTextWriter xwriter = new XmlTextWriter(GetXMLpath() + "/filepaths.xml", Encoding.UTF8);
            xwriter.Formatting = Formatting.Indented;
            xwriter.WriteStartElement("paths");
            xwriter.WriteEndElement();
            
            
            xwriter.Close();
        }

        public void insertpathtoxmldoc()
        {
            FilesContainer files = FilesContainer.getInstance();
            XmlDocument xd = new XmlDocument();
            string path = @"C:\Users\Uth\Desktop\WoddenLegs\filepaths.xml";
            FileStream lfile = new FileStream(path, FileMode.Open);
            xd.Load(lfile);
            
            if (files.pcaps.Count > 0)
            {
                XmlElement pcaps = xd.CreateElement("pcapPaths");
                foreach (var item in files.pcaps)
                {
                    XmlElement pcap = xd.CreateElement("pcappath");
                    XmlText pcaptext = xd.CreateTextNode(item);
                    pcap.AppendChild(pcaptext);
                    pcaps.AppendChild(pcaps);
                }
                xd.DocumentElement.AppendChild(pcaps);
            }
            if (files.pdfs.Count > 0)
            {
                XmlElement pdfpaths = xd.CreateElement("pdfPaths");
                foreach (var item in files.pdfs)
                {
                    XmlElement pdfs = xd.CreateElement("pdfpath");
                    XmlText pdfstext = xd.CreateTextNode(item);
                    pdfs.AppendChild(pdfstext);
                    pdfpaths.AppendChild(pdfs);
                }
                xd.DocumentElement.AppendChild(pdfpaths);
            }
            if (files.PictureFiles.Count > 0)
            {
                XmlElement piturefiles = xd.CreateElement("piturePaths");
                foreach (var item in files.PictureFiles)
                {
                    XmlElement picturepaths = xd.CreateElement("piturePath");
                    XmlText picturepath = xd.CreateTextNode(item);
                    picturepaths.AppendChild(picturepath);
                }
                xd.DocumentElement.AppendChild(piturefiles);
            }
            if (files.xmls.Count > 0)
            {
                XmlElement xmlfiles = xd.CreateElement("xmlPaths");
                foreach (var item in files.xmls)
                {
                    XmlElement xmlpath = xd.CreateElement("xmlPaths");
                    XmlText xmltext = xd.CreateTextNode(item);
                    xmlpath.AppendChild(xmltext);
                    xmlfiles.AppendChild(xmlpath);
                }
                xd.DocumentElement.AppendChild(xmlfiles);
            }
            
            lfile.Close();
            xd.Save(path);
        }
    }
}
