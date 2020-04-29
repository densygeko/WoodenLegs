using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using ControllerLayer;

namespace GUI
{
    /// <summary>
    /// Interaction logic for InsertFiles.xaml
    /// </summary>
    public partial class InsertFiles : Window
    {
        public InsertFiles()
        {
            InitializeComponent();
        }


        //Browser button
        private void Browse_Click(object sender, RoutedEventArgs e)
        {
            using (FolderBrowserDialog FBD = new FolderBrowserDialog())
            {
                string folderPath;
                FBD.ShowDialog();
                if (FBD.SelectedPath != null)
                {
                    folderPath = FBD.SelectedPath;
                    Textbox.Text = folderPath;
                }
            }
        }
        private void Confirm_Click(object sender, RoutedEventArgs e)
        {
            string path;
            path = Textbox.Text;
            FileController Fctr = new FileController();
            Fctr.Getfiles(path);
            //close window
            MainWindow mian = new MainWindow();
            mian.Show();
            Close();
        }
    }
}
