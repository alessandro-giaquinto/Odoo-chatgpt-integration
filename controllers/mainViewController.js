/** @odoo-module */
import { Component, useState } from '@odoo/owl';


export class MainViewController extends Component {
    static template = "my_module.MainView" /* Cambia my_module nel nome effettivo del modulo */

    setup() {
        this.state = useState({value: "Inserisci qui il testo da sottoporre a chatGPT"}) /* Inizializza la text area con un campo predefinito */
    }
}

 