
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
            string spriptpath = supsptring + @"\WoddenLegs\"; //edit to path where the xml is
            return spriptpath;
        }
        public List<Identifier> ReadIdentifierFromXml()
        {
            try //try cath for when the ui load and a xml file hasn't have created it till gets a still returns a list
            {
                XmlDocument xdoc = new XmlDocument();
                FileStream fileStream = new FileStream(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml", FileMode.Open);
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
            catch (System.IO.FileNotFoundException e) // retruns a empty list for the ui to show
            {
                 List < Identifier > nulllist = new List<Identifier>();
                return nulllist;
            }


        }

        public void InsertblackList()
        {
            XmlDocument xd = new XmlDocument();
            FileStream lfile = new FileStream(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml", FileMode.Open);
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
            xd.Save(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml"); //saves the work
        }

        public void UpdataBlaclistType(bool email, bool number, bool ip)
        {
            XmlDocument xdoc = new XmlDocument(); //makes a XmlDocument class
            FileStream up = new FileStream(GetXMLpath() + @"Main2\dist\Matchedldentifiers.xml", FileMode.Open); //makes to steam of data out of an exsiting xml doc
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
            xdoc.Save(GetXMLpath() + @"Main2\dist\Matchedldentifiers.xml"); // save the chenges
        }

         
        public void InsertBlacklistKeyword(string insertKeyword)
        {
            XmlDocument xd = new XmlDocument(); //Makes an instance of a Xmldocclass 
            FileStream lfile = new FileStream(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml", FileMode.Open); //open steam of data out of an exsiting xml doc
            xd.Load(lfile);
            XmlElement cl = (XmlElement)xd.GetElementsByTagName("blacklistKeyword")[0]; //findes the note BlacklistKeyword in the xml doc
            XmlElement keyword = xd.CreateElement("keyword"); //makes an new element named keyword
            XmlText keywordtext = xd.CreateTextNode(insertKeyword); // put the string into the insertkeyword
            keyword.AppendChild(keywordtext); //put the keywordtext under the keyword node
            cl.AppendChild(keyword); //add the keyword to blacklistkeyword node
            lfile.Close(); //closes the stean of data
            xd.Save(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml"); //saves the changes
        } 

        public void DeleteBlacklistKeyword(string deleteKeyword)
        {
            FileStream rfile = new FileStream(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml", FileMode.Open); //makes data steam from and existing xml doc
            XmlDocument tdoc = new XmlDocument(); // makes an xmldoc class 
            tdoc.Load(rfile); //uses the data steam with the xmldoc class
            XmlNodeList list = tdoc.GetElementsByTagName("keyword"); //makes a list of the node  
            XmlElement Blkw = (XmlElement)tdoc.GetElementsByTagName("blacklistKeyword")[0];
            for (int i = 0; i < list.Count; i++)
            {
                XmlElement cl = (XmlElement)tdoc.GetElementsByTagName("keyword")[i]; // gets the elements we have arivde at
                if (cl.InnerText == deleteKeyword) //finds checks if the element we have arived is the one we wanna delete
                {
                    Blkw.RemoveChild(cl); // delete the element
                }
            }
            rfile.Close(); // closes the data steam
            tdoc.Save(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml"); //saved the changes
        }

        public List<string> GetBlacklistkeywords()
        {
            FileStream rfile = new FileStream(GetXMLpath() + @"Main2\dist\MatchedIdentifiers.xml", FileMode.Open); //makes data steam from and existing xml doc
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

        public void MakeXmlfile()
        {
            XmlTextWriter xwriter = new XmlTextWriter(GetXMLpath() + "/filepaths.xml", Encoding.UTF8); //makes an instanst of a writter there can make xml data, with a path to where you want the xml file and an encoding type
            xwriter.Formatting = Formatting.Indented; //Mkaes the fomatting readable for humans
            xwriter.WriteStartElement("paths"); //adds the element paths to xml doc
            xwriter.WriteEndElement(); //ends the paths element
            
            
            xwriter.Close(); //closes the steam of data
        }

        public void Insertpathtoxmldoc()
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
