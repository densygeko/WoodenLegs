using System;
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
            FileController Fctr = new FileController();
            //act
            Fctr.Getfiles(@"C:\Users\Uth\Desktop\WoddenLegs\TestLayer\test\");
            //Asert
            Assert.AreEqual<int>(5, Fctr.getpdf().Count);
        }
    }
}
