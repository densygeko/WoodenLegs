using System;
using ModelLayer;
using ControllerLayer;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.IO;

namespace TestLayer
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void testgetallpdf()
        {
            //Arange
            //need to make an instance of the classe in testing
            FilesContainer Fcon = FilesContainer.getInstance();
            FileController Fctr = new FileController();
           
            //act
            //using the testfolder the in the TestLayer + bin + debug+test \\ 
            string folderoath = Directory.GetCurrentDirectory();
            Fctr.Getfiles(folderoath + @"\test\");
            //Asert
            //checks that the amount of pdfs are 5 would mean that method have found all the pdfs in the testing folder
            Assert.AreEqual<int>(5, Fcon.pdfs.Count);
        }

        [TestMethod]
        public void testxml()
        {
            FileController Fctr = new FileController();
            XmlController xml = new XmlController();
            Fctr.Getfiles(xml.GetXMLpath() + @"WoddenLegs\ControlLayer\TempPDFHolder");
        }

        [TestMethod]
        public void testblacklist()
        {
            XmlController xml = new XmlController();
            xml.makeXmlfile();
        }

        [TestMethod]
        public void testrun()
        {
            cmdluncherController cmdluncher = new cmdluncherController();
            cmdluncher.start();
        }
    }
}
