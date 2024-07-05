/** @odoo-module */
import { Component, useState, useRef, onMounted } from '@odoo/owl';


export class MainView extends Component {
    static template = "main_view.MainView" /* deve sempre coincidere con l'attributo t-name del nodo <template> */

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

    async onSendText() {
        this.button.el.value = "Attendere prego";
        /* Chiamata BE o FE? */
    }
}

 