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
using ControllerLayer;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Ui
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        //when you click on the browser bottom
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            using (FolderBrowserDialog FBD = new FolderBrowserDialog())
            {
                string folderPath;
                FBD.ShowDialog();
                if(FBD.SelectedPath != null)
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
            
        }
    }
}
