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
            string exestirng = @"C:\Users\Uth\Desktop\WoddenLegs\WoddenLegs\dist\Main2.exe";
            string xmlstring = xml.GetXMLpath() + "filepaths.xml";


            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.CreateNoWindow = false;
            startInfo.FileName = exestirng;
            startInfo.WindowStyle = ProcessWindowStyle.Maximized;
            startInfo.Arguments = xmlstring;

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
