using Microsoft.Azure.Amqp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModelLayer
{
    //In c#, sealed is a keyword that is used to stop inheriting the particular class from other classes and we can also prevent 
    //overriding the particular properties or methods based on our requirements.

    //this class is made as a singelton
    //with in mind of holding all the file by haveing a list of list of strings that hold the filepaths of s specific type

    //this class has not make made super safe for treading
    public sealed class FilesContainer
    {
        //holding the instance helping to make sure there 1 instance, standart for the singelton patton
        private static FilesContainer instance;
        //list for the file type pdf
        public List<string> pdfs { get; }
        //list of the file type pcap
        public List<string> pcaps { get; }
        //list of the picture filetype
        public List<string> PictureFiles { get; }
        //list of the filetype xml
        public List<string> xmls { get; }
        //list of the filetype texts
        public List<string> Texts { get; }
        //list of csv files 
        public List<string> Csvs { get;  }
        //the list of list of string has all the list of above 
        public List<List<string>> fileTypes { get; }

        //The keyword "protects" the class from having its' constructor called by external classes.
        //However unlike the private keyword, protected will allow derived classes to access the class member. 
        //Classes that use it will employ other means to create instances of the class
        public FilesContainer()
        {
            pdfs = new List<string>();
            pcaps = new List<string>();
            PictureFiles = new List<string>();
            xmls = new List<string>();
            fileTypes = new List<List< string >>();
            Texts = new List<string>();
            Csvs = new List<string>();
            fileTypes.Add(pdfs);
            fileTypes.Add(pcaps);
            fileTypes.Add(PictureFiles);
            fileTypes.Add(xmls);
        }

        //this method are used to make an instance of the class and can only beone
        public static FilesContainer getInstance()
        {
            if (instance == null)
            {
                instance = new FilesContainer();
            }
            return instance;
        }
    }
}
