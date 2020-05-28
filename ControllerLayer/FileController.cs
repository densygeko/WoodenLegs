using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ModelLayer;

namespace ControllerLayer
{
    public class FileController
    {
        // makes a instance of the fileContainer, this is used to sort the files
        private FilesContainer files;
        // need make a List of directories, to make sure we got all the files from all the folders
        private List<directory> directories;

        private XmlController xmlController = new XmlController();
        private cmdlauncherController cmd = new cmdlauncherController();
        public FileController()
        {
            files = FilesContainer.getInstance();
            directories = new List<directory>();
        }

        //this metod are getting the path of the root folder, from the root folder they get all the under directories 
        // If there are files in the root directionary those files will be added to the list "directories"
        public void Getfiles(string path)
        {
            //makeing the root path into a directory class
            // and adding it to the list of directory in case there are files in the root directory too 
            directory maindir = new directory(path);
            directories.Add(maindir);
            //loops tropugh the list of directoies, it starts on 1 which is the root in the list of  directory ("dirctories")
            int trueres = 0;
            //this while loop stops then we have checked every directory in the list of directory for under directories
            while(directories.Count != trueres)
            {
                //loop tho the list of directory it stats on 1 with the root directory
                for (int i = 0; i < directories.Count; i++)
                {
                    //check if already read 
                    if (directories[i].read == false)
                    {
                        //create a list of all the under directories paths
                        string[] dir = Directory.GetDirectories(directories[i].path);
                        //loop tho the list of the under directories
                        foreach (var item1 in dir)
                        {
                            //makeing each under directories path into a direcoty class
                            directory newdir = new directory(item1);
                            //adding it to the list of class directory
                            directories.Add(newdir);
                        }
                        //swich boolean variable in the directory class to read so not gonna be read again this while loop
                        directories[i].read = true;
                        //cout up the number of read directorys
                        trueres++;
                    }
                }
            }
            //at this point we have gotton all the under directories from the root directory
            //we are looping tho all the directories
            foreach (var item in directories)
            {
                //we are sorting all the files in all the directories
                Sortfiles(Directory.GetFiles(item.path));
            }
            xmlController.MakeXmlfile(); //makes the xmlfile
            xmlController.Insertpathtoxmldoc(); //insert the paths we found
            cmd.start(); //start the pyton program through the commandline
            xmlController.InsertblackList(); //Insert the blacklist to the xml file
        }
        //this is a method for sortingfiles the input are a array of string(file paaths)
        public void Sortfiles(string[] incfiles)
        {
            //looping tho incomming aray
            foreach (var item in incfiles)
            {
                //makeing a supstring of the incomming path after the last dot, this is file type
                string supstring = item.Substring(item.LastIndexOf(".") + 1);
                //makeing it to upper case because some filetype are anme "Pdf or Jpg"
                supstring = supstring.ToUpper();
                //this string switch takes the supstring and adding file to the right list so we are ready to pull data from the files
                switch (supstring)
                {
                    case "PDF":
                        files.pdfs.Add(item);
                        break;
                    case "PCAP":
                        files.pcaps.Add(item);
                        break;
                    case "PNG":
                        files.PictureFiles.Add(item);
                        break;
                    case "XML":
                        files.xmls.Add(item);
                        break;
                    case "JPEG":
                        files.PictureFiles.Add(item);
                        break;
                    case "JPG":
                        files.PictureFiles.Add(item);
                        break;
                    case "CSV":
                        files.Csvs.Add(item);
                        break;
                    case "TXT":
                        files.Texts.Add(item);
                        break;
                    default:
                        break;
                }
            }
        }
    }
}