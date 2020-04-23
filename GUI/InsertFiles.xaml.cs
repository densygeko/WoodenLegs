using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

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

        /*
        private void Button_Click(object sender, RoutedEventArgs e)
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

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            string path;
            path = Textbox.Text;
            FileController Fctr = new FileController();
            DisplayIdentifier displayIdentifier = new DisplayIdentifier();
            this.NavigationService.Navigate(displayIdentifier);

        }
        */

    }
}
