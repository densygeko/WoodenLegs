using System;
using ModelLayer;
using ControllerLayer;
using Microsoft.VisualStudio.TestTools.UnitTesting;

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
            //using the testfolder the in the TestLayer \\ folder needs to updata on every pull from github\\ need a fix for this
            Fctr.Getfiles(@"C:\Users\Bruger\Desktop\Wodden-legs\WoddenLegs\TestLayer\test\");
            //Asert
            //checks that the amount of pdfs are 5 would mean that method have found all the pdfs in the testing folder
            Assert.AreEqual<int>(5, Fcon.pdfs.Count);
        }
    }
}
