/** @odoo-module **/

import { mount, whenReady } from "@odoo/owl";
import { MainView } from "./mainView";
import { templates } from "@web/core/assets";

// Monta la pagina quando document.body è pronto
whenReady(() => {
    // Inserire qui il token OpenAI
    const token = "";
    mount(MainView, document.body, { templates, dev: true, name: "Odoo ChatGPT Integration"});
});