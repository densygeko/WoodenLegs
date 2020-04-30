using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControllerLayer
{
    public class cmdluncherController
    {
        public void start()
        {
            LaunchCommandLineApp();
        }
        public static void LaunchCommandLineApp()
        {
            XmlController xml = new XmlController();
            string exestirng = xml.GetXMLpath() + @"Main2\dist\Main2.exe"; //makes the path for exe file in use
            string xmlstring = xml.GetXMLpath() + "filepaths.xml"; //makes a path for the agurment for the exe file


            ProcessStartInfo startInfo = new ProcessStartInfo(); //makes a class there Specifies a set of values that are used when you start a process.
            startInfo.CreateNoWindow = true; //makes sure if the exe has a ui it will not pop up.
            startInfo.FileName = exestirng; //use the path string made above.
            startInfo.WindowStyle = ProcessWindowStyle.Hidden; //hide cmd if that in use in the exe file.
            startInfo.Arguments = xmlstring; //putting the argurments with exe file
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
