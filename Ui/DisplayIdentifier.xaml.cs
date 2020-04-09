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
using System.Windows.Navigation;
using System.Windows.Shapes;
using ModelLayer;

namespace Ui
{
    /// <summary>
    /// Interaction logic for DisplayIdentifier.xaml
    /// </summary>
    public partial class DisplayIdentifier : Page
    {
        Email selection = null;
        public DisplayIdentifier()
        {

            Email email = new Email(1, "d:/tabebr", "noget@tin.et", 2);
            Email email2 = new Email(2, "d:/tabebr", "noget@fnoget.et", 1);
            Email email3 = new Email(3, "d:/tabebr", "noget2@noget.et", 3);
            Email email4 = new Email(4, "d:/tabebr", "noget1@noget.et", 4);
            Email email5 = new Email(5, "d:/tabebr", "noge3t@noget.et", 5);
            List<Email> emails = new List<Email>();
            emails.Add(email);
            emails.Add(email2);
            emails.Add(email3);
            List<Email> blackEmails = new List<Email>();
            blackEmails.Add(email4);
            blackEmails.Add(email5);
            InitializeComponent();
            DataIdentifier.ItemsSource = emails;
            DataBlacklist.ItemsSource = blackEmails;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            if (selection != null)
            {
                displaypath displaypath = new displaypath();
                displaypath.path = selection.path;
                displaypath.identifier = selection.identifier;
                List<displaypath> dps = new List<displaypath>();
                dps.Add(displaypath);
                for (int i = 0; i < selection.gane_fundet; i++)
                {
                    displaypath dp = new displaypath();
                    dp.identifier = selection.identifier;
                    dp.path = selection.path + i.ToString();
                    dps.Add(dp);
                    DataDisplayPath.ItemsSource = dps;
                }

            }
        }

        private void DataIdentifier_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            var row = (Email)DataIdentifier.SelectedItem;
            if (row != null)
            {
                selection = row;
            }
        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
           
        }

        private void Button_Click_3(object sender, RoutedEventArgs e)
        { 
            
            if (this.DataBlacklist.Visibility == System.Windows.Visibility.Hidden)
            {
                
                this.DataBlacklist.Visibility = System.Windows.Visibility.Visible;
                this.FjernFraBlackListbtn.Visibility = System.Windows.Visibility.Visible;
                this.AddTypeBtn.Visibility = System.Windows.Visibility.Visible;
                this.EmailBox.Visibility = System.Windows.Visibility.Visible;
                this.IpBox.Visibility = System.Windows.Visibility.Visible;
                this.TelephoneBox.Visibility = System.Windows.Visibility.Visible;
                this.BlacklistLabel.Visibility = System.Windows.Visibility.Visible;
                this.BlacklistOptsBtn.Content = "Hide blacklist options";
                this.BlackRec.Visibility = System.Windows.Visibility.Visible;
                this.DataIdentifier.Height = 440;
                this.DataDisplayPath.Height = 440;


            }
            else if (this.DataBlacklist.Visibility == System.Windows.Visibility.Visible)
            {
                this.DataBlacklist.Visibility = System.Windows.Visibility.Hidden;
                this.FjernFraBlackListbtn.Visibility = System.Windows.Visibility.Hidden;
                this.AddTypeBtn.Visibility = System.Windows.Visibility.Hidden;
                this.EmailBox.Visibility = System.Windows.Visibility.Hidden;
                this.IpBox.Visibility = System.Windows.Visibility.Hidden;
                this.TelephoneBox.Visibility = System.Windows.Visibility.Hidden;
                this.BlacklistLabel.Visibility = System.Windows.Visibility.Hidden;
                this.BlacklistOptsBtn.Content = "Blacklist options";
                this.BlackRec.Visibility = System.Windows.Visibility.Hidden;
                this.DataIdentifier.Height = 828;
                this.DataDisplayPath.Height = 738;
            }


        }
    }

    partial class displaypath
    {
       public string identifier { set; get; }
       public string path { set; get; }
    }
}
