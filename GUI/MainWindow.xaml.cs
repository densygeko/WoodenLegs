﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
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
        public MainWindow()
        {
            InitializeComponent();
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
           
        }
    }
}
