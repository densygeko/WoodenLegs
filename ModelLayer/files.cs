using Microsoft.Azure.Amqp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModelLayer
{
    public sealed class FilesContainer
    {
        private static FilesContainer instance;
        private List<string> pdfs;
        private List<string> pcaps;
        private List<string> billedeFiler;
        private List<string> xmls;
        private List<List<string>> fileTypes;
        protected FilesContainer()
        {
            pdfs = new List<string>();
            pcaps = new List<string>();
            billedeFiler = new List<string>();
            xmls = new List<string>();
            fileTypes = new List<List< string >>();
            fileTypes.Add(pdfs);
            fileTypes.Add(pcaps);
            fileTypes.Add(billedeFiler);
            fileTypes.Add(xmls);
        }

        public static FilesContainer getInstance()
        {
            if (instance == null)
            {
                instance = new FilesContainer();
            }
            return instance;
        }
        public List<List<string>> Getfiletypes()
        {
            return fileTypes;
        }
        public List<string> Getpdfs()
        {
            return pdfs;
        }
        public List<string> getpcaps()
        {
            return pcaps;
        }
        public List<string> GetPictures()
        {
            return billedeFiler;
        }
        public List<string> getxmls()
        {
            return xmls;
        }
    }
}
