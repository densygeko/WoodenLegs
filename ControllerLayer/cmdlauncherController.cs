using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControllerLayer
{
    public class cmdlauncherController
    {
        public void start()
        {
            LaunchCommandLineApp();
        }
        public static void LaunchCommandLineApp()
        {
            XmlController xml = new XmlController();
            string exestring = xml.GetXMLpath() + @"Main2\dist\Main2.exe"; //makes the path for exe file in use
            string xmlstring = xml.GetXMLpath() + "filepaths.xml"; //finding the xml file

            ProcessStartInfo startInfo = new ProcessStartInfo(); //makes a class that specifies a set of values which are used when you start a process.
            startInfo.CreateNoWindow = true; //makes sure if the exe has a ui it will not pop up.
            startInfo.FileName = exestring; //use the path string made above.
            startInfo.WindowStyle = ProcessWindowStyle.Maximized; //hide cmd
            startInfo.Arguments = xmlstring; //putting the arguments with exe file
            startInfo.WorkingDirectory = xml.GetXMLpath()+ @"Main2\dist"; //the output from the exe file, will be in the working directory because of the way the exe file is coded
            
            try
            {
                // Start the process with the info we specified.
                // Call WaitForExit and then the using statement will close.
                using (Process exeProcess = Process.Start(startInfo))
                {
                    exeProcess.WaitForExit();
                }
            }
            catch
            {
                // Log error.
            }
        }
    }
}
