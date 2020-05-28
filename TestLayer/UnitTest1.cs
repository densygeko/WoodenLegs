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
        public void testxml()
        {
            
            XmlController xml = new XmlController();

            xml.InsertblackList();
        }

        [TestMethod]
        public void testblacklist()
        {
            XmlController xml = new XmlController();
            xml.DeleteBlacklistKeyword("88 99 33 88");
        }

        [TestMethod]
        public void testrun()
        {
            cmdlauncherController cmdluncher = new cmdlauncherController();
            cmdluncher.start();
        }
    }
}
