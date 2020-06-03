using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Globalization;
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
using ControllerLayer;
using ModelLayer;

namespace GUI
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private Identifier _selectedIdentifier;
        private XmlController XmlController = new XmlController();
        private string _sleectedBlacklistKeyword;
        public MainWindow()
        {
            InitializeComponent();
            loadIdentifiers();
            CheckforBlacklist();
           // this.DisplayIdentifierDataGrid.ItemsSource = XmlController.ReadIdentifierFromXml();
        }

        public void loadIdentifiers()
        {
            this.DisplayIdentifierDataGrid.ItemsSource = XmlController.ReadIdentifierFromXml();
        }

        // Asks the user if they are sure that they want to close the application
        private void ButtonCloseApplication_Click(object sender, RoutedEventArgs e)
        {
            MessageBoxResult result = MessageBox.Show("Alt du har arbejdet på går tabt, er du sikker på at du vil lukke applikationen?", "", MessageBoxButton.YesNo);
            switch (result)
            {
                case MessageBoxResult.Yes:
                    Application.Current.Shutdown();
                    break;
                case MessageBoxResult.No:
                    break;
            }
        }


        private void ButtonInsertDoc_Click(object sender, RoutedEventArgs e)
        {
            InsertFiles insertFilesWindow = new InsertFiles();
            insertFilesWindow.Topmost = true;
            insertFilesWindow.Show();
            Close();
        }

        private void ButtonCloseMenu_Click(object sender, RoutedEventArgs e)
        {
            ButtonOpenMenu.Visibility = Visibility.Visible;
            ButtonCloseMenu.Visibility = Visibility.Collapsed;
        }

        private void ButtonOpenMenu_Click(object sender, RoutedEventArgs e)
        {
            ButtonOpenMenu.Visibility = Visibility.Collapsed;
            ButtonCloseMenu.Visibility = Visibility.Visible;
        }

        private void blacklist_Click(object sender, RoutedEventArgs e)
        {
            BlackListData.ItemsSource = XmlController.GetBlacklistkeywords();
            if (BlackListData.Visibility == Visibility.Hidden)
            {
                BlackListData.Visibility = Visibility.Visible;
                BlackListTextBox.Text = "Skjul blacklist";
                BlackListIcon.Foreground = Brushes.Black;
            }
            else
            {
                BlackListData.Visibility = Visibility.Hidden;
                BlackListTextBox.Text = "Vis blacklist";
                BlackListIcon.Foreground = Brushes.White;
            }
        }

        
        private void DisplayIdentifierDataGrid_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            Identifier identifier = (Identifier)this.DisplayIdentifierDataGrid.CurrentItem;
            if (_selectedIdentifier != identifier)
            {
                _selectedIdentifier = identifier;
                nofiChanged(_selectedIdentifier);
            }
        }

        public void nofiChanged(Identifier identifier1)
        {
            try
            {
                this.DataGridDisplayPaths.ItemsSource = _selectedIdentifier.Paths;
            }
            catch
           {
                this.DataGridDisplayPaths.ItemsSource = null;
            }
        }

        private void IdentifireListRight_Click(object sender, RoutedEventArgs e)
        {
            XmlController.InsertBlacklistKeyword(_selectedIdentifier.identifier);
            XmlController.TrunIsblacklisted(_selectedIdentifier.identifier);
            BlackListData.ItemsSource = XmlController.GetBlacklistkeywords();
            loadIdentifiers();
        }
        
        private void Email_buttonClick(object sender, MouseButtonEventArgs e)
        {
            bool email = XmlController.GetBlacklistType()[0];
            if (email == true)
            {
                email = false;
                XmlController.UpdateBlacklistTypeEmail(email);
            } 
            else
            {
                email = true;
                XmlController.UpdateBlacklistTypeEmail(email);
            }
            CheckforBlacklist();
            loadIdentifiers();
        }

        private void CheckforBlacklist()
        {
            try
            {
                List<bool> blacklistTypes = XmlController.GetBlacklistType();
                if (blacklistTypes[0] == true)
                {
                    EmailIcon.Foreground = Brushes.Black;
                }
                else
                {
                    EmailIcon.Foreground = Brushes.White;
                }

                if (blacklistTypes[2] == true)
                {
                    NumberIcon.Foreground = Brushes.Black;
                }
                else
                {
                    NumberIcon.Foreground = Brushes.White;
                }
                if (blacklistTypes[1] == true)
                {
                    IpIcon.Foreground = Brushes.Black;
                }
                else
                {
                    IpIcon.Foreground = Brushes.White;
                }
            }
            catch
            {
                
            }
            
            
        }

        private void Ip_buttonClick(object sender, MouseButtonEventArgs e)
        {
            bool Ip = XmlController.GetBlacklistType()[1];
            if (Ip == true)
            {
                Ip = false;
            }
            else
            {
                Ip = true;
            }
            XmlController.UpdateBlacklistTypeIP(Ip);
            CheckforBlacklist();
            loadIdentifiers();
        }

        private void Number_buttonClick(object sender, MouseButtonEventArgs e)
        {
            bool Number = XmlController.GetBlacklistType()[2];
            if (Number == true)
            {
                Number = false;
            }
            else
            {
                Number = true;
            }
            XmlController.UpdateBlacklistTypeNumber(Number);
            CheckforBlacklist();
            loadIdentifiers();
        }

        private void blacklist_Rightclick(object sender, RoutedEventArgs e)
        {
            XmlController.DeleteBlacklistKeyword(_sleectedBlacklistKeyword);
            XmlController.TrunIsblacklisted(_sleectedBlacklistKeyword);
            BlackListData.ItemsSource = XmlController.GetBlacklistkeywords();
            loadIdentifiers();
        }

        private void BlackListData_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            string chagedstring = (string)this.BlackListData.CurrentItem;
            if(_sleectedBlacklistKeyword != chagedstring)
            {
                _sleectedBlacklistKeyword = chagedstring;
            }
        }
    }
}
