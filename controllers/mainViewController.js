/** @odoo-module */
import { Component, useState, useRef, onMounted } from '@odoo/owl';


export class MainViewController extends Component {
    static template = "my_module.MainView" /* Cambia my_module nel nome effettivo del modulo */

    /* Richiama gli hook qui dentro, serve la lettura ORM dell'API per il token */
    setup() {
        this.state = useState({value: "Inserisci qui il testo da sottoporre a chatGPT"}); /* Inizializza la text area con un campo predefinito */
        /* Aggancia textarea e button */
        this.textArea = useRef("text_chat_gpt");
        this.button = useRef("button_chat_gpt");

        /* Test */
        onMounted(() => {
            console.log(this.state);
            console.log(this.textArea.el); // ref -> el
            console.log(this.button.el);
        });
    }
}

 