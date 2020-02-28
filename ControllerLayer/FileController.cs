using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControllerLayer
{
    public class FileController
    {

        private List<string> pdfs = new List<string>();
        private List<string> pcaps = new List<string>();
        private List<string> billedeFiler = new List<string>();
        private List<string> xmls = new List<string>();
        private List<List<string>> fileTypes = new List<List<string>>();
        public FileController()
        {
            
            fileTypes.Add(pdfs);
            fileTypes.Add(pcaps);
            fileTypes.Add(billedeFiler);
            fileTypes.Add(xmls);
        }

        public List<List<string>> Getfiles(string path)
        {
            string[] dirs = Directory.GetDirectories(path);
            string[] fils = Directory.GetFiles(path);
            if (fils.Length > 0)
            {
                Sortfiles(fils);
                
            }
            foreach (var item in dirs)
            {
                string[] files = Directory.GetFiles(item);
                Sortfiles(files);
            }
            return fileTypes;
        }
        public void Sortfiles(string[] files)
        {
            foreach (var item in files)
            {
                string supstring = item.Substring(item.LastIndexOf(".") + 1);
                supstring.ToUpper();
                switch (supstring)
                {
                    case ".PDF":
                        pdfs.Add(item);
                        break;
                    case ".PCAP":
                        pcaps.Add(item);
                        break;
                    case ".PNG":
                        billedeFiler.Add(item);
                        break;
                    case ".XML":
                        xmls.Add(item);
                        break;
                    default:
                        break;
                }
            }
        }
        public List<List<string>> GetAllfiletypes()
        {
            return fileTypes;
        }
    }
}