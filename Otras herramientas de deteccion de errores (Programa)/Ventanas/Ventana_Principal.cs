using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prueba2
{
    public partial class Ventana_Principal : Form
    {

        private Ventana_A ventanaA;
        private Ventana_B ventanaB;
        private Ventana_C ventanaC;
        private Ventana_SDR ventanaSDR;

        private const int WN_NCLBUTOONDBCLK = 0x00A3; //Mensaje de doble clic 
        public Ventana_Principal()
        {
            InitializeComponent();
        }

        protected override void WndProc(ref Message m)
        {
            //Verificar si el mensaje es un doble clic en la barra de titulo
            if (m.Msg == WN_NCLBUTOONDBCLK)
            {
                //No hacer para para evitar la maximinazion por doble clic
                return;
            }
            base.WndProc(ref m);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DateTime horaActual = DateTime.Now;
            labelHora.Text = "Hora de ejecución: " + horaActual.ToString();


        }


        private void configuracion_Click(object sender, EventArgs e)
        {
            //Crear una instancia del formulario de configuracion
            ConfiguracionForm configuracionForm = new ConfiguracionForm();

            //Mostrar el formulario de configuracion como un dialogo modal
            DialogResult result = configuracionForm.ShowDialog();

            //Comprobar si el usuario cerró el diálogo de configuracion
            if (result == DialogResult.OK)
            {

            }

        }

        private void conexionALaBaseDeDatosToolStripMenuItem_Click(object sender, EventArgs e)
        {

            //Crear una instancia del formulario de conexion
            Conexion conexionForm = new Conexion();

            //Mostrar el formulario de conexion como un dialogo modal
            DialogResult result = conexionForm.ShowDialog();

            //Comprobar si el usuario cerró el dialogo de conexion
            if (result == DialogResult.OK)
            {

            }

        }

        private void btnNaveA_Click(object sender, EventArgs e)
        {
            if (ventanaA == null || ventanaA.IsDisposed)
            {
                ventanaA = new Ventana_A();
            }

            if (!ventanaA.Visible)
            {
                ventanaA.Show();
            }
            else
            {
                ventanaA.Focus();
            }


        }

        private void btnNaveB_Click(object sender, EventArgs e)
        {
            if (ventanaB == null || ventanaB.IsDisposed)
            {
                ventanaB = new Ventana_B();
            }

            if (!ventanaB.Visible)
            {
                ventanaB.Show();
            }
            else
            {
                ventanaB.Focus();
            }
        }

        private void btnNaveC_Click(object sender, EventArgs e)
        {
            if (ventanaC == null || ventanaC.IsDisposed)
            {
                ventanaC = new Ventana_C();
            }

            if (!ventanaC.Visible)
            {
                ventanaC.Show();
            }
            else
            {
                ventanaC.Focus();
            }
        }

        private void btnNaveSDR_Click(object sender, EventArgs e)
        {
            if (ventanaSDR == null || ventanaSDR.IsDisposed)
            {
                ventanaSDR = new Ventana_SDR();
            }

            if (!ventanaSDR.Visible)
            {
                ventanaSDR.Show();
            }
            else
            {
                ventanaSDR.Focus();
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click_1(object sender, EventArgs e)
        {

        }

        private void infoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //Crear una instancia del formulario de creditos
            Creditos creditos = new Creditos();

            //Mostrar el formulario de conexion como un dialogo modal
            DialogResult result = creditos.ShowDialog();

            //Comprobar si el usuario cerró el dialogo de conexion
            if (result == DialogResult.OK)
            {

            }
        }


      
    }

}
