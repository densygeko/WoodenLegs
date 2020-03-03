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
        private FilesContainer files;
        private List<directory> directories; 
        public FileController()
        {
            files = FilesContainer.getInstance();
            directories = new List<directory>();
        }

        public void Getfiles(string path)
        {
            directory maindir = new directory(path);
            directories.Add(maindir);
            int trueres = 0;
            while(directories.Count != trueres)
            {
                for (int i = 0; i < directories.Count; i++)
                {
                    if (directories[i].read == false)
                    {
                        string[] dir = Directory.GetDirectories(directories[i].path);
                        foreach (var item1 in dir)
                        {
                            directory newdir = new directory(item1);
                            directories.Add(newdir);
                        }
                        directories[i].read = true;
                        trueres++;
                    }
                }
            }
            foreach (var item in directories)
            {
                Sortfiles(Directory.GetFiles(item.path));
            }
        }
        public void Sortfiles(string[] incfiles)
        {
            foreach (var item in incfiles)
            {
                string supstring = item.Substring(item.LastIndexOf(".") + 1);
                supstring = supstring.ToUpper();
                switch (supstring)
                {
                    case "PDF":
                        files.Getpdfs().Add(item);
                        break;
                    case "PCAP":
                        files.getpcaps().Add(item);
                        break;
                    case "PNG":
                        files.GetPictures().Add(item);
                        break;
                    case "XML":
                        files.GetPictures().Add(item);
                        break;
                    case "JPEG":
                        files.GetPictures().Add(item);
                        break;
                    case "JPG":
                        files.GetPictures().Add(item);
                        break;
                    default:
                        break;
                }
            }
        }
        public List<List<string>> GetAllfiletypes()
        {
            return files.Getfiletypes();
        }

        public List<string> getpdf()
        {
            return files.Getpdfs();
        }
        public List<string> getxmls()
        {
            return files.getxmls();
        }
        public List<string> getpcaps()
        {
            return files.GetPictures();

        }
       
        public List<string> getpictures()
        {
        return files.GetPictures();
        }
    }
}